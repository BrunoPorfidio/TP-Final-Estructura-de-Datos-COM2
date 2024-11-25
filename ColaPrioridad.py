import heapq
from Paciente import Paciente

class ColaPrioridad:
    def __init__(self):
        self.heap = []
        self.entrada_finder = {}  # mapping of pacientes to entries
        self.REMOVED = '<removed-paciente>'  # placeholder for a removed paciente
        self.contador = 0  # unique sequence count

    def insertar(self, paciente: Paciente):
        if paciente in self.entrada_finder:
            self.eliminar(paciente)
        count = self.contador
        entry = [-paciente.gravedad, count, paciente]
        self.entrada_finder[paciente] = entry
        heapq.heappush(self.heap, entry)
        self.contador += 1

    def eliminar(self, paciente: Paciente):
        entry = self.entrada_finder.pop(paciente)
        entry[-1] = self.REMOVED


    def actualizar(self, paciente: Paciente, nueva_gravedad: int):
        self.eliminar(paciente)
        paciente.gravedad = nueva_gravedad
        self.insertar(paciente)

    def esta_vacia(self):
        return not self.entrada_finder

    def tamano(self):
        return len(self.entrada_finder)

    def mostrar(self):
        if not self.heap:  # Verifica si la cola está vacía
            print("No hay pacientes en la cola de prioridad.")
            return
        # Ordena la lista de pacientes en función de su gravedad
        pacientes_ordenados = sorted(self.entrada_finder.keys(), key=lambda p: -p.gravedad)
    
        for paciente in pacientes_ordenados:
            print(f"Gravedad: {paciente.gravedad}, ID: {paciente.id}, Nombre: {paciente.nombre}")