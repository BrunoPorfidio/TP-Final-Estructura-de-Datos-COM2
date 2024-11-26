from collections import deque
import heapq
from typing import List


class Hospital:
    def __init__(self, id: int, nombre: str, especialidades: List[str] = None):
        self.id = id
        self.nombre = nombre
        self.especialidades = especialidades or []
        self.conexiones = {}  # Inicializa un diccionario para las conexiones

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}, Especialidades: {', '.join(self.especialidades)})"


class GrafoHospitales:
    def __init__(self):
        self.hospitales = {}  # Almacena hospitales con su nombre como clave

    def agregar_hospital(self, id: int, nombre: str, especialidades: List[str] = None):
        nombre = nombre.strip()
        if nombre not in self.hospitales:
            self.hospitales[nombre] = Hospital(id, nombre, especialidades)
        else:
            print(f"El hospital '{nombre}' ya existe.")

    def agregar_conexion(self, hospital1: str, hospital2: str, distancia: int):
        hospital1 = hospital1.strip()
        hospital2 = hospital2.strip()
        if hospital1 in self.hospitales and hospital2 in self.hospitales:
            # Usando el nombre del hospital como clave
            self.hospitales[hospital1].conexiones[hospital2] = distancia
            self.hospitales[hospital2].conexiones[hospital1] = distancia
        else:
            print(f"Uno o ambos hospitales no existen: '{hospital1}', '{hospital2}'.")

    def dijkstra(self, inicio: str, fin: str):
        distancias = {hospital: float("inf") for hospital in self.hospitales}
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
            for vecino, peso in self.hospitales[hospital_actual].conexiones.items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    camino[vecino] = hospital_actual
                    heapq.heappush(pq, (distancia, vecino))
        return None, float("inf")

    def mejor_ruta_ambulancia(self, origen: str, destino: str):
        origen = origen.strip()
        destino = destino.strip()
        if origen not in self.hospitales:
            print(f"El hospital de origen '{origen}' no existe.")
            return
        if destino not in self.hospitales:
            print(f"El hospital de destino '{destino}' no existe.")
            return
        ruta, distancia = self.dijkstra(origen, destino)
        if ruta:
            print(" -> ".join(ruta))
            print(f"Distancia total: {distancia}")
        else:
            print(f"No se encontró una ruta desde {origen} a {destino}.")

    def bfs(self, inicio: str, fin: str):
        inicio = inicio.strip()
        fin = fin.strip()
        if inicio not in self.hospitales or fin not in self.hospitales:
            print("Uno o ambos hospitales no existen.")
            return
        queue = deque([inicio])
        visited = {inicio: None}  # Guarda el nodo anterior para reconstruir el camino
        while queue:
            hospital_actual = queue.popleft()
            if hospital_actual == fin:
                # Reconstruir el camino
                ruta = []
                while hospital_actual is not None:
                    ruta.append(hospital_actual)
                    hospital_actual = visited[hospital_actual]
                return list(reversed(ruta))
            for vecino in self.hospitales[hospital_actual].conexiones:
                if vecino not in visited:
                    visited[vecino] = hospital_actual
                    queue.append(vecino)