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

        # Rotaciones para balancear el árbol
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
            return nodo                                                     #PUNTO 2: FUNCION RECURSIVA PARA BUSCAR UN PACIENTE POR SU ID
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
    
class Menu:                                                                 # PUNTO 1.2: INTERFAZ DE GESTION PARA DATOS MEDICOS

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

    def agregar_paciente(self) -> None:

        dato_incorrecto = True

        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        while dato_incorrecto:
            gravedad = int(input("Gravedad del paciente: (1 a 5): "))
            if gravedad < 1 or gravedad > 5:
                print(f"La gravedad no puede ser {gravedad}, debe ser un valor entre 1 y 5.")
            else:
                dato_incorrecto = False


        id = self.contador_id  # Asigna el ID actual del contador
        nuevo_paciente = Paciente(nombre, edad, id, gravedad)

        # Insertar el paciente en el árbol AVL
        self.raiz = self.pacientes.insertar(self.raiz, id, nuevo_paciente)
        print(f"\n")
        print("<========================>")
        print(f"Paciente {nombre} agregado con ID: {id}")
        print("<========================>")

        self.contador_id += 1  # Incrementa el contador para el próximo paciente

    def eliminar_paciente(self):
        id = int(input("ID del paciente a eliminar: "))
        self.raiz = self.pacientes.eliminar(self.raiz, id)
        print(f"\n")
        print("<========================>")
        print("Paciente eliminado con éxito.")
        print("<========================>")

    def modificar_paciente(self):

        id = int(input("ID del paciente a modificar: "))
        nodo = self.pacientes.buscar(self.raiz, id)

        if nodo:
            print(f"Paciente encontrado: {nodo.paciente}")

            seguir_modificando = True

            while seguir_modificando:

                print("\n--- MENU DE MODIFICACIONES ---")
                print("1. Modificar nombre")
                print("2. Modificar edad")
                print("3. Modificar gravedad")
                print("4. Agregar enfermedad")
                print("5. Agregar medicamento")
                print("6. Finalizar modificación")
                

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
                    nodo.paciente.nombre = nuevo_nombre

                elif opcion == "2":
                    nueva_edad = int(input("Ingrese la nueva edad del paciente: "))
                    nodo.paciente.edad = nueva_edad
                
                elif opcion == "3":
                    nueva_gravedad = int(input(F"ingrese la nueva gravedad del paciente."))
                    dato_incorrecto = True
                    while dato_incorrecto:
                        nueva_gravedad = int(input("Gravedad del paciente: (1 a 5): "))
                        if nueva_gravedad < 1 or nueva_gravedad > 5:
                            print(f"La gravedad no puede ser {nueva_gravedad}, debe ser un valor entre 1 y 5.")
                        else:
                            nodo.paciente.gravedad = nueva_gravedad
                            dato_incorrecto = False


                elif opcion == "4":
                    nombre_enfermedad = input("Ingrese el nombre de la enfermedad: ")
                    fecha_enfermedad = input("Ingrese la fecha (YYYY-MM-DD) o presione Enter para hoy: ")
                    if fecha_enfermedad:
                        fecha_enfermedad = datetime.strptime(fecha_enfermedad, '%Y-%m-%d')
                        enfermedad = Enfermedad(nombre_enfermedad, fecha_enfermedad)
                    else:
                        enfermedad = Enfermedad(nombre_enfermedad)
                    nodo.paciente.agregar_enfermedad(enfermedad)
                    print(f"\n")
                    print("<========================>")
                    print("Enfermedad agregada con éxito.")
                    print("<========================>")

                elif opcion == "5":
                    nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                    fecha_medicamento = input("Ingrese la fecha (YYYY-MM-DD) o presione Enter para hoy: ")
                    if fecha_medicamento:
                        fecha_medicamento = datetime.strptime(fecha_medicamento, '%Y-%m-%d')
                        medicamento = Medicamento(nombre_medicamento, fecha_medicamento)
                    else:
                        medicamento = Medicamento(nombre_medicamento)
                    nodo.paciente.agregar_medicamento(medicamento)
                    print(f"\n")
                    print("<========================>")
                    print("Medicamento agregado con éxito.")
                    print("<========================>")

                elif opcion == "6":
                    print(f"\n")
                    print("<========================>")
                    print("Modificación finalizada.")
                    print("<========================>")
                    seguir_modificando = False
                else:
                    print(f"\n")
                    print("<========================>")
                    print("Opción inválida. Intente nuevamente.")
                    print("<========================>")
        else:
            print(f"\n")
            print("<========================>")
            print("Paciente no encontrado.")
            print("<========================>")


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()