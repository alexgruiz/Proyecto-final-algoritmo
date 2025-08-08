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

        elif opcion == 3:  # Por autor
            if not obras:
                print("Primero debe seleccionar un departamento para cargar obras.")
                continue

            autores = obtener_autores(obras)
            print("\nAutores disponibles:")
            for i, autor in enumerate(autores, 1):
                print(f"{i}. {autor}")

            try:
                seleccion = int(input("\nSeleccione un autor (num): "))
                if 1 <= seleccion <= len(autores):
                    nombre = autores[seleccion - 1]
                else:
                    print("Número inválido.")
                    continue

                obras_filtradas = obtener_obras_por_autor(obras, nombre)
                mostrar_obras(obras_filtradas)
            
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == 4:  # Salir
            print("Saliendo del sistema")
            break

        else:
            print("Opción no válida. Por favor intente nuevamente.")
        
        # Si hay obras mostradas, permitir ver detalles
        if obras:
            print("\n¿Desea ver los detalles de una obra? (ingrese ID o 0 para continuar)")
            try:
                obra_id = int(input("ID: "))
                if obra_id != 0:
                    obra_seleccionada = None
                    for obra in obras:
                        if obra.id == obra_id:
                            obra_seleccionada = obra
                            break
                    mostrar_detalle_obra(obra_seleccionada)
            except ValueError:
                print("Entrada inválida.")

if __name__ == "__main__":
    main()
                    
