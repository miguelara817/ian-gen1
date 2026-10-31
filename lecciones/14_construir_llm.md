# Lección 14 — Construir y entrenar nuestro mini-LLM

## Objetivos

- Conectar preparación de texto, arquitectura y optimización.
- Ejecutar un entrenamiento desde cero y localizar artefactos.
- Entender qué significa «desde cero» en este laboratorio.

Aquí construimos un modelo de lenguaje neuronal pequeño con Transformer causal. Se inicializan pesos aleatorios; no se descargan pesos preentrenados. Aprende a predecir el siguiente carácter del corpus. No es un sistema de propósito general: su escala y datos son para enseñanza.

Desde la raíz del proyecto, prepara el entorno como indica `README.md` y ejecuta:

```powershell
python -m laboratorio train --steps 500 --run-id leccion-14
```

El programa prepara los datos, elige CPU o CUDA, crea el modelo, actualiza pesos y calcula pérdidas y muestra. Inspecciona `artifacts/experiments.jsonl` y `artifacts/checkpoints/`. No reutilices el mismo `run-id`: cada nombre identifica una ejecución.

Para generar:

```powershell
python -m laboratorio generate --checkpoint artifacts/checkpoints/leccion-14.pt --prompt "La inteligencia"
```

Si la muestra parece ruido, es esperable con corpus pequeño y pocas iteraciones. Añade datos apropiados, cambia un factor y compara; no esperes aprendizaje autónomo diario. La evolución ocurre cuando ejecutas entrenamiento y registras las decisiones.

## Experimentos

1. Ejecuta dos veces con distinto `run-id` y misma configuración. ¿Qué tan parecidas son las pérdidas y muestras? Considera aleatoriedad.
2. Añade algunas frases al corpus y repite con un nuevo ID. Mantén constantes los demás factores.
3. Aumenta los pasos, sin tocar datos ni arquitectura. Compara train y validación.
4. Escribe una conclusión prudente: separa observación de explicación.

**Criterio para avanzar:** puedes explicar el trayecto desde caracteres hasta logits, pérdida, actualización y checkpoint.
