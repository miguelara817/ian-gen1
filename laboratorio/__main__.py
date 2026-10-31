"""Comandos para entrenar y generar con el laboratorio."""

import argparse

import torch

from laboratorio.data import CharDataset
from laboratorio.model import ModelConfig, TinyGPT
from laboratorio.train import train


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m laboratorio")
    subparsers = parser.add_subparsers(dest="command", required=True)

    training = subparsers.add_parser("train", help="Entrena un modelo desde cero")
    training.add_argument("--steps", type=int, default=500)
    training.add_argument("--run-id", required=True)
    training.add_argument("--seed", type=int, default=1337)

    generation = subparsers.add_parser("generate", help="Genera texto desde un checkpoint")
    generation.add_argument("--checkpoint", required=True)
    generation.add_argument("--prompt", default="")
    generation.add_argument("--tokens", type=int, default=300)
    generation.add_argument("--temperature", type=float, default=0.8)

    args = parser.parse_args()
    if args.command == "train":
        if args.steps < 1:
            parser.error("--steps debe ser mayor que cero")
        train(args.steps, args.run_id, args.seed)
        return

    saved = torch.load(args.checkpoint, map_location="cpu", weights_only=True)
    config = ModelConfig(**saved["config"])
    dataset = CharDataset.from_text(saved["text"])
    model = TinyGPT(config, dataset.vocab_size)
    model.load_state_dict(saved["model"])
    if args.temperature <= 0:
        parser.error("--temperature debe ser mayor que cero")
    ids = dataset.encode(args.prompt) if args.prompt else [dataset.stoi["\n"]]
    output = model.generate(torch.tensor([ids]), args.tokens, args.temperature)
    print(dataset.decode(output[0].tolist()))


if __name__ == "__main__":
    main()
