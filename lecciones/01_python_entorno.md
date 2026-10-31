# Lección 1 — Tu entorno y tu primer programa

## Objetivos

- Entender qué hacen Python y el intérprete.
- Ejecutar un archivo y distinguir código de su salida.
- Usar errores como información para depurar.

## Idea central

Un programa es una secuencia de instrucciones que el intérprete de Python ejecuta. El archivo contiene instrucciones; la terminal inicia el intérprete y muestra resultados.

Comprueba la instalación:

```powershell
python --version
```

Crea `hola.py` con este contenido:

```python
print("Hola, mundo")
print(2 + 3)
```

Ejecuta `python hola.py`. `print` muestra un valor. En la segunda línea, Python calcula primero la suma y luego muestra `5`.

Los entornos virtuales aíslan las dependencias de cada proyecto. Desde la carpeta del laboratorio:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En macOS/Linux la activación es `source .venv/bin/activate`. Para comprobar dónde está Python, usa `python -c "import sys; print(sys.executable)"`.

## Errores útiles

- `SyntaxError`: la forma del código no es válida; mira la línea indicada.
- `NameError`: intentaste usar un nombre que Python no conoce.
- `ModuleNotFoundError`: el paquete falta o estás usando otro entorno.

Lee el mensaje completo, localiza la primera línea de tu propio código y cambia una cosa a la vez.

## Ejercicios

1. Imprime tu nombre y una pregunta que tengas sobre inteligencia artificial.
2. Imprime el resultado de `17 * 23`.
3. Provoca un `NameError` escribiendo un nombre no definido y luego corrígelo.
4. Explica con tus palabras qué diferencia hay entre el archivo `hola.py` y el programa Python que lo ejecuta.

**Criterio para avanzar:** puedes ejecutar un archivo, localizarlo desde la terminal y explicar qué produce cada `print`.
