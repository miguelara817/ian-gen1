# Lección 5 — Álgebra, funciones y notación

## Objetivos

- Leer expresiones con variables.
- Interpretar función, entrada y salida.
- Usar notación matemática para describir predicciones.

Una variable matemática representa un número que puede cambiar. En `y = 2x + 1`, la función recibe `x`, multiplica por dos y suma uno. Si `x=3`, entonces `y=7`. En Python:

```python
def f(x):
    return 2 * x + 1
```

Una función de modelo suele escribirse `f_θ(x)`: `x` es la entrada, `θ` representa los parámetros aprendidos y `f_θ(x)` es la predicción. Entrenar significa ajustar `θ` para que las predicciones se acerquen a objetivos.

La notación de suma `Σ` compacta repeticiones. El promedio de errores `e₁, ..., eₙ` es `L = (1/n) Σᵢ eᵢ`. En código: `sum(errores) / len(errores)`.

Una igualdad matemática afirma que dos expresiones tienen el mismo valor; una asignación de Python guarda un valor en un nombre. No confundir ambos contextos ayuda a pasar una fórmula a código.

## Ejercicios

1. Calcula `f(x)=3x-2` para `x=0, 1, 4`.
2. Escribe una función Python que calcule esa regla.
3. Los errores son `[1, 2, 3, 4]`. Calcula su media a mano y con Python.
4. En `f_θ(x)`, explica qué significan entrada, parámetros y salida en un clasificador.

**Criterio para avanzar:** puedes traducir una fórmula sencilla a una función Python y comprobar un caso manualmente.
