from datetime import datetime
from typing import List

class EventoMedico:
    def __init__(self, tipo: str, detalles: str, fecha: datetime = None):
        self.tipo = tipo
        self.detalles = detalles
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"{self.tipo}: {self.detalles} (Fecha: {self.fecha.strftime('%Y-%m-%d')})"

class Enfermedad:
    def __init__(self, nombre: str, fecha: datetime = None):
        self.nombre = nombre
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"{self.nombre} (Fecha: {self.fecha.strftime('%Y-%m-%d')})"

class Medicamento:
    def __init__(self, nombre: str, fecha: datetime = None):
        self.nombre = nombre
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"{self.nombre} (Fecha: {self.fecha.strftime('%Y-%m-%d')})"

class Paciente:
    def __init__(self, id: int, nombre: str, edad: int, gravedad: int, id_hospital: int):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.gravedad = gravedad
        self.id_hospital = id_hospital
        self.historial: List[EventoMedico] = []
        self.medicamentos: List[Medicamento] = []  # Cambiado a lista de objetos Medicamento
        self.enfermedades: List[Enfermedad] = []  # Nuevo historial de enfermedades

    def agregar_evento_medico(self, tipo: str, detalles: str):
        self.historial.append(EventoMedico(tipo, detalles))

    def agregar_medicamento(self, medicamento: str):
        self.medicamentos.append(Medicamento(medicamento))  # Agregar medicamento como objeto

    def agregar_enfermedad(self, enfermedad: str):
        self.enfermedades.append(Enfermedad(enfermedad))  # Agregar enfermedad al historial

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Gravedad: {self.gravedad}"
    

    def detalle_completo(self):
        return (f"{self}\n"
                f"Historial: {'\n '.join(str(evento) for evento in self.historial)}\n"
                f"Medicamentos: {'\n '.join(str(medicamento) for medicamento in self.medicamentos)}\n"
                f"Enfermedades: {'\n '.join(str(enfermedad) for enfermedad in self.enfermedades)}")  # Incluir enfermedades
