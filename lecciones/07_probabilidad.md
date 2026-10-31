# Lección 7 — Probabilidad y distribuciones

## Objetivos

- Interpretar probabilidades como pesos de resultados posibles.
- Comprender una distribución categórica y el muestreo.
- Entender qué aprende un modelo de lenguaje al predecir el siguiente token.

Una distribución sobre `k` categorías asigna probabilidades no negativas que suman 1. Para tres letras, `[0.1, 0.7, 0.2]` significa que la segunda es la más probable, pero las otras aún pueden aparecer.

El modelo produce puntuaciones llamadas logits. `softmax` las convierte en probabilidades:

`pᵢ = exp(zᵢ) / Σⱼ exp(zⱼ)`.

Al muestrear una categoría, el resultado es aleatorio según esos pesos. Elegir siempre el máximo se llama decodificación codiciosa. La temperatura ajusta la concentración: dividir logits por un valor bajo hace la distribución más concentrada; un valor alto la suaviza.

La probabilidad de una secuencia puede descomponerse como producto de probabilidades condicionales del siguiente token. El modelo autoregresivo aprovecha esta regla: predice paso a paso condicionado al contexto previo.

## Ejercicios

1. ¿Puede una distribución tener probabilidades `[0.2, 0.2, 0.2]`? Justifica.
2. Si un token tiene probabilidad `0.8`, ¿es imposible que salga uno con `0.2`?
3. Para la secuencia «sol», escribe qué contexto usarías para predecir cada carácter en un modelo de caracteres.
4. Describe el efecto esperado de temperatura muy baja y muy alta, sin afirmar que la salida sea siempre idéntica.

**Criterio para avanzar:** puedes explicar la diferencia entre la puntuación del modelo, una probabilidad y una muestra.
