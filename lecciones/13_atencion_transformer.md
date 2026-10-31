# Lección 13 — Atención y Transformer causal

## Objetivos

- Entender embeddings posicionales y atención como mezcla contextual.
- Comprender la máscara causal.
- Identificar componentes del bloque Transformer del proyecto.

Un embedding transforma cada ID en un vector. Como las posiciones importan, se combina con una representación posicional. La atención permite que una posición pondere información de otras posiciones del contexto.

En atención, cada vector genera consulta `Q`, clave `K` y valor `V`. Se calculan compatibilidades `QKᵀ`, se escalan, se normalizan con softmax y se usan para mezclar `V`: `Attention(Q,K,V)=softmax(QKᵀ/√dₖ)V`. Las múltiples cabezas aprenden relaciones diferentes en paralelo.

Un modelo causal no debe ver tokens futuros al predecir el pasado. La máscara causal impide que la posición `t` atienda a posiciones `>t`. Sin máscara, el modelo podría copiar la respuesta durante entrenamiento en vez de aprender predicción real.

El bloque del proyecto combina normalización, atención, conexión residual y una red MLP. Las conexiones residuales suman la entrada a la transformación y facilitan el flujo de información y gradiente.

Lee `CausalSelfAttention`, `Block` y `TinyGPT` en `laboratorio/model.py`. Sigue las dimensiones: `[lote, tiempo, embedding]`.

## Ejercicios

1. En una secuencia de 4 posiciones, dibuja qué posiciones puede consultar cada una bajo máscara causal.
2. Si `QKᵀ` tiene forma `[tiempo, tiempo]`, ¿qué relación representa cada celda?
3. ¿Por qué se divide por `√dₖ` antes del softmax?
4. Explica la función de embedding posicional, atención, MLP y conexión residual en una frase cada uno.

**Criterio para avanzar:** puedes explicar por qué existe la máscara y describir el flujo de información de un bloque.
