# Laboratorio LLM: aprender construyendo

Un laboratorio incremental para estudiar machine learning, deep learning, PLN y búsqueda vectorial construyendo un modelo de lenguaje pequeño desde cero. La primera etapa entrena un modelo de caracteres con un Transformer causal escrito en PyTorch: no utiliza pesos preentrenados. Está pensado para aprender los fundamentos y ver resultados, no para competir con modelos grandes.

## Requisitos

- Python 3.10 o posterior.
- PyTorch instalado según tu sistema (CPU funciona; CUDA acelera el entrenamiento).

## Primer experimento

En PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m laboratorio train --steps 500 --run-id dia-01
```

En macOS/Linux, activa el entorno con `source .venv/bin/activate`.

El entrenamiento usa `data/corpus.txt`, divide los datos en entrenamiento y validación, y guarda:

- `artifacts/checkpoints/dia-01.pt`: pesos y configuración del modelo.
- `artifacts/experiments.jsonl`: métricas, fecha, configuración y muestra generada.

Genera texto desde un checkpoint:

```powershell
python -m laboratorio generate --checkpoint artifacts/checkpoints/dia-01.pt --prompt "La inteligencia"
```

Añade ejemplos propios a `data/corpus.txt` antes de la siguiente sesión. Mantén el mismo corpus para un experimento comparable o guarda una copia por fecha si quieres medir el efecto de los datos. El registro no cambia los pesos mágicamente: el modelo aprende cuando se ejecuta el entrenamiento. Cada `run-id` debe ser único para conservar checkpoints anteriores.

## Qué observar

- `train_loss` y `val_loss`: pérdida de predicción del siguiente carácter. En general, bajar es buena señal; una brecha creciente puede indicar sobreajuste.
- `sample`: generación cualitativa. Con pocos pasos suele ser incoherente; es parte del aprendizaje observar cómo cambia.
- Compara ejecuciones variando una cosa cada vez (datos, pasos, tamaño, tasa de aprendizaje) y anota una hipótesis antes de entrenar.

La primera versión utiliza un token por carácter para hacer visible el flujo. Los LLM actuales suelen usar tokenizadores subword, grandes corpus y muchos recursos. No incluyas datos personales o texto que no tengas derecho a usar.

## Ruta de aprendizaje

Consulta [ROADMAP.md](ROADMAP.md) para el mapa general y el curso guiado en [`lecciones/`](lecciones/00_indice.md). Las lecciones comienzan sin asumir experiencia previa y avanzan desde Python y matemáticas hasta implementar, entrenar y evaluar el Transformer de este laboratorio. Haz una por sesión: lee, ejecuta los ejemplos, resuelve los ejercicios y anota tus conclusiones antes de avanzar.
