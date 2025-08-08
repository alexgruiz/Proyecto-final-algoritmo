import requests 
from models import Departamento, Artista, Obra

def obtener_departamentos ():
  ''Obtiene la lista de departamentos del museo desde la API''
  url = ''https://collectionapi.metmuseum.org/public/collection/v1/departments''
  response = requests.get(url)
  data = response.json ()

  departamentos = []
  for dept in data['departments']:
      departamentos.append(Departamento(dept['departmentId'], dept['displayName']))

  return departamentos

def obtener_obras_por_departamento(departamento_id):
   # Obtiene las obras de un departamento seleccionado
   url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={departamento_id}" 
   response = requests.get(url)
   data = response.json()

   print(f'Total de obras: {data['total']}')
   print(''Filtrando obras:'')
   obras = []
   for obra_id in data['objectIDs'][:10]:  # Limitado a 10 obras para no sobrecargar la API
        # Si se colocan mas de 10, la API responde con errores variados 
        print(f'Obteniendo detalles de la obra ID: {obra_id}')
        obra_data = obtener_detalle_obra(obra_id)
        if obra_data:
            obras.append(obra_data)
   return obras    


def obtener_detalle_obra(obra_id): 
    # Obtiene los detalles completos de una obra seleccionada o determinada 
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}"
    response = requests.get(url)
    data = response.json()

    if not data.get('artistDisplayName'):
        return None 

    # Crear instancias de Artista, Dpto y obra 
    artista = Artista(
        nombre =data['artistDisplayName'],
        nacionalidad = data.get('artistNationality', 'Desconocida'),
        fecha_nacimiento = data.get ('artistBegindate', 'Desconocida'),
        fecha_muerte= data.get('artistEndDate', 'Desconocida')
    )

    departamento = Departamento(
        data.get('departmentId', 0),
        data.get('department', 'Desconocido')
    )

    obra = Obra(
        id = data['objectID'],
        titulo = data['title'], 
        artista = artista, 
        departamento = departamento, 
        tipo= data['classification'], 
        fecha_creacion=data['objectDate'], 
        imagen_url= data.get('primaryImageSmall', '')
    )

    return obra

    # Se obtienen las obras filtradas por nacionalidad o autor
    def obtener_obras_por_nacionalidad(obras,nacionalidad):
        'Filtra las obras según nacionalidad del artista'
        return [obra for obra in obras if obra.artista.nacionalidad.lower() == nacionalidad.lower()]
    
    def obtener_obras_por_autor(obras, nombre_autor):
        ''Filtra obras por nombre del artista''
        return [obra for obra in obras if nombre_autor.lower() in obra.artista.nombre.lower()]

        
   


    
