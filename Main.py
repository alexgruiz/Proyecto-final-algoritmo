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
  
    print("\nDetalles de la obra: ")
    print(f"Título: {obra.titulo}")
    print(f"Artista: {obra.artista.nombre}")
    print(f"Nacionalidad: {obra.artista.nacionalidad}")
    print(f"Fechas del artista: {obra.artista.fecha_nacimiento} - {obra.artista.fecha_muerte}")
    print(f"Tipo: {obra.tipo}")
    print(f"Año de creación: {obra.fecha_creacion}")
    
    if obra.imagen_url:
        print("\n¿Desea ver la imagen de la obra? (s/n)")
        if input().lower() == 's': # Si el usuario desea ver la imagen, se muestra
            mostrar_imagen(obra.imagen_url)

def main():
    # Cargar datos iniciales
    departamentos = obtener_departamentos()
    obras = []

    while True:
        opcion = menu_principal()
        
        if opcion == 1:  # Por departamento
            print("\nDepartamentos disponibles:")
            for dept in departamentos:
                print(f"{dept.id}: {dept.nombre}")

            try:
                dept_id = int(input("\nIngrese el ID del departamento: "))
                obras = obtener_obras_por_departamento(dept_id)
                mostrar_obras(obras)
            except ValueError:
                print("ID de departamento inválido.")

        elif opcion == 2:  # Por nacionalidad
            if not obras:
                print("Primero debe seleccionar un departamento para cargar obras.")
                continue
                
            nacionalidades = obtener_nacionalidades(obras)
            print("\nNacionalidades disponibles:")
            for i, nac in enumerate(nacionalidades, 1):
                print(f"{i}. {nac}")

            try:
                seleccion = int(input("\nSeleccione una nacionalidad: ")) - 1
                if 0 <= seleccion < len(nacionalidades):
                    obras_filtradas = obtener_obras_por_nacionalidad(obras, nacionalidades[seleccion])
                    mostrar_obras(obras_filtradas)
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Por favor ingrese un número válido.")

        
