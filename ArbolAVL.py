from Paciente import Paciente

class NodoAVL:
    def __init__(self, paciente: Paciente):
        self.paciente = paciente
        self.izquierda = None
        self.derecha = None
        self.altura = 1

    def __eq__(self, other):
        """Compara dos nodos AVL basándose en el paciente que contienen."""
        if isinstance(other, NodoAVL):
            return self.paciente == other.paciente  # Compara los pacientes
        return False

    def __hash__(self):
        """Genera un valor hash basado en el paciente."""
        return hash(self.paciente)  # Usa el hash del paciente para el hash del nodo

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

    def balance(self, nodo):
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x

    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y

    def insertar(self, paciente: Paciente):
        self.raiz = self._insertar(self.raiz, paciente)

    def _insertar(self, nodo, paciente):
        if not nodo:
            return NodoAVL(paciente)
        if paciente.id < nodo.paciente.id:
            nodo.izquierda = self._insertar(nodo.izquierda, paciente)
        else:
            nodo.derecha = self._insertar(nodo.derecha, paciente)
        self.actualizar_altura(nodo)
        balance = self.balance(nodo)
        if balance > 1:
            if paciente.id < nodo.izquierda.paciente.id:
                return self.rotar_derecha(nodo)
            else:
                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                return self.rotar_derecha(nodo)
        if balance < -1:
            if paciente.id > nodo.derecha.paciente.id:
                return self.rotar_izquierda(nodo)
            else:
                nodo.derecha = self.rotar_derecha(nodo.derecha)
                return self.rotar_izquierda(nodo)
        return nodo

    def buscar(self, id: int):
        return self._buscar(self.raiz, id)

    def _buscar(self, nodo, id):
        if not nodo or nodo.paciente.id == id:
            return nodo
        if id < nodo.paciente.id:
            return self._buscar(nodo.izquierda, id)
        return self._buscar(nodo.derecha, id)

    def eliminar(self, id: int):
        self.raiz = self._eliminar(self.raiz, id)

    def _eliminar(self, nodo, id):
        if not nodo:
            return nodo
        if id < nodo.paciente.id:
            nodo.izquierda = self._eliminar(nodo.izquierda, id)
        elif id > nodo.paciente.id:
            nodo.derecha = self._eliminar(nodo.derecha, id)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            min_nodo = self._encontrar_minimo(nodo.derecha)
            nodo.paciente = min_nodo.paciente
            nodo.derecha = self._eliminar(nodo.derecha, min_nodo.paciente.id)
        self.actualizar_altura(nodo)
        balance = self.balance(nodo)
        if balance > 1:
            if self.balance(nodo.izquierda) >= 0:
                return self.rotar_derecha(nodo)
            else:
                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                return self.rotar_derecha(nodo)
        if balance < -1:
            if self.balance(nodo.derecha) <= 0:
                return self.rotar_izquierda(nodo)
            else:
                nodo.derecha = self.rotar_derecha(nodo.derecha)
                return self.rotar_izquierda(nodo)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def recorrido_inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.paciente)
            self._inorden(nodo.derecha, resultado)