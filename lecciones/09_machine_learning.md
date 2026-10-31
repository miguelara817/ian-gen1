# Lección 9 — Aprender de ejemplos: ML y evaluación

## Objetivos

- Distinguir entrenamiento, validación y prueba.
- Comprender parámetros, hiperparámetros, pérdida y generalización.
- Identificar sobreajuste.

Machine learning consiste en ajustar un modelo a datos para que encuentre patrones útiles. Los parámetros se aprenden del entrenamiento; los hiperparámetros —por ejemplo, tamaño del modelo, tasa de aprendizaje y pasos— se eligen para dirigir el proceso.

Se reserva una parte de los datos para validación. Esa parte no actualiza los parámetros y permite estimar cómo responde el modelo a ejemplos no usados en el ajuste. Un conjunto de prueba se guarda para una evaluación final cuando hay decisiones repetidas basadas en validación.

La pérdida cuantifica el desacuerdo entre predicción y objetivo. En predicción categórica, la entropía cruzada penaliza asignar baja probabilidad al resultado correcto. Menor pérdida suele ser mejor bajo esa métrica, pero no demuestra comprensión ni garantiza utilidad.

Sobreajuste: el modelo mejora en entrenamiento pero empeora o deja de mejorar en validación. Puede estar memorizando peculiaridades. En un corpus diminuto, el problema puede aparecer rápido.

## Ejercicios

1. Explica para qué sirve cada partición: entrenamiento, validación y prueba.
2. Si entrenamiento mejora y validación empeora durante varias evaluaciones, ¿qué hipótesis investigarías?
3. Propón un experimento para comparar dos tamaños de modelo manteniendo lo demás constante.
4. ¿Por qué una sola muestra generada no basta para medir calidad?

**Criterio para avanzar:** diseñas una comparación controlada y puedes explicar una brecha de validación.
