# Proyecto: Resolución de Laberintos con Python

Este proyecto implementa un programa en Python que resuelve laberintos representados en archivos de texto utilizando el algoritmo **BFS (Breadth-First Search)**. El objetivo principal es encontrar el camino más corto desde un punto inicial (`I`) hasta un punto final (`F`) dentro del laberinto.

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Uso](#uso)
- [Formato del Laberinto](#formato-del-laberinto)
- [Cómo Funciona](#cómo-funciona)
- [Ejemplo de Ejecución](#ejemplo-de-ejecución)
- [Notas Adicionales](#notas-adicionales)
- [Licencia](#licencia)

---

## Características

- Resuelve laberintos automáticamente usando **búsqueda por amplitud (BFS)**.
- Encuentra el camino más corto desde el punto de inicio (`I`) hasta el final (`F`).
- Muestra gráficamente el laberinto con el camino resuelto.
- Maneja errores como:
  - Puntos de inicio o fin inexistentes.
  - Laberintos sin solución.

---

## Requisitos

- **Python 3.7** o superior.
- No requiere librerías externas; utiliza únicamente bibliotecas estándar de Python.

---

## Uso

1. Clona el repositorio o descarga los archivos necesarios.
2. Asegúrate de tener un archivo de texto que contenga el laberinto (ver formato más abajo).
3. Ejecuta el programa desde la línea de comandos:
   ```bash
   python laberinto.py archivo_laberinto.txt
Formato del Laberinto
El archivo del laberinto debe cumplir con las siguientes reglas:

I: Representa el punto de inicio.
F: Representa el punto final.
#: Son las paredes que no se pueden atravesar.
Espacios en blanco ( ): Representan caminos transitables.
Ejemplo de Archivo (laberinto.txt)
plaintext
Copy code
########
#I     #
### ## #
#      #
# ####F#
########
Cómo Funciona
Lectura del Laberinto: El programa lee el archivo y lo convierte en una matriz de caracteres.
Identificación del Inicio: Busca la posición del punto de inicio (I) dentro del laberinto.
Resolución con BFS:
Explora todas las celdas accesibles comenzando desde I.
Encuentra el camino más corto hasta F.
Visualización del Resultado: Imprime el laberinto con el camino encontrado marcado con *.
Algoritmo Utilizado: BFS (Breadth-First Search)
El BFS asegura que el primer camino encontrado hacia el punto final (F) sea el más corto en términos de pasos.

Ejemplo de Ejecución
Entrada: laberinto.txt
plaintext
Copy code
########
#I     #
# ###  #
#    F #
########
Comando
bash
Copy code
python laberinto.py laberinto.txt
Salida
plaintext
Copy code
########
#I*****#
#*###  #
#****F #
########
Notas Adicionales
Si el laberinto no tiene solución, el programa mostrará un mensaje indicando que no se encontró un camino.
Si no se encuentra el punto de inicio (I) o el punto final (F), el programa también arrojará un error amigable.
