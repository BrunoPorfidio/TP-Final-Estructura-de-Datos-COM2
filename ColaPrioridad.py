import heapq
from Paciente import Paciente

class ColaPrioridad:
    def __init__(self):
        self.heap = []

    def insertar(self, paciente: Paciente):
        heapq.heappush(self.heap, (-paciente.gravedad, paciente.id, paciente))

    def atender_siguiente(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None

    def esta_vacia(self):
        return len(self.heap) == 0

    def tamano(self):
        return len(self.heap)