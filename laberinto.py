import random
# --------------------------------------------------------//
#     Función para generar laberinto aleatoriamente.
# --------------------------------------------------------//
def generar_laberinto(ancho, alto):
    # Crear una grilla de celdas
    n = int((alto*ancho)*0.3) # numero de obstaculos
    while True:
        px = random.randint(0, ancho-1) # posicion del jugador en x
        py = random.randint(0, alto-1) # posicion del jugador en y
        mx = random.randint(0, ancho-1) # posicion de la meta en x
        my = random.randint(0, alto-1) # posicion de la meta en y
        if (px, py) != (mx, my): #Validación sobreescritura de posiciones
            break
    grilla = [['[ ]' for _ in range(ancho)] for _ in range(alto)]
    grilla[py][px] = '[P]'
    grilla[my][mx] = '[M]'
    # Generar obstáculos en posiciones libres.
    pos_libres = [(y,x) for x in range(ancho) for y in range(alto)
                if(y,x) not in [(py, px), (my, mx)]] #Validación sobreescritura de posiciones
    random.shuffle(pos_libres) # Mezclo los elementos recibidos
    for y,x in pos_libres[:n]:
        grilla[y][x] = '[#]'
    return grilla
# --------------------------------------------------------//
# Función para imprimir el laberinto con sus respectivos índices
# --------------------------------------------------------//
def imprimir_laberinto(grilla):
    # colores 
    RESET = "\033[0m"
    COLOR_P = "\033[92m"   # Verde jugador
    COLOR_M = "\033[35m"   # morado meta
    COLOR_OBS = "\033[94m" # Azul obstáculos
    COLOR_VACIO = "\033[97m" # Blanco vacío

    # Imprimir columnas
    print("   ", end="")
    for col in range(len(grilla[0])):
        print(f"{col:2d} ", end="")
    print()
    # Imprimir filas
    for idx, fila in enumerate(grilla):
        print(f"{idx:2d} ", end="")
        for celda in fila:
            if celda == '[P]':
                print(f"{COLOR_P}{celda}{RESET}", end="")
            elif celda == '[M]':
                print(f"{COLOR_M}{celda}{RESET}", end="")
            elif celda == '[#]':
                print(f"{COLOR_OBS}{celda}{RESET}", end="")
            else:
                print(f"{COLOR_VACIO}{celda}{RESET}", end="")
        print()
def imprimir_laberinto_con_camino(grilla, camino):
    RESET = "\033[0m"
    COLOR_P = "\033[92m"   # Verde jugador
    COLOR_M = "\033[35m"   # Morado meta
    COLOR_OBS = "\033[94m" # Azul obstáculos
    COLOR_VACIO = "\033[97m" # Blanco vacío
    COLOR_CAMINO = "\033[102m\033[30m" # Fondo verde claro, texto negro

    camino_set = set(camino)
    print("   ", end="")

    for col in range(len(grilla[0])):
        print(f"{col:2d} ", end="")
    print()

    for idx, fila in enumerate(grilla):
        print(f"{idx:2d} ", end="")
        for jdx, celda in enumerate(fila):
            if celda == '[P]':
                print(f"{COLOR_P}{celda}{RESET}", end="")
            elif celda == '[M]':
                print(f"{COLOR_M}{celda}{RESET}", end="")
            elif celda == '[#]':
                print(f"{COLOR_OBS}{celda}{RESET}", end="")
            elif (idx, jdx) in camino_set:
                print(f"{COLOR_CAMINO}[·]{RESET}", end="")
            else:
                print(f"{COLOR_VACIO}{celda}{RESET}", end="")

        print() 
