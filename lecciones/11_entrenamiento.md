# Lección 11 — Entrenamiento: pérdida y gradiente

## Objetivos

- Comprender el ciclo de entrenamiento de PyTorch.
- Saber qué hacen `backward`, `step` y `zero_grad`.
- Reconocer el papel de lotes y semilla.

El ciclo esencial es: formar un lote, predecir, calcular pérdida, calcular gradientes y actualizar parámetros. En PyTorch:

```python
prediccion = modelo(entrada)
loss = funcion_de_perdida(prediccion, objetivo)
optimizador.zero_grad(set_to_none=True)
loss.backward()
optimizador.step()
```

`backward()` calcula derivadas; `step()` aplica la regla del optimizador; `zero_grad()` limpia los gradientes acumulados de la iteración anterior. Un lote es una muestra de ejemplos procesados juntos. Una época recorre el conjunto de entrenamiento, aunque en aprendizaje por lotes aleatorios no siempre coincide con el bucle usado.

Fijar una semilla mejora la reproducibilidad, pero no garantiza resultados idénticos entre hardware, versiones y algoritmos. Evaluar requiere `model.eval()` y desactivar gradientes; dropout y otros módulos se comportan de manera distinta en evaluación.

## Ejercicios

1. Ordena las cinco operaciones del ciclo y explica por qué no se actualiza antes de `backward()`.
2. ¿Qué riesgo hay en olvidar `zero_grad()` en el ciclo típico?
3. Busca en `laboratorio/train.py` dónde se elige dispositivo CPU/CUDA y dónde se mide validación.
4. Explica por qué se usan lotes en vez de calcular siempre sobre todos los ejemplos.

**Criterio para avanzar:** puedes recorrer el bucle de entrenamiento y decir qué estado cambia en cada línea.
