"""Bucle de entrenamiento y registro local de experimentos."""

import json
import random
from datetime import datetime, timezone
from pathlib import Path

import torch

from laboratorio.data import CharDataset, get_batch
from laboratorio.model import ModelConfig, TinyGPT

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "data" / "corpus.txt"
ARTIFACTS = ROOT / "artifacts"


def train(steps: int, run_id: str, seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dataset = CharDataset.from_file(CORPUS)
    train_data, val_data = dataset.split()
    config = ModelConfig()
    model = TinyGPT(config, dataset.vocab_size).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

    def evaluate(data: torch.Tensor) -> float:
        model.eval()
        with torch.no_grad():
            values = [
                model(*get_batch(data, 16, config.block_size, device))[1].item()
                for _ in range(10)
            ]
        model.train()
        return sum(values) / len(values)

    model.train()
    for step in range(steps):
        x, y = get_batch(train_data, 16, config.block_size, device)
        _, loss = model(x, y)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

    train_loss = evaluate(train_data)
    val_loss = evaluate(val_data)
    prompt = "La " if all(char in dataset.stoi for char in "La ") else ""
    start_ids = dataset.encode(prompt) if prompt else [0]
    start = torch.tensor([start_ids], device=device)
    sample = dataset.decode(model.generate(start, 240, temperature=0.8)[0].cpu().tolist())

    checkpoints = ARTIFACTS / "checkpoints"
    checkpoints.mkdir(parents=True, exist_ok=True)
    checkpoint = checkpoints / f"{run_id}.pt"
    if checkpoint.exists():
        raise FileExistsError(f"Ya existe {checkpoint}; usa otro --run-id para conservar ambos.")
    torch.save(
        {"model": model.cpu().state_dict(), "config": model.config_dict(), "text": dataset.text},
        checkpoint,
    )
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "seed": seed,
        "steps": steps,
        "device": device,
        "corpus_chars": len(dataset.text),
        "vocab_size": dataset.vocab_size,
        "config": config.__dict__,
        "train_loss": train_loss,
        "val_loss": val_loss,
        "sample": sample,
        "checkpoint": str(checkpoint.relative_to(ROOT)),
    }
    log_path = ARTIFACTS / "experiments.jsonl"
    with log_path.open("a", encoding="utf-8") as log:
        log.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Dispositivo: {device} | train_loss: {train_loss:.4f} | val_loss: {val_loss:.4f}")
    print(f"Checkpoint: {checkpoint}\nRegistro: {log_path}\n\nMuestra:\n{sample}")
