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


