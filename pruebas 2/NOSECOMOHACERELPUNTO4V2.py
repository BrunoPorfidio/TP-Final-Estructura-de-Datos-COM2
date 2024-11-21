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

    def buscar(self, nodo, id) -> object:
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
        self.historial_clinico = None


    def agregar_enfermedad(self, enfermedad):
        self.historial_enfermedades.agregar(enfermedad)

    def agregar_medicamento(self, medicamento):
        self.historial_medicamentos.agregar(medicamento)

    def mostrar_historial_enfermedades(self):
        return self.historial_enfermedades.mostrar()

    def mostrar_historial_medicamentos(self):
        return self.historial_medicamentos.mostrar()

    def agregar_evento_medico(self, tipo, detalles):
        nuevo_evento = EventoMedico(tipo, detalles)
        nuevo_nodo_evento = NodoEventoMedico(nuevo_evento)

        if not self.historial_clinico:
            self.historial_clinico = nuevo_nodo_evento
        else:
            # Si ya hay eventos, los agregamos como subeventos
            actual = self.historial_clinico
            while actual.subeventos:
                actual = actual.subeventos[-1]  # Navegar hasta el último subevento
            actual.agregar_subevento(nuevo_nodo_evento)
    """
    def mostrar_historial_clinico(self):
        def mostrar_eventos(nodo, nivel=0):
            if nodo:
                print("  " * nivel + str(nodo.evento))
                for subevento in nodo.subeventos:
                    mostrar_eventos(subevento, nivel + 1)

        mostrar_eventos(self.historial_clinico)
    """
    def mostrar_historial_clinico(self):
        return self.historial_clinico.mos
    



    def __str__(self):
        # Preparar el historial de enfermedades
        enfermedades = self.mostrar_historial_enfermedades()
        historial_enfermedades = "Historial de Enfermedades:\n"
        if enfermedades:
            historial_enfermedades += "\n".join(f"  - {enfermedad}" for enfermedad in enfermedades)
        else:
            historial_enfermedades += "  - No hay enfermedades registradas."

        # Preparar el historial de medicamentos
        medicamentos = self.mostrar_historial_medicamentos()
        historial_medicamentos = "Historial de Medicamentos:\n"
        if medicamentos:
            historial_medicamentos += "\n".join(f"  - {medicamento}" for medicamento in medicamentos)
        else:
            historial_medicamentos += "  - No hay medicamentos registrados."

        # Información básica del paciente junto con los historiales
        return (
            f"\nPaciente:\n"
            f" - ID: {self.id}\n"
            f" - Nombre: {self.nombre}\n"
            f" - Edad: {self.edad} años\n"
            f" - Gravedad: {self.gravedad}\n"
            f"{historial_enfermedades}\n"
            f"{historial_medicamentos}\n"
        )
        
    
class GestorPacientes:                                                                 
    def __init__(self):
        self.pacientes = ArbolAVL()
        self.raiz = None
        self.contador_id = 1


    def mostrar_gestor(self):

        seguir_viendo_gestor = True
        while seguir_viendo_gestor:
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
                self.pacientes.mostrar(self.raiz)           # SE TIENE QUE MOSTRAR TAMBIEN EL HISTORIAL CLINICO
                self.modificar_paciente()
            elif opcion == "4":
                self.pacientes.mostrar(self.raiz)
            elif opcion == "5":
                print(f"\n")
                print("<========================>")
                print("Saliendo del programa...")
                print("<========================>")
                seguir_viendo_gestor = False
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
                print("6. Modificar historial clinico")
                print("7. Finalizar modificación")
                

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self.modificar_nombre(nodo)

                elif opcion == "2":
                    self.modificar_edad(nodo)

                elif opcion == "3":
                    self.modificar_gravedad(nodo)

                elif opcion == "4":

                    self.agregar_enfermedad(nodo)

                elif opcion == "5":

                    self.agregar_medicamento(nodo)

                elif opcion == "6":
                    self.modificar_historial_clinico(nodo)

                elif opcion == "7":
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

    def modificar_historial_clinico(self, nodo):
        tipo = input("Ingrese el tipo de evento (CONSULTA, DIAGNOSTICO O TRATAMIENTO) :")
        detalles = input("Ingrese detalles del tipo de evento: ")
        nodo.paciente.agregar_evento_medico(tipo, detalles)

    def modificar_nombre(self, nodo):
        nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
        nodo.paciente.nombre = nuevo_nombre

    def modificar_edad(self, nodo):
        nueva_edad = int(input("Ingrese la nueva edad del paciente: "))
        nodo.paciente.edad = nueva_edad
    
    def modificar_gravedad(self, nodo):
        dato_incorrecto = True
        while dato_incorrecto:
            nueva_gravedad = int(input("Ingrese la nueva gravedad del paciente: (1 a 5): "))
            if nueva_gravedad < 1 or nueva_gravedad > 5:
                print(f"La gravedad no puede ser {nueva_gravedad}, debe ser un valor entre 1 y 5.")
            else:
                nodo.paciente.gravedad = nueva_gravedad
                dato_incorrecto = False

    def agregar_enfermedad(self, nodo):
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

    def agregar_medicamento(self, nodo):
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

    def agregar_evento(self, nodo):
        tipo = input("Ingrese el tipo de evento (Consulta, Diagnostico o Tratamiento): ")
        detalles = input("Ingrese detalles del tipo de evento: ")
        nodo.paciente.agregar_evento_medico(tipo, detalles)


class NodoEventoMedico:
    def __init__(self, evento):
        self.evento = evento
        self.subeventos = []

    def agregar_subevento(self, subevento):
        self.subeventos.append(subevento)

class EventoMedico:
    def __init__(self, tipo, detalles, fecha=None):
        self.tipo = tipo  # "Consulta", "Diagnóstico", "Tratamiento"
        self.detalles = detalles
        self.fecha = fecha if fecha else datetime.now()

    def __str__(self):
        return f"{self.tipo}: {self.detalles} (Fecha: {self.fecha.strftime('%Y-%m-%d')})"



if __name__ == "__main__":
    gestor = GestorPacientes()
    gestor.mostrar_gestor()





"""
# Clase para representar cada evento médico en el historial clínico
class EventoMedico:
    def __init__(self, tipo, detalles, fecha=None):
        self.tipo = tipo  # Tipo de evento: 'Consulta', 'Diagnóstico' o 'Tratamiento'
        self.detalles = detalles  # Detalles del evento
        self.fecha = fecha if fecha else datetime.now()  # Fecha del evento
        self.subeventos = []  # Lista de subeventos asociados (hijos)

    def agregar_subevento(self, subevento):
        Agrega un subevento asociado a este evento médico.
        self.subeventos.append(subevento)

    def __str__(self, nivel=0):
        Representación en string del evento y sus subeventos.
        espacio = "  " * nivel
        evento_str = f"{espacio}- {self.tipo}: {self.detalles} (Fecha: {self.fecha.strftime('%Y-%m-%d')})\n"
        for subevento in self.subeventos:
            evento_str += subevento.__str__(nivel + 1)
        return evento_str


"""


"""
    def mostrar_historial_clinico(self):
        # Mostrar historial con numeración
        print(f"\nHistorial clínico de {self.nombre}:")
        self._mostrar_eventos(self.historial_clinico, nivel=1)

    def _mostrar_eventos(self, evento, nivel):
        # Método recursivo para mostrar eventos numerados
        print(f"{nivel} - {evento.tipo} ({evento.detalles}) (Fecha: {evento.fecha.strftime('%Y-%m-%d')})")
        subnivel = 1
        for subevento in evento.subeventos:
            self._mostrar_eventos(subevento, f"{nivel}.{subnivel}")
            subnivel += 1

    def seleccionar_evento(self, numero_evento):
        evento = self._buscar_evento_por_numero(self.historial_clinico, numero_evento.split('.'))
        if evento:
            print(f"\nSeleccionaste el evento: {evento.tipo} ({evento.detalles})")
            self.editar_evento(evento)
        else:
            print("Evento no encontrado.")

    def _buscar_evento_por_numero(self, evento, indices):
        if not indices:
            return evento
        try:
            index = int(indices[0]) - 1
            return self._buscar_evento_por_numero(evento.subeventos[index], indices[1:])
        except (IndexError, ValueError):
            return None

    def editar_evento(self, evento):
        # Opciones para editar el evento seleccionado
        print("\n¿Qué deseas agregar?")
        print("1 - Diagnóstico")
        print("2 - Tratamiento")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            detalles = input("Ingresa los detalles del diagnóstico: ")
            self.agregar_evento_medico(tipo="Diagnóstico", detalles=detalles, evento_padre=evento)
            print("Diagnóstico agregado.")
        elif opcion == "2":
            detalles = input("Ingresa los detalles del tratamiento: ")
            self.agregar_evento_medico(tipo="Tratamiento", detalles=detalles, evento_padre=evento)
            print("Tratamiento agregado.")
        else:
            print("Opción no válida.")

"""





"""
    def agregar_evento_medico(self, tipo, detalles, fecha=None, evento_padre=None):
        Agrega un evento médico al historial clínico. Si se especifica un evento padre,
        el nuevo evento se agrega como subevento.
        nuevo_evento = EventoMedico(tipo, detalles, fecha)
        if evento_padre:
            evento_padre.agregar_subevento(nuevo_evento)
        elif not self.historial_clinico:
            # Si no hay historial, este será el primer evento
            self.historial_clinico = nuevo_evento
        else:
            # Si existe un historial, agrega el evento a la raíz como subevento
            self.historial_clinico.agregar_subevento(nuevo_evento)

    def mostrar_historial_clinico(self):
        Devuelve la representación del historial clínico en string.
        if self.historial_clinico:
            return str(self.historial_clinico)
        else:
            return "No hay historial clínico registrado."
"""

#AGREGO ALGO QUE QUIZAS AYUDE


# Crear el historial del paciente
historial = NodoHistorial("Inicio", "Historial del Paciente")

# Añadir consultas
consulta1 = NodoHistorial("Consulta", "Consulta 1")
consulta2 = NodoHistorial("Consulta", "Consulta 2")
historial.agregar_evento(consulta1)
historial.agregar_evento(consulta2)

# Añadir diagnósticos y tratamientos a la Consulta 1
diagnostico1_1 = NodoHistorial("Diagnóstico", "Diagnóstico 1.1")
tratamiento1_1_1 = NodoHistorial("Tratamiento", "Tratamiento 1.1.1")
diagnostico1_1.agregar_evento(tratamiento1_1_1)
consulta1.agregar_evento(diagnostico1_1)

diagnostico1_2 = NodoHistorial("Diagnóstico", "Diagnóstico 1.2")
seguimiento1_2 = NodoHistorial("Seguimiento", "Seguimiento 1.2")
diagnostico1_2.agregar_evento(seguimiento1_2)
consulta1.agregar_evento(diagnostico1_2)

# Añadir diagnóstico y tratamiento a la Consulta 2
diagnostico2_1 = NodoHistorial("Diagnóstico", "Diagnóstico 2.1")
tratamiento2_1_1 = NodoHistorial("Tratamiento", "Tratamiento 2.1.1")
diagnostico2_1.agregar_evento(tratamiento2_1_1)
consulta2.agregar_evento(diagnostico2_1)

print(historial)