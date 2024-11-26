from ArbolAVL import ArbolAVL
from ColaPrioridad import ColaPrioridad
from Paciente import Paciente, EventoMedico, Medicamento, Enfermedad
from GrafoHospital import GrafoHospitales

class GestorPacientes:
    def __init__(self):
        self.arbol_pacientes = ArbolAVL()
        self.cola_prioridad = ColaPrioridad()
        self.grafo_hospital = GrafoHospitales()
        self.id_contador = 0

    def generar_id(self):
        self.id_contador += 1
        return self.id_contador

    def agregar_paciente(self, nombre: str, edad: int, gravedad: int, id_hospital):
        id_paciente = self.generar_id()
        paciente = Paciente(id_paciente, nombre, edad, gravedad, id_hospital)
        self.arbol_pacientes.insertar(paciente)
        self.cola_prioridad.insertar(paciente)
        print(f"Paciente agregado con ID: {id_paciente}")

    def eliminar_paciente(self, id_paciente: int):
        paciente = self.arbol_pacientes.buscar(id_paciente)
        if paciente:
            self.arbol_pacientes.eliminar(id_paciente)
            self.cola_prioridad.eliminar(paciente)
            print(f"Paciente con ID {id_paciente} eliminado.")
            return True
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")
            return False

    def modificar_paciente(self, id_paciente: int, nombre: str = None, edad: int = None, gravedad: int = None):
        nodo = self.arbol_pacientes.buscar(id_paciente)
        if nodo:
            paciente = nodo.paciente
            if nombre:
                paciente.nombre = nombre
            if edad:
                paciente.edad = edad
            if gravedad:
                paciente.gravedad = gravedad
                self.cola_prioridad.actualizar(paciente, gravedad)
            print(f"Paciente con ID {id_paciente} modificado.")
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def buscar_paciente(self, id_paciente: int):
        nodo = self.arbol_pacientes.buscar(id_paciente)
        return nodo.paciente if nodo else None

    def agregar_evento_medico(self, id_paciente: int, tipo: str, detalles: str):
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            paciente.agregar_evento_medico(tipo, detalles)
            print(f"Evento médico agregado al paciente con ID {id_paciente}.")
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def agregar_medicamento(self, id_paciente: int, nombre_medicamento: str):
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            paciente.agregar_medicamento(nombre_medicamento)
            print(f"Medicamento agregado al paciente con ID {id_paciente}.")
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def agregar_enfermedad(self, id_paciente: int, nombre_enfermedad: str):
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            paciente.agregar_enfermedad(nombre_enfermedad)
            print(f"Enfermedad agregada al paciente con ID {id_paciente}.")
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def mostrar_historial_clinico(self, id_paciente: int):
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            print(paciente.detalle_completo())
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def mostrar_todos_pacientes(self):
        pacientes = self.arbol_pacientes.recorrido_inorden()
        for paciente in pacientes:
            print(paciente)

    def mostrar_cola_prioridad(self):
        if self.cola_prioridad.esta_vacia() == True:
            print("No hay pacientes en la cola de prioridad.")
        else:
            self.cola_prioridad.mostrar()
            print("Pacientes en la cola de prioridad (de mayor a menor gravedad):")


    def mostrar_ruta_optima(self, origen: str, destino: str):
        ruta = self.grafo_hospital.buscar_camino_mas_corto(origen, destino)
        if ruta:
            print(f"Ruta más corta de {origen} a {destino}: {' -> '.join(ruta)}")
        else:
            print(f"No se encontró una ruta de {origen} a {destino}.")

    def agregar_departamento(self, nombre: str):
        self.grafo_hospital.agregar_nodo(nombre)
        print(f"Departamento {nombre} agregado al hospital.")

    def conectar_departamentos(self, origen: str, destino: str, distancia: int):
        self.grafo_hospital.agregar_arista(origen, destino, distancia)
        print(f"Conexión establecida entre {origen} y {destino} con distancia {distancia}.")

    def mostrar_estructura_hospital(self):
        print("Estructura del Hospital:")
        self.grafo_hospital.mostrar_estructura()

    def buscar_pacientes_por_enfermedad(self, enfermedad: str):
        pacientes_con_enfermedad = []
        for paciente in self.arbol_pacientes.recorrido_inorden():
            if enfermedad in paciente.enfermedades:
                pacientes_con_enfermedad.append(paciente)
        return pacientes_con_enfermedad

    def estadisticas_pacientes(self):
        total_pacientes = len(self.arbol_pacientes.recorrido_inorden())
        edades = [p.edad for p in self.arbol_pacientes.recorrido_inorden()]
        edad_promedio = sum(edades) / total_pacientes if total_pacientes > 0 else 0
        gravedad_promedio = sum(p.gravedad for p in self.arbol_pacientes.recorrido_inorden()) / total_pacientes if total_pacientes > 0 else 0

        print(f"Total de pacientes: {total_pacientes}")
        print(f"Edad promedio: {edad_promedio:.2f}")
        print(f"Gravedad promedio: {gravedad_promedio:.2f}")

    def pacientes_en_rango_edad(self, edad_min: int, edad_max: int):
        return [p for p in self.arbol_pacientes.recorrido_inorden() if edad_min <= p.edad <= edad_max]

    def actualizar_prioridades(self):
        for paciente in self.arbol_pacientes.recorrido_inorden():
            nueva_prioridad = self.calcular_prioridad(paciente)
            paciente.gravedad = nueva_prioridad
            self.cola_prioridad.actualizar(paciente)

    def calcular_prioridad(self, paciente: Paciente):
        # Este es un ejemplo simple. Puedes ajustar la lógica según tus necesidades.
        prioridad_base = paciente.gravedad
        factor_edad = 1 + (paciente.edad / 100)  # Los pacientes mayores tienen prioridad ligeramente mayor
        factor_enfermedades = 1 + (len(paciente.enfermedades) * 0.1)  # Más enfermedades, mayor prioridad
        return int(prioridad_base * factor_edad * factor_enfermedades)
    
    def atender_paciente_mas_grave(self):
        if not self.cola_prioridad.esta_vacia():  # Verificamos si la cola de prioridad no está vacía
            paciente = self.cola_prioridad.desacolar()  # Usamos el método desacolar para obtener el paciente más grave
            if paciente:  # Verificamos que el paciente no sea None (en caso de que la cola estuviera vacía)
                self.arbol_pacientes.eliminar(paciente.id)  # Eliminamos al paciente del árbol de pacientes por su ID
                return paciente  # Retornamos el paciente que fue atendido
            else:
                print("No hay pacientes en la cola.")
                return None
        else:
            print("La cola de prioridad está vacía.")
            return None
    