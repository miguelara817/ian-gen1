# Lección 6 — Vectores y matrices

## Objetivos

- Interpretar un vector como una lista ordenada de números.
- Calcular producto punto y reconocer dimensiones.
- Conectar álgebra lineal con embeddings y capas neuronales.

Un vector de `d` componentes es un punto o una representación en un espacio `d`-dimensional. Por ejemplo, `[0.2, -0.1, 0.7]` tiene dimensión 3. Un embedding de palabra o token es un vector aprendido que representa ese símbolo.

Para vectores `a` y `b` del mismo tamaño, el producto punto es `a·b = Σᵢ aᵢbᵢ`. Para `[1,2]` y `[3,4]`, vale `1·3 + 2·4 = 11`.

```python
a = [1, 2]
b = [3, 4]
producto = sum(x * y for x, y in zip(a, b))
```

Una matriz es una tabla rectangular. Si `x` tiene `d` componentes y `W` tiene `m` filas y `d` columnas, `Wx` produce un vector de `m` componentes. Las dimensiones deben coincidir: entender la forma evita muchos errores de tensores.

## Ejercicios

1. Calcula a mano el producto punto de `[2, -1, 3]` y `[4, 2, 0]`.
2. Implementa una función general de producto punto; ¿qué debe ocurrir si las longitudes difieren?
3. Si una capa transforma vectores de 8 números a 5, ¿qué forma tiene su matriz de pesos?
4. Explica por qué un vocabulario de 100 símbolos y embeddings de 32 componentes requiere 100 vectores de longitud 32.

**Criterio para avanzar:** puedes comprobar formas de matrices y calcular un producto punto.
