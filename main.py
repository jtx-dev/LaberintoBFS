import math
from laberinto import *
from busqueda import posiciones_iniciales_finales, bfs
import time

# -------------------------------------------------------//
#                         Menú
# -------------------------------------------------------//
while True:
    #-----------------------------------------------------||
    #         Validación de entrada alto y ancho
    #-----------------------------------------------------||
    print("Ingrese el alto y el ancho (mayores que 1):")
    try:
        n, m = map(int, input().split())
        if n > 1 and m > 1:
            break
        else:
            print("Ambos valores deben ser mayores que 1. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Ingrese dos números enteros.")

# -------------------------------------------------------//
#      Generar laberinto y ejecutar búsqueda
# -------------------------------------------------------//
grilla = generar_laberinto(m, n)
print("|----------------------------------------|")
print("Mostrando laberinto generado aleatoriamente:")

time.sleep(1) #comentar en caso de querer rapidez de ejecución

imprimir_laberinto(grilla)

inicio, meta = posiciones_iniciales_finales(grilla)
camino = bfs(grilla, inicio, meta)

print("buscando el camino más corto...")

time.sleep(1) #comentar en caso de querer rapidez de ejecución

if camino:
    print("|----------------------------------------|")
    print("Camino más corto encontrado:")
    for i in camino:
        print(f'->{i}\n', end=" ")


    time.sleep(1) #comentar en caso de querer rapidez de ejecución
    
    print("|----------------------------------------|")
    print("Mostrando camino en el laberinto:")
    imprimir_laberinto_con_camino(grilla, camino[1:-1])  # Excluye inicio y meta al momento de imprimir el laberinto
else:
    print("|----------------------------------------|")
    print("No hay camino disponible \033[91m:(\033[0m")
