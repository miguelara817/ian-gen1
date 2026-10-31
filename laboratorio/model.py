"""Transformer causal compacto con bloques de atención multi-cabeza."""

from dataclasses import asdict, dataclass

import torch
from torch import nn
from torch.nn import functional as F


@dataclass
class ModelConfig:
    block_size: int = 96
    n_embd: int = 96
    n_head: int = 4
    n_layer: int = 3
    dropout: float = 0.1


class CausalSelfAttention(nn.Module):
    def __init__(self, config: ModelConfig):
        super().__init__()
        if config.n_embd % config.n_head:
            raise ValueError("n_embd debe ser divisible por n_head")
        self.attn = nn.MultiheadAttention(
            config.n_embd, config.n_head, dropout=config.dropout, batch_first=True
        )
        self.register_buffer(
            "mask", torch.triu(torch.ones(config.block_size, config.block_size, dtype=torch.bool), diagonal=1)
        )
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        length = x.size(1)
        attended, _ = self.attn(
            x, x, x, attn_mask=self.mask[:length, :length], need_weights=False
        )
        return self.dropout(attended)


class Block(nn.Module):
    def __init__(self, config: ModelConfig):
        super().__init__()
        self.ln1 = nn.LayerNorm(config.n_embd)
        self.attention = CausalSelfAttention(config)
        self.ln2 = nn.LayerNorm(config.n_embd)
        self.mlp = nn.Sequential(
            nn.Linear(config.n_embd, 4 * config.n_embd),
            nn.GELU(),
            nn.Linear(4 * config.n_embd, config.n_embd),
            nn.Dropout(config.dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attention(self.ln1(x))
        return x + self.mlp(self.ln2(x))


class TinyGPT(nn.Module):
    def __init__(self, config: ModelConfig, vocab_size: int):
        super().__init__()
        self.config = config
        self.token_embedding = nn.Embedding(vocab_size, config.n_embd)
        self.position_embedding = nn.Embedding(config.block_size, config.n_embd)
        self.blocks = nn.Sequential(*(Block(config) for _ in range(config.n_layer)))
        self.final_norm = nn.LayerNorm(config.n_embd)
        self.lm_head = nn.Linear(config.n_embd, vocab_size)
        self.apply(self._init_weights)

    @staticmethod
    def _init_weights(module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, indices: torch.Tensor, targets: torch.Tensor | None = None):
        _, length = indices.shape
        if length > self.config.block_size:
            raise ValueError("La secuencia excede block_size")
        positions = torch.arange(length, device=indices.device)
        x = self.token_embedding(indices) + self.position_embedding(positions)
        logits = self.lm_head(self.final_norm(self.blocks(x)))
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.reshape(-1, logits.size(-1)), targets.reshape(-1))
        return logits, loss

    @torch.no_grad()
    def generate(self, indices: torch.Tensor, max_new_tokens: int, temperature: float = 1.0):
        self.eval()
        for _ in range(max_new_tokens):
            context = indices[:, -self.config.block_size :]
            logits, _ = self(context)
            probabilities = F.softmax(logits[:, -1, :] / temperature, dim=-1)
            next_token = torch.multinomial(probabilities, num_samples=1)
            indices = torch.cat((indices, next_token), dim=1)
        return indices

    def config_dict(self) -> dict:
        return asdict(self.config)
