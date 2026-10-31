# Lección 4 — Colecciones, archivos y datos

## Objetivos

- Elegir una colección adecuada para cada dato.
- Leer texto de un archivo de manera reproducible.
- Comprender por qué preparar datos es parte del trabajo de ML.

Una `list` conserva elementos en orden y permite repetidos; una `set` conserva elementos únicos; un `dict` asocia claves con valores.

```python
frases = ["hola", "modelo", "hola"]
vocabulario = set(frases)
frecuencias = {"hola": 2, "modelo": 1}
print(len(frases), len(vocabulario), frecuencias["hola"])
```

Leer un archivo UTF-8:

```python
from pathlib import Path

texto = Path("data/corpus.txt").read_text(encoding="utf-8")
lineas = texto.splitlines()
print(f"{len(lineas)} líneas, {len(texto)} caracteres")
```

El texto del corpus es una observación, no una instrucción de Python. Antes de entrenar pregunta: ¿de dónde procede?, ¿tengo permiso?, ¿está vacío?, ¿qué separación entre entrenamiento y validación tiene sentido? El laboratorio separa secuencialmente para conservar el orden del texto, un método didáctico que no siempre es ideal para cualquier conjunto de datos.

## Ejercicios

1. Cuenta las líneas y los caracteres de `data/corpus.txt`.
2. Construye un conjunto con los caracteres del corpus y cuenta su tamaño.
3. Crea un diccionario con el número de caracteres de cada línea.
4. Explica por qué una lista y un conjunto producen longitudes distintas si hay elementos repetidos.

**Criterio para avanzar:** puedes leer el corpus desde el proyecto y describir qué representa cada colección.
