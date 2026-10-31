# Lección 2 — Variables, tipos y expresiones

## Objetivos

- Guardar valores con nombres y descubrir sus tipos.
- Diferenciar números, texto y valores lógicos.
- Convertir datos con intención.

Una variable es un nombre que referencia un valor:

```python
nombre = "Ada"
edad = 36
altura = 1.65
es_estudiante = True
print(type(nombre), type(edad), type(altura), type(es_estudiante))
```

Tipos básicos: `int` (entero), `float` (decimal), `str` (texto) y `bool` (`True`/`False`). `=` asigna; `==` compara.

```python
tokens = 128
caracteres = 42
proporcion = caracteres / tokens
print(f"Proporción: {proporcion:.2f}")
```

Una f-string inserta expresiones dentro de texto. La división `/` produce un decimal; `//` es división entera y `%` da el resto.

No se puede sumar directamente texto y entero: `"edad: " + 36` produce un error de tipo. Usa `f"edad: {36}"` o convierte de forma explícita con `str(36)`. `int("12")` convierte texto numérico; `int("doce")` falla porque no existe una conversión válida.

## Ejercicios

1. Define `tokens = 256` y `vocabulario = 64`; calcula qué fracción del vocabulario representan los tokens.
2. Imprime un resumen con una f-string que incluya tu nombre y un concepto que quieras estudiar.
3. Predice el tipo de `3 / 2`, `3 // 2` y `3 == 2`, después compruébalo con `type`.
4. ¿Por qué convertir `"3.14"` con `int` no preserva el valor decimal?

**Criterio para avanzar:** distingues asignación de comparación y puedes explicar el tipo de los valores del ejercicio.
