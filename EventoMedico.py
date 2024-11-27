from datetime import datetime

class EventoMedico:
    def __init__(self, tipo: str, detalles: str, fecha: datetime = None):
        self.tipo = tipo
        self.detalles = detalles
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"{self.tipo}: {self.detalles} [Fecha: {self.fecha.strftime('%d-%m-%Y | %H:%M')}]"