# Lección 10 — Tensores, neuronas y PyTorch

## Objetivos

- Leer la forma de tensores.
- Comprender una neurona como transformación seguida de activación.
- Ejecutar operaciones básicas con PyTorch.

Un tensor generaliza escalares, vectores y matrices a varias dimensiones. Su `shape` describe tamaños: `[lote, longitud, canales]` puede describir varias secuencias con una representación por posición.

Una neurona calcula `y = φ(w·x + b)`: producto ponderado, sesgo `b` y función no lineal `φ`. Capas apilan transformaciones; activaciones como ReLU o GELU permiten representar relaciones no lineales.

```python
import torch

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(x.shape)                 # torch.Size([2, 2])
print(x @ x.T)                 # producto matricial
```

`nn.Linear(2, 3)` aprende una transformación de vectores de 2 entradas a 3 salidas. PyTorch calcula gradientes para tensores que tienen `requires_grad=True`; los módulos `nn.Module` agrupan parámetros y operaciones.

## Ejercicios

1. Crea tensores de formas `[4]`, `[2, 3]` y `[2, 5, 8]`; explica sus dimensiones.
2. Usa `torch.arange(6).reshape(2, 3)` y predice el resultado antes de imprimirlo.
3. Construye una `nn.Linear(2, 1)` y pásale un lote de 4 vectores de 2 componentes. ¿Qué forma tiene la salida?
4. Explica por qué la activación no lineal aumenta la capacidad expresiva de una red.

**Criterio para avanzar:** puedes leer `shape` y comprobar que una operación respeta las dimensiones.
