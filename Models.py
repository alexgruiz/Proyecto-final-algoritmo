class Departamento:
    def __init__(self, id, nombre):
        self.id = id 
        self.nombre = nombre
    def __str__(self):
        return f"{self.id}: {self.nombre}"
class Artista:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte      
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"
class Obra:
    def __init__(self, id, titulo, artista, departamento, tipo, fecha_creacion, imagen_url):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.departamento = departamento
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.imagen_url = imagen_url      
    def __str__(self):
        return f"{self.id}: {self.titulo} - {self.artista.nombre}"


