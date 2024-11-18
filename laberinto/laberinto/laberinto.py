import sys
from collections import deque

def leer_laberinto(archivo):
    laberinto = []
    with open(archivo, 'r') as f:
        for linea in f:
            laberinto.append(list(linea.strip()))
    return laberinto

def encontrar_inicio(laberinto):
    for y, fila in enumerate(laberinto):
        for x, valor in enumerate(fila):
            if valor == 'I':
                return (x, y)
    return None

def es_valido(laberinto, x, y, visitados):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    if 0 <= x < columnas and 0 <= y < filas:
        if laberinto[y][x] != '#' and (x, y) not in visitados:
            return True
    return False

def resolver_laberinto(laberinto):
    inicio = encontrar_inicio(laberinto)
    if not inicio:
        print("No se encontró el punto de inicio 'I' en el laberinto.")
        return False

    cola = deque()
    cola.append((inicio, [inicio]))
    visitados = set()

    while cola:
        (x, y), camino = cola.popleft()
        if laberinto[y][x] == 'F':
            return camino

        visitados.add((x, y))

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if es_valido(laberinto, nx, ny, visitados):
                cola.append(((nx, ny), camino + [(nx, ny)]))
    return None

def imprimir_laberinto(laberinto, camino=None):
    laberinto_copia = [fila[:] for fila in laberinto]
    if camino:
        for x, y in camino[1:-1]:
            laberinto_copia[y][x] = '*'
    for fila in laberinto_copia:
        print(''.join(fila))

def main():
    if len(sys.argv) != 2:
        print("Uso: python laberinto.py archivo_laberinto.txt")
        sys.exit(1)

    archivo_laberinto = sys.argv[1]
    laberinto = leer_laberinto(archivo_laberinto)
    camino = resolver_laberinto(laberinto)

    if camino:
        print("\n¡Se encontró una solución!\n")
        imprimir_laberinto(laberinto, camino)
    else:
        print("No se encontró solución para el laberinto.")

if __name__ == "__main__":
    main()
