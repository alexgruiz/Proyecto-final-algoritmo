from PIL import Image 
import requests 
from io import BytesIO
def mostrar_imagen(url):
    # Muestra la imagen de una obra desde su URL
    try:
        response = requests.get(url)
        img= Image.open(BytesIO(response.content))
        img.show()
    except:
        print("No se pudo mostrar la imagen")
def obtener_nacionalidades(obras):
    # Obtiene una lista de nacionalidades unicas de los artistas
    nacionalidades = set()
    for obra in obras:
        if obra.artista.nacionalidad:
            nacionalidades.add(obra.artista.nacionalidad)
    return list(nacionalidades)
def obtener_autores(obras):
    # Obtiene una lista de artistas de las obras
    autores = set()
    for obra in obras:
        if obra.artista.nombre:
            autores.add(obra.artista.nombre.strip())
    return sorted(autores)

