# Lección 15 — Generación, evaluación y experimentos

## Objetivos

- Comprender generación autoregresiva y temperatura.
- Evaluar con métricas y ejemplos cualitativos.
- Diseñar experimentos reproducibles.

Para generar, el modelo toma el contexto disponible, predice probabilidades del próximo token, muestrea uno y lo añade. Repite este ciclo. El límite de contexto restringe cuántos tokens previos entran en cada paso.

La pérdida de validación resume predicciones en datos no usados para actualizar pesos. Es útil para comparar experimentos con la misma preparación y evaluación, pero no mide gramática, factualidad ni utilidad por completo. Lee también muestras, revisa casos diversos y anota limitaciones.

Un experimento responsable documenta pregunta, hipótesis, corpus, semilla, configuración, cambios y resultados. Cambiar tasa de aprendizaje, datos y tamaño a la vez no permite atribuir el efecto a un factor.

## Ejercicios

1. Genera con temperaturas `0.4` y `1.2` desde el mismo checkpoint. Describe diversidad y coherencia sin declarar un ganador universal.
2. Diseña una comparación para `n_layer=2` frente a `n_layer=3`.
3. ¿Por qué se necesita un checkpoint para volver a generar sin repetir entrenamiento?
4. Propón una lista de casos cualitativos para revisar y una métrica cuantitativa que acompañe el análisis.

**Criterio para avanzar:** tu bitácora permite a otra persona repetir y entender una comparación.
