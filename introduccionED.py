class Persona:
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = int(edad)
        self.estatura = float(estatura)

personas = []
#CARGAR LOS DATOS DEL ARCHIVO
def cargar_datos():
    with open('c:\Programas Python\Introduccion-IA\dataset.txt', 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            personas.append(Persona(data[0], data[1], data[2]))
#MOSTRAR DATO
def mostrar_personas():
    for persona in personas:
        print(f"{persona.nombre}, {persona.edad}, {persona.estatura}")
        
#ORDENAR NOMBRE
def ordenar_por_nombre():
    global personas
    personas = sorted(personas, key=lambda x: x.nombre)
    print()
    mostrar_personas()
    
#ORDENAR POR EDAD
def ordenar_por_edad():
    global personas
    personas = sorted(personas, key=lambda x: x.edad)
    print()
    mostrar_personas()

#ORDENAR ESTATURA
def ordenar_por_estatura():
    global personas
    personas = sorted(personas, key=lambda x: x.estatura)
    print()
    mostrar_personas()
    
def eliminar_por_nombre():
    global personas
    nombre_a_eliminar = input("Ingrese el nombre de la persona que desea eliminar: ")
    indice_eliminado = None
    for i, persona in enumerate(personas):
        if persona.nombre == nombre_a_eliminar:
            indice_eliminado = i
            break
    if indice_eliminado is not None:
        personas.pop(indice_eliminado)
        print("Persona eliminada correctamente.")
    else:
        print("No se encontró a ninguna persona con ese nombre.")
    print()
    mostrar_personas()
    return indice_eliminado

def insertar_dato():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    estatura = input("Ingrese la estatura: ")
    indice_eliminado = eliminar_por_nombre()
    if indice_eliminado is not None:
        personas.insert(indice_eliminado, Persona(nombre, edad, estatura))
        print("Persona insertada correctamente.")
    else:
        personas.append(Persona(nombre, edad, estatura))
        print("Persona añadida correctamente.")
    print()
    mostrar_personas()

cargar_datos()
while True:   
    print()
    print("Introduccion a la estructura de datos:")
    print("1. Ordenar por nombre")
    print("2. Ordenar por edad")
    print("3. Ordenar por estatura")
    print("4. Insertar dato")
    print("5. Eliminar dato")
    print("6. Salir")
    
    op=input("ingresa el numero para la opcion que quiera realizar: ")    
    if op == '1':
        ordenar_por_nombre()
    elif op == '2':
        ordenar_por_edad()
    elif op == '3':
        ordenar_por_estatura()
    elif op == '4':
        insertar_dato()
    elif op == '5':
        eliminar_por_nombre()
    elif op == '6':
        break
    else:
        print("dato no valido!")
        print()