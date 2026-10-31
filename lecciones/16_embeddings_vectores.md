# Lección 16 — Embeddings y bases de datos vectoriales

## Objetivos

- Distinguir embedding, índice vectorial y generador de texto.
- Interpretar similitud coseno y búsqueda de vecinos.
- Comprender el flujo general de RAG.

Un embedding de texto es un vector numérico producido para representar contenido. La similitud coseno compara la dirección de dos vectores: `cos(a,b) = (a·b)/(||a|| ||b||)`. Es cercana a 1 para direcciones parecidas, a 0 para ortogonales y a -1 para opuestas (si se permiten valores negativos).

Una base/índice vectorial almacena vectores y metadatos y permite recuperar vecinos por similitud. No es, por sí misma, un modelo generativo ni garantiza que el resultado sea verdadero. La calidad depende del modelo de embeddings, fragmentación, consulta y evaluación.

Flujo RAG simplificado: dividir documentos en fragmentos → calcular embeddings → indexar → incrustar la consulta → recuperar fragmentos → incorporarlos al contexto del generador → producir respuesta. Deben evaluarse recuperación y generación por separado.

El mini-LLM de este proyecto predice caracteres y no proporciona embeddings semánticos robustos. Esta lección establece los conceptos para una ampliación posterior con un modelo de embeddings y FAISS o Chroma; evita confundir sus representaciones internas con un índice de producción.

## Ejercicios

1. Calcula la similitud coseno para `[1,0]` y `[1,0]`, y para `[1,0]` y `[0,1]`.
2. ¿Qué diferencia hay entre recuperar el fragmento pertinente y redactar una respuesta?
3. Diseña tres consultas y una etiqueta de relevancia para evaluar recuperación.
4. Enumera dos formas en que RAG puede fallar aunque exista una base vectorial.

**Criterio para completar el curso:** puedes explicar el sistema desde datos hasta respuesta, incluyendo qué se aprende, qué se recupera, cómo se evalúa y qué límites observas.
