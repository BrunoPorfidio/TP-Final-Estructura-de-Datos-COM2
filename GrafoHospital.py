from collections import deque
import heapq
from typing import List


class Hospital:
    def __init__(self, id: int, nombre: str, especialidad: str):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.conexiones = {}  # Inicializa un diccionario para las conexiones

    def __str__(self):
        return f"{self.nombre}: \n     - ID: {self.id}\n     - Especialidad: {(self.especialidad)}"


class GrafoHospitales:

    def __init__(self):
        self.hospitales = {}  # Almacena hospitales con su nombre como clave

    def agregar_hospital(self, id: int, nombre: str, especialidad):
        nombre = nombre.strip()
        if id not in self.hospitales:
            self.hospitales[id] = Hospital(id, nombre, especialidad)
        else:
            print(f"El hospital ya existe.")

    def agregar_conexion(self, id_hospital1: int, id_hospital2: int, distancia: int):
        # Verificar si los IDs de los hospitales existen en el diccionario
        valores = self.hospitales.values()
        if id_hospital1 in self.hospitales and id_hospital2 in self.hospitales:
            # Usando el ID del hospital como clave
            self.hospitales[id_hospital1].conexiones[id_hospital2] = distancia
            self.hospitales[id_hospital2].conexiones[id_hospital1] = distancia
            print(f"Conexión entre '{id_hospital1}' y '{id_hospital2}' agregada con distancia {distancia}.")
        else:
            print(f"Uno o ambos hospitales no existen: '{id_hospital1}', '{id_hospital2}'.")

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

    def mejor_ruta_ambulancia(self, origen: int, destino: int):
            # Verificar si los hospitales con los ID proporcionados existen en el grafo
            if origen not in self.hospitales:
                print(f"El hospital de origen con ID '{origen}' no existe.")
                return
            if destino not in self.hospitales:
                print(f"El hospital de destino con ID '{destino}' no existe.")
                return

            # Llamar a un método de algoritmo de ruta más corta, como Dijkstra (implementado previamente)
            ruta, distancia = self.dijkstra(origen, destino)

            # Mostrar la ruta y la distancia si existe una ruta
            if ruta:
                print(" -> ".join(str(self.hospitales[hospital].nombre) for hospital in ruta))  # Mostrar nombres de los hospitales
                print(f"Distancia total: {distancia}")
            else:
                print(f"No se encontró una ruta desde el hospital con ID {origen} a {destino}.")

    def bfs(self, inicio: int, fin: int):
        # Verificar si los hospitales con los IDs proporcionados existen en el grafo
        if inicio not in self.hospitales or fin not in self.hospitales:
            print("Uno o ambos hospitales no existen.")
            return
        
        # Cola para explorar los hospitales y diccionario para llevar un registro del camino
        queue = deque([inicio])
        visited = {inicio: None}  # Guarda el nodo anterior para reconstruir el camino
        
        while queue:
            hospital_actual = queue.popleft()
            
            # Si llegamos al hospital de destino, reconstruimos el camino
            if hospital_actual == fin:
                ruta = []
                while hospital_actual is not None:
                    ruta.append(hospital_actual)
                    hospital_actual = visited[hospital_actual]
                return list(reversed(ruta))  # Regresar la ruta en el orden correcto
            
            # Explorar los hospitales vecinos
            for vecino in self.hospitales[hospital_actual].conexiones:
                if vecino not in visited:
                    visited[vecino] = hospital_actual
                    queue.append(vecino)

    def dfs(self, inicio: int, fin: int):
        # Verificar si los hospitales con los IDs proporcionados existen en el grafo
        if inicio not in self.hospitales or fin not in self.hospitales:
            print("Uno o ambos hospitales no existen.")
            return
        
        # Pila para la exploración DFS y diccionario para llevar el seguimiento del camino
        stack = [inicio]
        visited = {inicio: None}  # Guarda el nodo anterior para reconstruir el camino
        
        while stack:
            hospital_actual = stack.pop()
            
            # Si llegamos al hospital de destino, reconstruimos el camino
            if hospital_actual == fin:
                ruta = []
                while hospital_actual is not None:
                    ruta.append(hospital_actual)
                    hospital_actual = visited[hospital_actual]
                return list(reversed(ruta))  # Regresar la ruta en el orden correcto
            
            # Explorar los hospitales vecinos
            for vecino in self.hospitales[hospital_actual].conexiones:
                if vecino not in visited:
                    visited[vecino] = hospital_actual
                    stack.append(vecino)

    def mostrar_hospitales(self):
        """Muestra todos los hospitales con su ID y especialidad."""
        print("Lista de hospitales:")
        for hospital in self.hospitales.values():
            print(f"ID: {hospital.id}, Nombre: {hospital.nombre}, Especialidad: {hospital.especialidad}")
