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

estado_inicial = [[2,0,3,0]]  
limite=1000
plt.show()

def IDFS(F, nivel, limite, ax):
    if not F:
        print("Solución no encontrada")
        return None
    else:
        EA = F.pop(0)
        print(EA)
        dibujar_tablero(EA, ax)  # Dibujar el estado actual del tablero
        plt.pause(0.001)  # Pausa para visualizar el estado antes de avanzar

        if goaltest(EA):
            print("Solución encontrada:", EA)
            dibujar_tablero(EA, ax)  # Dibujar el estado final del tablero
            plt.pause(10)  # Pausa para visualizar el estado final antes de terminar
            return EA
        else:
            if nivel < limite - 1:
                OS = expand(EA)
                for estado in reversed(OS):  # Iterar sobre OS en orden inverso para agregar al principio
                    F.insert(0, estado)
            else:
                print("Se llegó al límite, no hay solución ", limite)
                return False

            return IDFS(F, nivel, limite, ax)


# Llamar a la función IDFS con gráficos
fig, ax = plt.subplots()
while True:
    solucion = IDFS(estado_inicial, nivel=0, limite=limite, ax=ax)
    if solucion:
        break
    F = [[0, 0, 0, 0]]  # Reiniciar F
    limite = 10000  # Reiniciar límite


