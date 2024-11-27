class Hospital:
    def __init__(self, id: int, nombre: str, especialidad: str):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.conexiones = {}  # Inicializa un diccionario para las conexiones

    def __str__(self):
        return f"{self.nombre}: \n     - ID: {self.id}\n     - Especialidad: {(self.especialidad)}"
