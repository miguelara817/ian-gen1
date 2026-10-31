# Repository notes

- This is a single Python project; the executable entry point is `python -m laboratorio` (`laboratorio/__main__.py`). There is no packaging/build system or test suite configured.
- Install dependencies from the repository root with `python -m pip install -r requirements.txt`; PyTorch's platform-specific install may be needed for CUDA. Python 3.10+ is documented.
- Main workflows from the root: `python -m laboratorio train --steps 500 --run-id <unique-id>` and `python -m laboratorio generate --checkpoint artifacts/checkpoints/<id>.pt --prompt "..."`.
- Training reads only `data/corpus.txt`, splits it sequentially into train/validation, and writes checkpoints plus JSONL experiment records under ignored `artifacts/`. Each run ID must be unique; generated artifacts are not source files.
- Model/data/training implementation lives in `laboratorio/model.py`, `laboratorio/data.py`, and `laboratorio/train.py`. Course documentation is under `lecciones/`; `lecciones/00_indice.md` is its entry point.
- Quick source check: `python -m compileall -q laboratorio`. Running CLI commands requires PyTorch; there are no configured lint, type-check, or test commands.
