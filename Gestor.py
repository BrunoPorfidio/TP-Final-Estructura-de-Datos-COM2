from ArbolAVL import ArbolAVL
from ColaPrioridad import ColaPrioridad
from Paciente import Paciente, Medicamento, Enfermedad

class GestorPacientes:
    def __init__(self):
        self.arbol_pacientes = ArbolAVL()
        self.cola_urgencias = ColaPrioridad()
        self.contador_id = 1

    def agregar_paciente(self, nombre: str, edad: int, gravedad: int):
        nuevo_paciente = Paciente(self.contador_id, nombre, edad, gravedad)
        self.arbol_pacientes.insertar(nuevo_paciente)
        self.cola_urgencias.insertar(nuevo_paciente)
        self.contador_id += 1
        return nuevo_paciente

    def buscar_paciente(self, id: int):
        nodo = self.arbol_pacientes.buscar(id)
        return nodo.paciente if nodo else None

    def eliminar_paciente(self, id: int):
        paciente = self.buscar_paciente(id)
        if paciente:
            self.arbol_pacientes.eliminar(id)
            # Nota: Eliminar de la cola de prioridad requeriría una implementación más compleja
            return True
        return False

    def modificar_paciente(self, id: int, nombre: str = None, edad: int = None, gravedad: int = None):
        paciente = self.buscar_paciente(id)
        if paciente:
            if nombre:
                paciente.nombre = nombre
            if edad:
                paciente.edad = edad
            if gravedad:
                paciente.gravedad = gravedad
            print("Datos del paciente actualizados.")
        else:
            print("Paciente no encontrado.")

    def agregar_evento_medico(self, id: int, tipo: str, detalles: str):
        paciente = self.buscar_paciente(id)
        if paciente:
            paciente.agregar_evento_medico(tipo, detalles)
            print("Evento médico agregado.")
        else:
            print("Paciente no encontrado.")

    def mostrar_historial_clinico(self, id: int):
        paciente = self.buscar_paciente(id)
        if paciente:
            print(paciente.detalle_completo())
        else:
            print("Paciente no encontrado.")

    def agregar_enfermedad(self, id: int, nombre_enfermedad: str):
        paciente = self.buscar_paciente(id)
        if paciente:
            enfermedad = Enfermedad(nombre_enfermedad)
            paciente.agregar_enfermedad(enfermedad)
            print(f"Enfermedad '{nombre_enfermedad}' agregada al paciente {paciente.nombre}.")
        else:
            print("Paciente no encontrado.")

    def agregar_medicamento(self, id: int, nombre_medicamento: str):
        paciente = self.buscar_paciente(id)
        if paciente:
            medicamento = Medicamento(nombre_medicamento)
            paciente.agregar_medicamento(medicamento)
            print(f"Medicamento '{nombre_medicamento}' agregado al paciente {paciente.nombre}.")
        else:
            print("Paciente no encontrado.")