# class Paciente:
#     def __init__(self, id_medico, nombre, edad, historial_enfermedades=None, medicamentos=None):
#         self.id_medico = id_medico
#         self.nombre = nombre
#         self.edad = edad
#         self.historial_enfermedades = historial_enfermedades or []
#         self.medicamentos = medicamentos or []

#     def añadir_enfermedad(self, enfermedad):                                        # SE PODRIA PONER LOS METODOS EN PRIVADO
#         self.historial_enfermedades.append(enfermedad)

#     def eliminar_enfermedad(self, enfermedad):
#         if enfermedad in self.historial_enfermedades:
#             self.historial_enfermedades.remove(enfermedad)

#     def añadir_medicamento(self, medicamento):
#         self.medicamentos.append(medicamento)

#     def eliminar_medicamento(self, medicamento):
#         if medicamento in self.medicamentos:
#             self.medicamentos.remove(medicamento)

#     def modificar_datos(self, nombre=None, edad=None):
#         if nombre:
#             self.nombre = nombre
#         if edad:
#             self.edad = edad


# def buscar_termino(lista, termino, indice=0):
#     if indice >= len(lista):
#         return False
#     if termino.lower() in lista[indice].lower():
#         return True
#     return buscar_termino(lista, termino, indice + 1)


# 1. Desarrollo de Clases e Interfaces (Unidad 1):
# o Define una clase Paciente que encapsule la información médica relevante
# (nombre, edad, historial de enfermedades, medicamentos, etc.).
# o Crea interfaces para la gestión de los datos médicos, permitiendo añadir,
# eliminar, y modificar información.
# Crea el codigo
class Paciente:
    def __init__(self, nombre, edad, historial_enfermedades=None, medicamentos=None):
        self.nombre = nombre
        self.edad = edad
        self.historial_enfermedades = (
            historial_enfermedades if historial_enfermedades else []
        )
        self.medicamentos = medicamentos if medicamentos else []

    def agregar_enfermedad(self, enfermedad):
        self.historial_enfermedades.append(enfermedad)

    def eliminar_enfermedad(self, enfermedad):
        self.historial_enfermedades.remove(enfermedad)

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def eliminar_medicamento(self, medicamento):
        self.medicamentos.remove(medicamento)

    def __str__(self):
        return f"Paciente: {self.nombre}, Edad: {self.edad}, Historial de enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}"


class GestorPacientes:
    def __init__(self):
        self.pacientes = {}

    def agregar_paciente(self, paciente):
        self.pacientes[paciente.nombre] = paciente

    def eliminar_paciente(self, nombre):
        if nombre in self.pacientes:
            del self.pacientes[nombre]

    def buscar_paciente(self, nombre):
        return self.pacientes.get(nombre)

    def __str__(self):
        pacientes = "\n".join([str(paciente) for paciente in self.pacientes.values()])
        return f"Gestor de pacientes:\n{pacientes}"


def buscar_enfermedad(paciente, enfermedad):
    if paciente.historial_enfermedades:
        if enfermedad in paciente.historial_enfermedades:
            return True
        else:
            return buscar_enfermedad(paciente, enfermedad)
    return False


class NodoArbol:
    def __init__(self, id, paciente):
        self.id = id
        self.paciente = paciente
        self.izquierda = None
        self.derecha = None


class GestorDatosMedicos:
    def __init__(self):
        self.datos_medicos = {}

    def agregar_datos_medicos(self, paciente_id, datos_medicos):
        if paciente_id not in self.datos_medicos:
            self.datos_medicos[paciente_id] = []
        self.datos_medicos[paciente_id].append(datos_medicos)

    def eliminar_datos_medicos(self, paciente_id, datos_medicos_id):
        if paciente_id in self.datos_medicos:
            self.datos_medicos[paciente_id] = [
                datos
                for datos in self.datos_medicos[paciente_id]
                if datos["id"] != datos_medicos_id
            ]

    def modificar_datos_medicos(
        self, paciente_id, datos_medicos_id, nuevos_datos_medicos
    ):
        if paciente_id in self.datos_medicos:
            for datos in self.datos_medicos[paciente_id]:
                if datos["id"] == datos_medicos_id:
                    datos.update(nuevos_datos_medicos)
                    break

    def obtener_datos_medicos(self, paciente_id):
        if paciente_id in self.datos_medicos:
            return self.datos_medicos[paciente_id]
        else:
            return []

    def obtener_todos_datos_medicos(self):
        return self.datos_medicos


# <====================================>


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, id, paciente):
        if not self.raiz:
            self.raiz = NodoArbol(id, paciente)
        else:
            self._insertar(self.raiz, id, paciente)

    def _insertar(self, nodo, id, paciente):
        if id < nodo.id:
            if nodo.izquierda:
                self._insertar(nodo.izquierda, id, paciente)
            else:
                nodo.izquierda = NodoArbol(id, paciente)
        else:
            if nodo.derecha:
                self._insertar(nodo.derecha, id, paciente)
            else:
                nodo.derecha = NodoArbol(id, paciente)

    def buscar(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, nodo, id):
        if nodo:
            if id == nodo.id:
                return nodo.paciente
            elif id < nodo.id:
                return self._buscar(nodo.izquierda, id)
            else:
                return self._buscar(nodo.derecha, id)
        return None

    def __str__(self):
        pacientes = []
        self._inorden(self.raiz, pacientes)
        return "\n".join([str(paciente) for paciente in pacientes])

    def _inorden(self, nodo, pacientes):
        if nodo:
            self._inorden(nodo.izquierda, pacientes)
            pacientes.append(nodo.paciente)
            self._inorden(nodo.derecha, pacientes)


class NodoArbolGeneral:
    def __init__(self, evento):
        self.evento = evento
        self.hijos = []


class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar(self, evento, padre=None):
        if not self.raiz:
            self.raiz = NodoArbolGeneral(evento)
        else:
            self._insertar(self.raiz, evento, padre)

    def _insertar(self, nodo, evento, padre):
        if nodo.evento == padre:
            nodo.hijos.append(NodoArbolGeneral(evento))
        else:
            for hijo in nodo.hijos:
                self._insertar(hijo, evento, padre)


import heapq


class ColaPrioridades:
    def __init__(self):
        self.cola = []

    def insertar(self, paciente, prioridad):
        heapq.heappush(self.cola, (prioridad, paciente))

    def eliminar(self):
        return heapq.heappop(self.cola)[1]


class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        self.nodos[nombre] = {}

    def agregar_arista(self, origen, destino, peso):
        if origen in self.nodos and destino in self.nodos:
            self.nodos[origen][destino] = peso
            self.nodos[destino][origen] = peso

    def buscar_camino(self, origen, destino):
        if origen not in self.nodos or destino not in self.nodos:
            return None

        visitados = set()
        camino = []
        self._buscar_camino(origen, destino, visitados, camino)
        return camino

    def _buscar_camino(self, nodo, destino, visitados, camino):
        visitados.add(nodo)
        camino.append(nodo)

        if nodo == destino:
            return True

        for vecino in self.nodos[nodo]:
            if vecino not in visitados:
                if self._buscar_camino(vecino, destino, visitados, camino):
                    return True

        camino.pop()
        return False


class RecorridoDFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitados = set()

    def recorrer(self, nodo):
        self.visitados.add(nodo)
        print(nodo)
        for vecino in self.grafo.nodos[nodo]:
            if vecino not in self.visitados:
                self.recorrer(vecino)

    def __str__(self):
        nodos = "\n".join([nodo for nodo in self.visitados])
        return f"Recorrido DFS:\n{nodos}"


class RecorridoBFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitados = set()
        self.cola = []

    def recorrer(self, nodo):
        self.visitados.add(nodo)
        print(nodo)
        self.cola.append(nodo)
        while self.cola:
            nodo_actual = self.cola.pop(0)
            for vecino in self.grafo.nodos[nodo_actual]:
                if vecino not in self.visitados:
                    self.visitados.add(vecino)
                    print(vecino)
                    self.cola.append(vecino)

    def __str__(self):
        nodos = "\n".join([nodo for nodo in self.visitados])
        return f"Recorrido BFS:\n{nodos}"


class OrdenamientoTopologico:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitados = set()
        self.orden = []

    def ordenar(self):
        for nodo in self.grafo.nodos:
            if nodo not in self.visitados:
                self._ordenar(nodo)

    def _ordenar(self, nodo):
        self.visitados.add(nodo)
        for vecino in self.grafo.nodos[nodo]:
            if vecino not in self.visitados:
                self._ordenar(vecino)
        self.orden.append(nodo)

    def obtener_orden(self):
        return self.orden


# Crear un paciente
paciente = Paciente("Juan", 30, ["Dengue", "COVID"], ["Ibuprofeno", "Paracetamol"])
paciente1 = Paciente("carlos", 30, ["Epoc", "Asma"], ["Tanque de oxigeno", "Curitas"])
paciente2 = Paciente("pepe", 30, ["Esgince", "Fractura"], ["Ibuprofeno", "Paracetamol"])

# Imprimir el paciente
print("\nPacientes:")
print(paciente)
print(paciente1)
print(paciente2)


# Crear un gestor de pacientes
gestor_pacientes = GestorPacientes()
gestor_pacientes.agregar_paciente(paciente)

# Imprimir el gestor de pacientes
print("\nGestor de pacientes:")
print(gestor_pacientes)

# Crear un gestor de pacientes
gestor_pacientes = GestorPacientes()


# Agregar el paciente al gestor de pacientes
gestor_pacientes.agregar_paciente(paciente)

# Imprimir la información de los pacientes
print(gestor_pacientes)

# Crear un gestor de datos médicos
gestor_datos_medicos = GestorDatosMedicos()

# Agregar datos médicos a un paciente
gestor_datos_medicos.agregar_datos_medicos(
    "paciente1", {"id": 1, "nombre": "Juan", "edad": 30, "enfermedad": "Diabetes"}
)

# Obtener todos los datos médicos de todos los pacientes
todos_datos_medicos = gestor_datos_medicos.obtener_todos_datos_medicos()

# Imprimir todos los datos médicos de todos los pacientes
print(todos_datos_medicos)


# Crear un árbol binario
arbol_binario = ArbolBinario()
arbol_binario.insertar(1, paciente)

# Imprimir el árbol binario
print("\nÁrbol binario:")
print(arbol_binario)

grafo = Grafo()
grafo.agregar_nodo("A")
grafo.agregar_nodo("B")
grafo.agregar_nodo("C")
grafo.agregar_nodo("D")
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("A", "C", 2)
grafo.agregar_arista("B", "D", 3)
grafo.agregar_arista("C", "D", 4)

camino = grafo.buscar_camino("A", "D")
print(camino)  # Output: ["A", "B", "D"] o ["A", "C", "D"]

# Buscar un camino entre dos nodos
camino = grafo.buscar_camino("A", "D")
print("\nCamino entre A y D:")
print(camino)

# Realizar un recorrido DFS
recorrido_dfs = RecorridoDFS(grafo)
recorrido_dfs.recorrer("A")
print("\nRecorrido DFS:")
print(recorrido_dfs)

# Realizar un recorrido BFS
recorrido_bfs = RecorridoBFS(grafo)
recorrido_bfs.recorrer("A")
print("\nRecorrido BFS:")
print(recorrido_bfs)
