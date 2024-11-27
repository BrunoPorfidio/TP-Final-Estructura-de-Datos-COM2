from collections import deque
import heapq
from Hospital import Hospital


class GrafoHospitales:

    def __init__(self):
        self.hospitales = {}  # Almacena hospitales con su nombre como clave

    def agregar_hospital(self, id: int):
        # Validación del nombre del hospital
        nombre_valido = False
        while not nombre_valido:
            nombre = input("Ingrese el nombre del hospital a agregar: ").strip()  # Eliminamos espacios innecesarios
            if nombre:  # Verificamos que no esté vacío
                nombre_valido = True
            else:
                print("El nombre del hospital no puede estar vacío.")

        # Validación de la especialidad
        especialidad_valida = False
        while not especialidad_valida:
            especialidad = input("Ingrese la especialidad del hospital: ").strip()
            if especialidad:  # Verificamos que la especialidad no esté vacía
                especialidad_valida = True
            else:
                print("La especialidad del hospital no puede estar vacía.")

        # Verificar si el hospital ya existe
        if id not in self.hospitales:
            # Si no existe, se agrega el hospital
            self.hospitales[id] = Hospital(id, nombre, especialidad)
            print(f"Hospital '{nombre}' agregado.")
        else:
            # Si el hospital ya existe, mostrar mensaje de error
            print(f"El hospital con ID {id} ya existe.")

    def agregar_conexion(self):
        # Mostrar hospitales disponibles
        self.mostrar_hospitales()

        # Validación del primer hospital
        id_hospital1_valido = False
        while not id_hospital1_valido:
            id_hospital1 = input("Ingrese el ID del primer hospital: ")
            
            if id_hospital1.isdigit():  # Verificar si el ID es un número
                id_hospital1 = int(id_hospital1)
                if id_hospital1 in self.hospitales:
                    id_hospital1_valido = True
                else:
                    print(f"El hospital con ID {id_hospital1} no existe. Por favor, ingrese un ID válido.")
            else:
                print("El ID del hospital debe ser un número entero.")

        # Validación del segundo hospital
        id_hospital2_valido = False
        while not id_hospital2_valido:
            id_hospital2 = input("Ingrese el ID del segundo hospital: ")
            
            if id_hospital2.isdigit():  # Verificar si el ID es un número
                id_hospital2 = int(id_hospital2)
                if id_hospital2 in self.hospitales:
                    id_hospital2_valido = True
                else:
                    print(f"El hospital con ID {id_hospital2} no existe. Por favor, ingrese un ID válido.")
            else:
                print("El ID del hospital debe ser un número entero.")

        # Validación de la distancia
        distancia_valida = False
        while not distancia_valida:
            distancia = input("Ingrese la distancia (en KM) entre los hospitales: ")
            
            if distancia.isdigit():  # Verificar si la distancia es un número
                distancia = int(distancia)
                if distancia > 0:
                    distancia_valida = True
                else:
                    print("La distancia debe ser un número entero positivo.")
            else:
                print("La distancia debe ser un número entero.")

        # Verificar si la conexión ya existe
        if id_hospital2 in self.hospitales[id_hospital1].conexiones:
            print(f"Ya existe una conexión entre el hospital {id_hospital1} y el hospital {id_hospital2}.")
        else:
            # Agregar la conexión entre los hospitales
            self.hospitales[id_hospital1].conexiones[id_hospital2] = distancia
            self.hospitales[id_hospital2].conexiones[id_hospital1] = distancia
            print(f"Conexión entre '{id_hospital1}' y '{id_hospital2}' agregada con distancia {distancia}.")

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

    def mejor_ruta_ambulancia(self):
        # Validación para el hospital de origen
        origen_valido = False
        while not origen_valido:
            origen = input("Ingrese el hospital de origen: ")
            
            if origen.isdigit():  # Verificar que el ID sea un número entero
                origen = int(origen)
                if origen in self.hospitales:
                    origen_valido = True
                else:
                    print(f"El hospital con ID '{origen}' no existe. Por favor, ingrese un ID válido.")
            else:
                print("El ID del hospital debe ser un número entero.")

        # Validación para el hospital de destino
        destino_valido = False
        while not destino_valido:
            destino = input("Ingrese el hospital de destino: ")
            
            if destino.isdigit():  # Verificar que el ID sea un número entero
                destino = int(destino)
                if destino in self.hospitales:
                    destino_valido = True
                else:
                    print(f"El hospital con ID '{destino}' no existe. Por favor, ingrese un ID válido.")
            else:
                print("El ID del hospital debe ser un número entero.")
        
        # Llamar al algoritmo de Dijkstra para obtener la mejor ruta
        ruta, distancia = self.dijkstra(origen, destino)

        # Mostrar la ruta y la distancia si existe una ruta
        if ruta:
            print("Ruta más corta desde el hospital de origen al destino:")
            print(" -> ".join(str(self.hospitales[hospital].nombre) for hospital in ruta))  # Mostrar los nombres de los hospitales
            print(f"Distancia total: {distancia} km")
        else:
            print(f"No se encontró una ruta desde el hospital con ID {origen} a {destino}.")

    def bfs(self, inicio: int, fin: int):
        
        # Verificar si los hospitales con los IDs proporcionados existen en el grafo
        if inicio not in self.hospitales:
            print(f"El hospital de inicio con ID '{inicio}' no existe.")
            return []
        if fin not in self.hospitales:
            print(f"El hospital de destino con ID '{fin}' no existe.")
            return []

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

        # Si no se encontró una ruta
        print(f"No se encontró una ruta desde el hospital con ID {inicio} a {fin}.")
        return []

    def dfs(self, inicio: int, fin: int):
        # Verificar si los hospitales con los IDs proporcionados existen en el grafo
        if inicio not in self.hospitales:
            print(f"El hospital de inicio con ID '{inicio}' no existe.")
            return []
        if fin not in self.hospitales:
            print(f"El hospital de destino con ID '{fin}' no existe.")
            return []
        
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

        # Si no se encontró una ruta
        print(f"No se encontró una ruta desde el hospital con ID {inicio} a {fin}.")
        return []

    def mostrar_hospitales(self):
        """Muestra todos los hospitales con su ID y especialidad."""
        print("Lista de hospitales:")
        for hospital in self.hospitales.values():
            print(f"ID: {hospital.id}, Nombre: {hospital.nombre}, Especialidad: {hospital.especialidad}")