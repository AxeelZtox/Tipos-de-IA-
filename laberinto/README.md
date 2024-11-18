# Proyecto: Resolución de Laberintos con Python

Este proyecto implementa un programa en Python que resuelve laberintos representados en archivos de texto utilizando el algoritmo **BFS (Breadth-First Search)**. El objetivo principal es encontrar el camino más corto desde un punto inicial (`I`) hasta un punto final (`F`) dentro del laberinto.

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Uso](#uso)
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
