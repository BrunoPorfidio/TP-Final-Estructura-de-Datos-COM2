from datetime import datetime
from typing import List

class EventoMedico:
    def __init__(self, tipo: str, detalles: str, fecha: datetime = None):
        self.tipo = tipo #CONSULTA, DIAGNOSTICO, TRATAMIENTO
        self.detalles = detalles
        self.fecha = fecha or datetime.now()
        self.hijos = List[EventoMedico] = []
    
    def agregar_hijo(self, hijo: 'EventoMedico'):
        """Agrega un evento médico relacionado como hijo."""
        self.hijos.append(hijo)

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
        return f"{self.nombre} (Fecha: {self.fecha.strftime('%d-%m-%Y')})"
    
    def get_nombre(self) -> str:
        return self.nombre

class HistorialClinico:
    def __init__(self):
        self.raiz: EventoMedico = None  # Nodo raíz del árbol

    def agregar_evento(self, evento: EventoMedico, padre: EventoMedico = None):
        """
        Agrega un evento médico al historial clínico.
        Si no se especifica un padre, el evento se agrega como raíz.
        """
        if padre is None:
            if self.raiz is None:
                self.raiz = evento
                print(f"Evento raíz agregado: {evento}")
            else:
                print("El historial ya tiene una raíz. Especifica un nodo padre.")
        else:
            padre.agregar_hijo(evento)
            print(f"Evento agregado como hijo de {padre}: {evento}")



class Paciente:
    def __init__(self, id: int, nombre: str, edad: int, gravedad: int):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.gravedad = gravedad
        self.historial = HistorialClinico()  # Ahora es un árbol general
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
    
    def __lt__(self, otro):
        # Comparación inversa para que el paciente con mayor gravedad tenga mayor prioridad
        return self.gravedad > otro.gravedad