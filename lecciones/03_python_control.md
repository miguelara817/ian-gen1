# Lección 3 — Decisiones, bucles y funciones

## Objetivos

- Expresar condiciones y repetir tareas.
- Descomponer un programa con funciones.
- Comprender argumentos y valores devueltos.

```python
perdida = 1.25
if perdida < 1.0:
    print("La pérdida es menor que uno")
else:
    print("Hay margen para seguir aprendiendo")
```

La indentación define los bloques. `for` recorre una secuencia; `range(3)` genera 0, 1 y 2:

```python
for dia in range(1, 4):
    print(f"Sesión {dia}")
```

Una función nombra una tarea reutilizable. `return` entrega un resultado; `print` solo lo muestra:

```python
def error_absoluto(prediccion, objetivo):
    return abs(prediccion - objetivo)

error = error_absoluto(0.7, 1.0)
print(error)
```

Los parámetros son nombres locales que reciben argumentos. Si una operación debe ser reutilizada o comprobada, suele convenir que devuelva un resultado en vez de imprimirlo.

## Ejercicios

1. Escribe una función `es_par(n)` que devuelva `True` si `n` es divisible entre 2.
2. Usa un bucle para mostrar los cuadrados de los números del 1 al 5.
3. Escribe `promedio(a, b, c)` que devuelva la media.
4. Modifica la función de error para devolver también `"sobreestima"` o `"subestima"` según la predicción frente al objetivo.

**Criterio para avanzar:** una función tuya recibe argumentos, calcula y devuelve el resultado esperado en varios casos.
