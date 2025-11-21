from collections import deque
# --------------------------------------------------------//
#  Función para guardar el inicio y el final del laberinto.
# --------------------------------------------------------//
def posiciones_iniciales_finales(grilla):
    for alto, fila in enumerate(grilla):
        for ancho, celda in enumerate(fila):
            if celda == '[P]':
                inicio = (alto, ancho)
            elif celda == '[M]':
                meta = (alto, ancho)
    return inicio, meta
# --------------------------------------------------------//
#  Función búsqueda en anchura para una grilla establecida.
# --------------------------------------------------------//
def bfs(grilla, inicio, meta):
    filas, columnas = len(grilla), len(grilla[0])
    visitado = set()
    cola = deque([(inicio, [inicio])]) # Desencolo la posición inicial
    while cola:
        (x, y), recorrido = cola.popleft()
        if (x, y) == meta:
            return recorrido
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # Direcciones posibles
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas and grilla[nuevo_x][nuevo_y] != '[#]' and (nuevo_x, nuevo_y) not in visitado:
                visitado.add((nuevo_x, nuevo_y))
                cola.append(((nuevo_x, nuevo_y), recorrido + [(nuevo_x, nuevo_y)]))
    return None