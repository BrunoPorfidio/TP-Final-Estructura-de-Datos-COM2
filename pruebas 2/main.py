from datetime import datetime

class Enfermedad:
    def __init__(self, nombre, fecha=None):
        self.nombre = nombre
        self.fecha = fecha if fecha else datetime.now()

    def __str__(self):
        return f"{self.nombre} (Fecha: {self.fecha.strftime('%Y-%m-%d')})"

class Medicamento:
    def __init__(self, nombre, fecha=None):
        self.nombre = nombre
        self.fecha = fecha if fecha else datetime.now()

    def __str__(self):
        return f"{self.nombre} (Fecha: {self.fecha.strftime('%Y-%m-%d')})"

class NodoAVL:
    def __init__(self, id, paciente):
        self.id = id
        self.paciente = paciente
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class ArbolAVL:
    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def calcular_balance(self, nodo):
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)) + 1
        x.altura = max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)) + 1
        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)) + 1
        y.altura = max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)) + 1
        return y

    def insertar(self, nodo, id, paciente):
        if not nodo:
            return NodoAVL(id, paciente)
        if id < nodo.id:
            nodo.izquierda = self.insertar(nodo.izquierda, id, paciente)
        else:
            nodo.derecha = self.insertar(nodo.derecha, id, paciente)
        
        nodo.altura = max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha)) + 1
        balance = self.calcular_balance(nodo)

        if balance > 1 and id < nodo.izquierda.id:
            return self.rotacion_derecha(nodo)
        if balance < -1 and id > nodo.derecha.id:
            return self.rotacion_izquierda(nodo)
        if balance > 1 and id > nodo.izquierda.id:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)
        if balance < -1 and id < nodo.derecha.id:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def eliminar(self, nodo, id):
        if not nodo:
            return nodo
        if id < nodo.id:
            nodo.izquierda = self.eliminar(nodo.izquierda, id)
        elif id > nodo.id:
            nodo.derecha = self.eliminar(nodo.derecha, id)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda

            temp = self.obtener_minimo(nodo.derecha)
            nodo.id = temp.id
            nodo.paciente = temp.paciente
            nodo.derecha = self.eliminar(nodo.derecha, temp.id)

        nodo.altura = max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha)) + 1
        balance = self.calcular_balance(nodo)

        if balance > 1 and self.calcular_balance(nodo.izquierda) >= 0:
            return self.rotacion_derecha(nodo)
        if balance < -1 and self.calcular_balance(nodo.derecha) <= 0:
            return self.rotacion_izquierda(nodo)
        if balance > 1 and self.calcular_balance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)
        if balance < -1 and self.calcular_balance(nodo.derecha) > 0:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def obtener_minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def buscar(self, nodo, id):
        if not nodo or nodo.id == id:
            return nodo
        if id < nodo.id:
            return self.buscar(nodo.izquierda, id)
        return self.buscar(nodo.derecha, id)
    
    def mostrar(self, nodo):
        if nodo:
            self.mostrar(nodo.izquierda)
            print(f"\n")
            print("<=============================>")
            print(nodo.paciente)            
            print("<=============================>")
            self.mostrar(nodo.derecha)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

class Paciente:
    def __init__(self, nombre: str, edad: int, id: int, gravedad: int):
        self.nombre = nombre
        self.edad = edad
        self.id = id
        self.historial_enfermedades = ListaEnlazada()
        self.historial_medicamentos = ListaEnlazada()
        self.gravedad = gravedad

    def agregar_enfermedad(self, enfermedad):
        self.historial_enfermedades.agregar(enfermedad)

    def agregar_medicamento(self, medicamento):
        self.historial_medicamentos.agregar(medicamento)

    def mostrar_historial_enfermedades(self):
        return self.historial_enfermedades.mostrar()

    def mostrar_historial_medicamentos(self):
        return self.historial_medicamentos.mostrar()
    
    def __str__(self):
        return f"\nPaciente: \n - Identificacion Medica (ID): {self.id}\n - Nombre: {self.nombre}\n - Edad: {self.edad} años\n - Gravedad: {self.gravedad} "
    
class Menu:
    def __init__(self):
        self.pacientes = ArbolAVL()
        self.raiz = None
        self.contador_id = 1

    def mostrar_menu(self):
        seguir_viendo_menu = True
        while seguir_viendo_menu:
            print("\n--- Menú ---")
            print("1. Agregar paciente nuevo")
            print("2. Eliminar paciente")
            print("3. Modificar datos de un paciente")
            print("4. Mostrar Pacientes Registrados.")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.eliminar_paciente()
            elif opcion == "3":
                self.pacientes.mostrar(self.raiz)
                self.modificar_paciente()
            elif opcion == "4":
                self.pacientes.mostrar(self.raiz)
            elif opcion == "5":
                print(f"\n")
                print("<========================>")
                print("Saliendo del programa...")
                print("<========================>")
                seguir_viendo_menu = False
            else:
                print("Opción inválida. Intente nuevamente.")

    def agregar_paciente(self):
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        gravedad = int(input("Gravedad del paciente (1-5): "))
        nuevo_paciente = Paciente(nombre, edad, self.contador_id, gravedad)
        self.raiz = self.pacientes.insertar(self.raiz, self.contador_id, nuevo_paciente)
        self.contador_id += 1
        print(f"Paciente agregado con ID: {self.contador_id - 1}")

    def eliminar_paciente(self):
        id_eliminar = int(input("Ingrese el ID del paciente a eliminar: "))
        self.raiz = self.pacientes.eliminar(self.raiz, id_eliminar)
        print(f"Paciente con ID {id_eliminar} eliminado (si existía).")

    def modificar_paciente(self):
        id_modificar = int(input("Ingrese el ID del paciente a modificar: "))
        nodo_paciente = self.pacientes.buscar(self.raiz, id_modificar)
        if nodo_paciente:
            paciente = nodo_paciente.paciente
            print(f"Paciente encontrado: {paciente}")
            
            nuevo_nombre = input(f"Nuevo nombre ({paciente.nombre}): ") or paciente.nombre
            nueva_edad = int(input(f"Nueva edad ({paciente.edad}): ") or paciente.edad)
            nueva_gravedad = int(input(f"Nueva gravedad ({paciente.gravedad}): ") or paciente.gravedad)
            
            paciente.nombre = nuevo_nombre
            paciente.edad = nueva_edad
            paciente.gravedad = nueva_gravedad
            
            print("Paciente modificado exitosamente.")
        else:
            print(f"No se encontró un paciente con ID {id_modificar}")

    # Ejemplo de uso
if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()  # Llamamos al método para mostrar el menú