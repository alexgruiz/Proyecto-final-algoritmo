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

def 


    
