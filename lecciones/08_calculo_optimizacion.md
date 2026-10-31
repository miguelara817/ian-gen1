# Lección 8 — Derivadas y optimización

## Objetivos

- Interpretar una derivada como tasa de cambio local.
- Entender descenso por gradiente a nivel conceptual.
- Relacionar pérdida con ajuste de parámetros.

Para una función `L(w)`, la derivada `dL/dw` indica cuánto cambia `L` cuando cambia ligeramente `w`. Si la derivada es positiva, reducir `w` un poco suele reducir la pérdida; si es negativa, aumentarlo suele reducirla.

El descenso por gradiente actualiza parámetros así: `w_nuevo = w_actual - η · dL/dw`. `η` (tasa de aprendizaje) determina el tamaño del paso. Pasos enormes pueden saltar la zona útil; pasos diminutos avanzan lentamente.

Con muchos parámetros, las derivadas parciales forman el gradiente. La regla de la cadena permite propagar cómo cada parámetro afecta a la pérdida a través de operaciones encadenadas: es la base de backpropagation.

Ejemplo: `L(w) = (w - 3)²`. Su derivada es `2(w-3)`. En `w=0`, la derivada es `-6`, así que un paso de gradiente positivo mueve `w` hacia valores mayores, acercándolo al mínimo 3.

## Ejercicios

1. Calcula la derivada de `(w-3)²` para `w=0` y `w=4`.
2. Aplica una actualización desde `w=0` con `η=0.1`.
3. ¿Qué podría ocurrir si `η=10` para este ejemplo?
4. Explica por qué el gradiente ofrece información para mejorar la predicción, aunque no garantiza que cualquier configuración encuentre el mejor resultado global.

**Criterio para avanzar:** puedes hacer una actualización numérica y describir qué representa la tasa de aprendizaje.
