import heapq

class GrafoHospitales:
    def __init__(self):
        self.hospitales = {}

    def agregar_hospital(self, nombre):
        if nombre not in self.hospitales:
            self.hospitales[nombre] = {}

    def agregar_conexion(self, hospital1, hospital2, distancia):
        if hospital1 in self.hospitales and hospital2 in self.hospitales:
            self.hospitales[hospital1][hospital2] = distancia
            self.hospitales[hospital2][hospital1] = distancia

    def dijkstra(self, inicio, fin):
        distancias = {hospital: float('inf') for hospital in self.hospitales}
        distancias[inicio] = 0
        pq = [(0, inicio)]
        camino = {}
        while pq:
            distancia_actual, hospital_actual = heapq.heappop(pq)
            if hospital_actual == fin:
                ruta = []
                while hospital_actual in camino:
                    ruta.append(hospital_actual)
                    hospital_actual = camino[hospital_actual]
                ruta.append(inicio)
                return list(reversed(ruta)), distancia_actual
            if distancia_actual > distancias[hospital_actual]:
                continue
            for vecino, peso in self.hospitales[hospital_actual].items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    camino[vecino] = hospital_actual
                    heapq.heappush(pq, (distancia, vecino))
        return None, float('inf')