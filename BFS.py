import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

sys.setrecursionlimit(9999999)


def goaltest(arr):
    ataques = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                ataques += 2
            elif abs(i - j) == abs(arr[i] - arr[j]):
                ataques += 2
    return ataques==0

def expand(estadoActual):
    lista_nueva = []    
    for i in range(len(estadoActual)):
        nuevo_estado = estadoActual.copy()
        if estadoActual[i] < len(estadoActual)-1:
            nuevo_estado[i] += 1
            lista_nueva.append(nuevo_estado)
    return lista_nueva

def BFS(F, ax):
    estado_visitados = []  # Lista para almacenar todos los estados visitados

    def BFS_recursivo(F):
        if not F:
            print("Solución no encontrada")
            return None

        EA = F.pop(0)  # Sacar el primer estado en la lista
        print(EA)
        estado_visitados.append(EA)  # Guardar el estado visitado

        if goaltest(EA):  # Si el estado es un estado objetivo, terminar con solución
            print("Solución encontrada:", EA)
            dibujar_tablero(EA, ax)  # Dibujar el estado final del tablero
            plt.pause(10)  # Pausa para visualizar el estado final antes de terminar
            return EA
        else:  # Expandir el estado actual y agregar los nuevos estados a la lista F
            OS = expand(EA)
            F.extend(OS)

        dibujar_tablero(EA, ax)  # Dibujar el estado actual del tablero
        plt.pause(0.001)  # Pausa para visualizar el estado antes de avanzar

        return BFS_recursivo(F)  # Llamar recursivamente a la función con la nueva lista F

    return BFS_recursivo(F)

def dibujar_tablero(estado, ax):
    ax.clear()
    n = len(estado)
    ax.scatter(range(1, n + 1), estado, color='red', marker='o')
    ax.set_xlim(0, n + 1)
    ax.set_ylim(0, n + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(range(1, n + 1))
    ax.set_yticks(range(1, n + 1))
    ax.grid(True)
    ax.set_title('Posición de las reinas en el tablero')
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Filas')


estado_inicial = [[0,0,0,0]]  
limite=1000
fig, ax = plt.subplots()
BFS(estado_inicial, ax)
plt.show()