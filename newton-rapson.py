import numpy as np
import matplotlib.pyplot as plt

punto_incio = float(input("Introduce el punto de inicio: "))
max_iteraciones = int(input("Introduce el máximo de iteraciones: "))
tolerancia = float(input("Introduce el valor aproximado al error: "))

def funcion(x):
    return x**3 - 2*x**2 + 2

def derivada_funcion(x):
    return 3*x**2 - 4*x

def newton_raphson(func, dxfunc, x0, tole, max_iteracion):
    x = x0
    iteraciones = 0
    while abs(func(x)) > tole and iteraciones < max_iteracion:
        x = x - func(x) / dxfunc(x)
        iteraciones += 1
    if iteraciones == max_iteracion:
        print("El método no converge después de {} iteraciones".format(max_iteracion))
    else:
        print("La raíz aproximada es:", x)
    return x

resultado = newton_raphson(funcion, derivada_funcion, punto_incio, tole=tolerancia, max_iteracion=max_iteraciones)

# Graficar la función y la raíz aproximada
x_values = np.linspace(-0.5, 2.5, 1000)
y_values = funcion(x_values)

plt.plot(x_values, y_values, label='f(x)')
plt.scatter(resultado, funcion(resultado), color='red', label='Raíz aproximada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Metodo de Newton')
plt.legend()
plt.grid(True)
plt.show()
