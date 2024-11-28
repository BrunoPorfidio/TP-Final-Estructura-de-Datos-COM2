from datetime import datetime

class Enfermedad:
    def __init__(self, nombre: str, fecha: datetime = None):
        self.nombre = nombre
        self.fecha = fecha or datetime.now()

    def __str__(self) -> str:
        return f"{self.nombre} [Fecha: {self.fecha.strftime('%d-%m-%Y | %H:%M')}]"
