class NodoAVL:
    def __init__(self, paciente):
        self.paciente = paciente
        self.izquierda = None
        self.derecha = None
        self.altura = 1  # Altura del nodo

class ArbolAVL:
    
    def insertar(self, nodo, paciente):
        # Inserción normal de un BST
        if nodo is None:
            return NodoAVL(paciente)

        if paciente.id_paciente < nodo.paciente.id_paciente:
            nodo.izquierda = self.insertar(nodo.izquierda, paciente)
        else:
            nodo.derecha = self.insertar(nodo.derecha, paciente)

        # Actualizar la altura del nodo
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        # Balancear el árbol
        return self.balancear(nodo)

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if nodo is None:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def balancear(self, nodo):
        balance = self.obtener_balance(nodo)

        # Rotación a la derecha
        if balance > 1 and self.obtener_balance(nodo.izquierda) >= 0:
            return self.rotar_derecha(nodo)

        # Rotación a la izquierda-derecha
        if balance > 1 and self.obtener_balance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        # Rotación a la izquierda
        if balance < -1 and self.obtener_balance(nodo.derecha) <= 0:
            return self.rotar_izquierda(nodo)

        # Rotación derecha-izquierda
        if balance < -1 and self.obtener_balance(nodo.derecha) > 0:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        # Realizar rotación
        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))

        return x

    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        # Realizar rotación
        y.izquierda = x
        x.derecha = T2

        # Actualizar alturas
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def preorden(self, nodo):
        if nodo:
            print(nodo.paciente.id_paciente, end=' ')
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def buscar(self, nodo, id_medico):
        if not nodo:  # Caso base: el nodo es None (no encontrado)
            return None

        if id_medico == nodo.paciente.id_medico:  # Si se encuentra el ID
            return nodo.paciente  # Retorna el paciente encontrado

        if id_medico < nodo.paciente.id_medico:  # Buscar en el subárbol izquierdo
            return self.buscar(nodo.izquierda, id_medico)

        # Si no, buscar en el subárbol derecho
        return self.buscar(nodo.derecha, id_medico)