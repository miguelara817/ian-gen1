"""Preparación sencilla de datos a nivel de carácter."""

from pathlib import Path

import torch


class CharDataset:
    def __init__(self, text: str):
        if len(text) < 20:
            raise ValueError("El corpus debe contener al menos 20 caracteres.")
        self.text = text
        self.chars = sorted(set(text))
        self.stoi = {char: index for index, char in enumerate(self.chars)}
        self.itos = {index: char for char, index in self.stoi.items()}
        self.data = torch.tensor(self.encode(text), dtype=torch.long)

    @classmethod
    def from_file(cls, path: str | Path) -> "CharDataset":
        return cls(Path(path).read_text(encoding="utf-8"))

    def encode(self, text: str) -> list[int]:
        unknown = sorted(set(text) - set(self.stoi))
        if unknown:
            raise ValueError(f"El texto contiene caracteres fuera del vocabulario: {unknown!r}")
        return [self.stoi[char] for char in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.itos[index] for index in ids)

    @property
    def vocab_size(self) -> int:
        return len(self.chars)

    def split(self, fraction: float = 0.9) -> tuple[torch.Tensor, torch.Tensor]:
        split_at = int(len(self.data) * fraction)
        return self.data[:split_at], self.data[split_at:]


def get_batch(data: torch.Tensor, batch_size: int, block_size: int, device: str):
    if len(data) <= block_size:
        raise ValueError("Cada partición debe ser más larga que block_size.")
    starts = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i : i + block_size] for i in starts])
    y = torch.stack([data[i + 1 : i + block_size + 1] for i in starts])
    return x.to(device), y.to(device)
