# Ruta progresiva

Avanza a tu ritmo. Para mantener una evolución visible, al final de cada sesión registra: fecha, qué esperabas, qué cambiaste, métricas, muestra y qué aprendiste. Cambia una variable a la vez.

## Etapa 1 — Fundamentos y datos (semana 1)

1. Recorre `laboratorio/data.py` y comprende entrenamiento frente a validación.
2. Cambia el corpus por textos pequeños y con permiso de uso. Mira el vocabulario de caracteres.
3. Ejecuta 100 y 500 pasos con la misma configuración. Compara pérdidas y muestras.
4. Aprende tensores, dimensiones, lotes, semilla aleatoria y descenso de gradiente.

**Meta:** explicar qué predice el modelo y por qué se separan los datos.

## Etapa 2 — Machine learning y evaluación (semana 2)

1. Compara corpus pequeños y grandes sin modificar otros parámetros.
2. Observa sobreajuste comparando pérdida de entrenamiento y validación.
3. Prueba tasa de aprendizaje y tamaño de lote en ejecuciones separadas.
4. Añade una tabla manual al diario con hipótesis y resultados.

**Meta:** interpretar una curva de aprendizaje y realizar experimentos controlados.

## Etapa 3 — Deep learning y Transformer (semanas 3–4)

1. Sigue `laboratorio/model.py`: embedding, atención causal, conexiones residuales y MLP.
2. Dibuja las formas de tensores en una pasada hacia adelante.
3. Cambia `n_embd`, `n_head` o `n_layer`, de uno en uno; vigila tiempo y validación.
4. Estudia softmax, entropía cruzada, backpropagation y máscara causal.

**Meta:** describir cómo cada token usa el contexto anterior para predecir el siguiente.

## Etapa 4 — PLN y tokenización (semana 5)

1. Contrasta tokenización por carácter con palabras/subpalabras.
2. Examina cómo puntuación, acentos y limpieza cambian el vocabulario.
3. Estudia generación autoregresiva, temperatura y límites de evaluación.

**Meta:** reconocer que la calidad depende tanto de datos y tokenización como de arquitectura.

## Etapa 5 — Embeddings y búsqueda vectorial (semana 6)

1. Aprende similitud coseno y representa fragmentos de texto con un modelo de embeddings.
2. Construye un índice local con FAISS o Chroma y consulta por vecinos semánticos.
3. Compara búsqueda por palabras clave con búsqueda vectorial; mide relevancia en consultas preparadas.
4. Explora RAG: recuperar fragmentos y pasarlos como contexto a un generador.

**Meta:** distinguir una base vectorial (índice de vectores) de un modelo generativo.

## Etapa 6 — Proyecto y reproducibilidad

Elige un corpus acotado y permitido, define una pregunta de evaluación, registra configuraciones y resultados, y escribe qué limitaciones encontraste. Al compartir el proyecto, incluye instrucciones para reproducirlo y no publiques datos sensibles.

## Plantilla de bitácora

```text
Fecha / run-id:
Pregunta e hipótesis:
Único cambio respecto a la sesión anterior:
Corpus y procedencia:
Pasos / configuración:
train_loss / val_loss:
Muestra generada:
Conclusión y próxima pregunta:
```
