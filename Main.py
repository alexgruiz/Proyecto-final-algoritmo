from Data_manager import *
from Utils import *

def menu_principal():
    # Muestra el menú principal del sistema
    print("\nCatálogo MetroArt: ")
    print("1. Buscar obras por departamento")
    print("2. Buscar obras por nacionalidad del autor")
    print("3. Buscar obras por nombre del autor")
    print("4. Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))
        return opcion
    except ValueError:
        print("Por favor ingrese un número válido.")
        return menu_principal()

def mostrar_obras(obras):
    # Muestra una lista de obras encontradas por departamento
    if not obras:
        print("No se encontraron obras con esos criterios.")
        return

    print("\nObras encontradas:")
    for obra in obras:
        print(obra)

def mostrar_detalle_obra(obra):
    # Muestra los detalles completos de una obra seleccionada
    if not obra:
        print("No se encontró la obra solicitada.")
        return
