from datetime import datetime
from typing import List
from EventoMedico import EventoMedico
from Medicamento import Medicamento
from Enfermedad import Enfermedad

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

    def __eq__(self, other):
        """Compara dos pacientes basándose en el ID (o cualquier atributo único)."""
        if isinstance(other, Paciente):
            return self.id == other.id
        return False

    def __hash__(self):
        """Genera un valor hash basado en el ID del paciente."""
        return hash(self.id)

    def agregar_evento_medico(self, tipo: str, detalles: str):
        self.historial.append(EventoMedico(tipo, detalles))

    def agregar_medicamento(self, medicamento: str):
        self.medicamentos.append(Medicamento(medicamento))  # Agregar medicamento como objeto

    def agregar_enfermedad(self, enfermedad: str):
        self.enfermedades.append(Enfermedad(enfermedad))  # Agregar enfermedad al historial

    def __str__(self):
        return f"\n·ID: {self.id}\n Nombre: {self.nombre}\n Edad: {self.edad}\n Gravedad: {self.gravedad}\n ID de hospital actual: {self.id_hospital}"

    def detalle_completo(self):
        # Formatear el historial
        historial_str = '\n    '.join(f"- {evento}" for evento in self.historial)
        
        # Formatear los medicamentos
        medicamentos_str = '\n    '.join(f"- {medicamento}" for medicamento in self.medicamentos)
        
        # Formatear las enfermedades
        enfermedades_str = '\n    '.join(f"- {enfermedad}" for enfermedad in self.enfermedades)
        
        # Devolver el string final formateado
        return (f"{self}\n"
                f"Historial:\n    {historial_str}\n"
                f"Medicamentos:\n    {medicamentos_str}\n"
                f"Enfermedades:\n    {enfermedades_str}")