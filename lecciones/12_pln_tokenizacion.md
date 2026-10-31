# Lección 12 — Texto, tokenización y predicción

## Objetivos

- Convertir texto en símbolos que un modelo pueda procesar.
- Entender vocabulario, codificación y contexto.
- Distinguir tokenización por caracteres de subpalabras.

Una red neuronal opera con números. Un tokenizador asigna a cada símbolo un entero: por ejemplo, `"a" → 5`. El vocabulario es el conjunto de tokens conocidos; codificar convierte texto a IDs y decodificar revierte la operación.

El laboratorio usa caracteres porque hace visible la representación y no requiere librería de tokenización. Eso produce secuencias largas y dificulta capturar unidades lingüísticas. Los modelos prácticos suelen usar subpalabras: fragmentos frecuentes que equilibran tamaño del vocabulario y longitud de secuencia.

Entrenamiento autoregresivo: cada posición ve un prefijo y el objetivo es el siguiente token. Para `"casa"`, los pares podrían ser `"c"→"a"`, `"ca"→"s"`, `"cas"→"a"`. En un lote, se desplazan las secuencias de entrada y objetivo una posición.

Revisa `CharDataset` y `get_batch` en `laboratorio/data.py`; observa cómo el corpus se codifica y cómo `y` es el desplazamiento de `x`.

## Ejercicios

1. Codifica mentalmente `"sol"` con un vocabulario `s=0, o=1, l=2`.
2. Para `x = [4, 5, 6]`, escribe los objetivos desplazados una posición.
3. ¿Qué sucede si aparece en generación un carácter no incluido durante el entrenamiento?
4. Compara ventajas y desventajas de tokenización de caracteres y subpalabras.

**Criterio para avanzar:** puedes explicar cómo se prepara un par de entrada y objetivo para predecir el siguiente token.
