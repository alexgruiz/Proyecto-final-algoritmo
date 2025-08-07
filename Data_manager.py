import requests 
from models import Departamento, Artista, Obra

def obtener departamentos ():
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


    
