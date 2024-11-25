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

    def agregar_paciente(self, nombre: str, edad: int, gravedad: int):
        id_paciente = self.generar_id()
        paciente = Paciente(id_paciente, nombre, edad, gravedad)
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
                self.cola_prioridad.actualizar(paciente)
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

    def buscar_en_historial(self, id: int, clave: str, tipo: str):                          #PUNTO 2
        """
        Busca recursivamente medicamentos o enfermedades clave en el historial de un paciente.
        """
        paciente = self.buscar_paciente(id)
        if not paciente:
            print(f"Paciente con ID {id} no encontrado.")
            return
        

        def buscar_recursivo(lista: list, indice=0):
            if indice >= len(lista):
                return False
            elemento = lista[indice]
            # Obtiene el nombre del medicamento o enfermedad (asegurando que sea string)
            #elemento = elemento.get_nombre() if hasattr(elemento, 'get_nombre') else str(elemento)
            # Comparación ignorando mayúsculas y minúsculas
            if clave.lower() in elemento.get_nombre().lower():
                print(f"Encontrado: {elemento.get_nombre()}, Fecha: {elemento.fecha.strftime('%d-%m-%Y')}")
                return True
            return buscar_recursivo(lista, indice + 1)

        if tipo == "medicamento":
            encontrado = buscar_recursivo(paciente.medicamentos)
            if not encontrado:
                print(f"No se encontró ninguna coincidencia con la clave '{clave}' en {tipo}s.")
        else:
            encontrado = buscar_recursivo(paciente.enfermedades)
            if not encontrado:
                print(f"No se encontró ninguna coincidencia con la clave '{clave}' en {tipo}es.")




    def agregar_evento_historial(self, id: int, tipo: str, descripcion: str, id_padre: int = None):
        """
        Agrega un evento médico al historial clínico de un paciente.
        Si no se especifica un ID de padre, el evento se agrega como raíz.
        """
        paciente = self.buscar_paciente(id)
        if not paciente:
            print(f"Paciente con ID {id} no encontrado.")
            return

        nuevo_evento = EventoMedico(tipo, descripcion)

        if id_padre is None:
            if paciente.historial.raiz is None:
                paciente.historial.agregar_evento(nuevo_evento)  # Agregar como raíz
            else:
                print("El historial ya tiene una raíz. Especifica un evento padre para continuar.")
        else:
            # Buscar el evento padre en el historial
            evento_padre = self._buscar_evento_por_id(paciente.historial.raiz, id_padre)
            if not evento_padre:
                print(f"Evento padre con ID {id_padre} no encontrado.")
                return
            paciente.historial.agregar_evento(nuevo_evento, evento_padre)  # Agregar como hijo

        print(f"Evento '{tipo}' agregado al historial del paciente {paciente.nombre}.")

    def mostrar_historial_paciente(self, id: int):
        """
        Muestra el historial clínico completo de un paciente.
        """
        paciente = self.buscar_paciente(id)
        if not paciente:
            print(f"Paciente con ID {id} no encontrado.")
            return

        print(f"Historial clínico del paciente {paciente.nombre}:")
        paciente.historial.mostrar_historial()


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
        self.cola_prioridad.mostrar()

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
        if not self.cola_prioridad.esta_vacia():
            paciente = self.cola_prioridad.extraer_maximo()  # Cambiar a extraer_maximo
            self.arbol_pacientes.eliminar(paciente.id)  # Asegúrate de eliminar por ID
            return paciente
        return None
    
    def mostrar_cola_prioridad(self):
        print("Pacientes en la cola de prioridad (de mayor a menor gravedad):")
        self.cola_prioridad.mostrar()  # Llama al método mostrar de ColaPrioridad


    