from ArbolAVL import ArbolAVL
from ColaPrioridad import ColaDePrioridad
from Paciente import Paciente, EventoMedico, Medicamento, Enfermedad
from GrafoHospital import GrafoHospitales
from DiagnosticoEnfermedad import DiagnosticoEnfermedad


class GestorPacientes:

    def __init__(self):
        self.arbol_pacientes = ArbolAVL()
        self.cola_prioridad = ColaDePrioridad()
        self.grafo_hospital = GrafoHospitales()
        self.diagnostico_enfermedad = DiagnosticoEnfermedad()
        self.id_contador = 0
        self.pacientes = {}

    def generar_id(self) -> int:
        self.id_contador += 1
        return self.id_contador

    def agregar_paciente(
        self,
        id: int,
        nombre: str,
        edad: int,
        gravedad: int,
        id_hospital: int,
        solicitar_datos: bool = True,
    ) -> None:
        if solicitar_datos:
            nombre_valido = False
            while not nombre_valido:
                nombre = input("Ingrese el nombre del paciente: ").strip()
                if nombre:  # Verificamos que no esté vacío
                    nombre_valido = True
                else:
                    print("El nombre del paciente no puede estar vacío.")

            edad_valida = False
            while not edad_valida:
                edad = int(input("Ingrese la edad del paciente: ").strip())
                if edad > 0:  # Verificamos que no sea negativo

                    edad_valida = True
                else:
                    print("La edad debe ser un número entero.")

            gravedad_valida = False
            while not gravedad_valida:  # Verificamos que no está vacío
                gravedad = int(input("Ingrese la gravedad del paciente: ").strip())
                if gravedad > 0:
                    gravedad_valida = True
                else:
                    print("La gravedad debe ser un número entero.")

            id_hospital_valida = False
            while not id_hospital_valida:  # Verificamos que no está vacío
                id_hospital = int(input("ID del Hospital del paciente: ").strip())
                if id_hospital > 0:
                    id_hospital_valida = True
                else:
                    print("El ID debe ser un número entero.")

        # Verificar si el paciente ya existe
        if id not in self.pacientes:
            # Genera un nuevo ID para el paciente
            id_paciente = self.generar_id()

            paciente = Paciente(id_paciente, nombre, edad, gravedad, id_hospital)

            self.pacientes[id] = paciente

            # Insertar el paciente en el árbol y la cola de prioridad
            self.arbol_pacientes.insertar(paciente)
            self.cola_prioridad.agregar(paciente)

            print(f"Paciente '{nombre}' agregado con ID {id_paciente}.")
        else:
            # Si el paciente ya existe, mostrar mensaje de error
            print(f"El Paciente con ID {id} ya existe.")

    def eliminar_paciente(self) -> None:

        # Inicializar el flag que indicará si el paciente fue eliminado
        paciente_fue_eliminado = False

        id_paciente = self.validar_id()

        # Buscar al paciente en el árbol
        nodo = self.arbol_pacientes.buscar(id_paciente)

        # Comprobar si el nodo existe
        if nodo is None:
            print(f"No se encontró el paciente con ID {id_paciente}.")
        else:
            # Obtener el paciente desde el nodo
            paciente = nodo.paciente

            # Eliminar al paciente del árbol
            if paciente:
                self.arbol_pacientes.eliminar(id_paciente)

                # Verificar si el paciente está en la cola de prioridad
                if paciente in self.cola_prioridad.buscar_entrada:
                    self.cola_prioridad.eliminar(paciente)
                    paciente_fue_eliminado = True
                    print(f"Paciente con ID {id_paciente} eliminado exitosamente.")
                else:
                    print(
                        f"Paciente con ID {id_paciente} no encontrado en la cola de prioridad."
                    )
            else:
                print(
                    f"No se pudo obtener información del paciente con ID {id_paciente}."
                )

    def modificar_paciente(self) -> None:
        # Inicializar bandera para determinar si se debe continuar con las modificaciones
        continuar = True

        # Validar que el ID ingresado sea un número entero
        id_paciente_input = input("Ingrese el ID del paciente a modificar: ").strip()
        if not id_paciente_input.isdigit():
            print("Error: El ID debe ser un número entero.")
            continuar = False

        # Si el ID es válido, buscar el paciente
        id_paciente = int(id_paciente_input) if continuar else None
        paciente = None
        if continuar:
            paciente = self.buscar_paciente(id_paciente)
            if not paciente:
                print("Paciente no encontrado.")
                continuar = False

        # Si el flujo de control no ha sido detenido, continuar con las modificaciones
        nombre = None
        edad = None
        gravedad = None
        if continuar:
            # Validar la entrada de nombre (puede estar en blanco, no es obligatorio)
            nombre = input(
                "Nuevo nombre (dejar en blanco si no se desea modificar): "
            ).strip()
            if nombre == "":
                nombre = None  # Si no se proporciona nombre, se deja como None

            # Validar la entrada de edad con una bandera booleana
            edad_valida = False
            while (
                not edad_valida
            ):  # Ciclo que se repite hasta que se ingrese un valor válido o se deje vacío
                edad_input = input(
                    "Nueva edad (dejar en blanco si no se desea modificar): "
                ).strip()
                if not edad_input:  # Si está vacío, se deja como None
                    edad = None
                    edad_valida = True  # Edad vacía es válida
                elif edad_input.isdigit():
                    edad = int(edad_input)
                    if 0 <= edad <= 150:  # Edad debe estar en el rango válido
                        edad_valida = True
                    else:
                        print("Error: La edad debe estar entre 0 y 150 años.")
                else:
                    print("Error: La edad debe ser un número entero.")

            # Validar la entrada de gravedad con una bandera booleana
            gravedad_valida = False
            while (
                not gravedad_valida
            ):  # Ciclo que se repite hasta que se ingrese un valor válido o se deje vacío
                gravedad_input = input(
                    "Nueva gravedad (dejar en blanco si no se desea modificar): "
                ).strip()
                if not gravedad_input:  # Si está vacío, se deja como None
                    gravedad = None
                    gravedad_valida = True  # Gravedad vacía es válida
                elif gravedad_input.isdigit():
                    gravedad = int(gravedad_input)
                    if gravedad >= 0:  # La gravedad debe ser un número positivo
                        gravedad_valida = True
                    else:
                        print("Error: La gravedad debe ser un número positivo.")
                else:
                    print("Error: La gravedad debe ser un número entero.")

        # Si todo es válido, proceder a actualizar los datos
        if continuar:
            # Buscar el nodo correspondiente al paciente en el árbol
            nodo = self.arbol_pacientes.buscar(id_paciente)
            if nodo:
                paciente = nodo.paciente
                # Modificar los campos si se proporcionan nuevos valores
                if nombre:
                    paciente.nombre = nombre
                if edad is not None:  # Si se proporciona una edad válida
                    paciente.edad = edad
                if gravedad is not None:  # Si se proporciona una gravedad válida
                    paciente.gravedad = gravedad
                    self.cola_prioridad.actualizar_gravedad(
                        paciente, gravedad
                    )  # Actualizar gravedad en la cola de prioridad

                print(f"Paciente con ID {id_paciente} modificado.\n")
                print("Sus nuevos datos serán:")
                print(self.buscar_paciente(id_paciente))
            else:
                print(f"No se encontró paciente con ID {id_paciente}.")

    def buscar_paciente(self, id_paciente: int = None) -> Paciente:

        if id_paciente == None:
            id_paciente = self.validar_id()

        # Buscar al paciente en el árbol
        nodo = self.arbol_pacientes.buscar(id_paciente)

        # Comprobar si el nodo existe
        if nodo is None:
            print(f"No se encontró el paciente con ID {id_paciente}.")
        else:
            # Verificar si el paciente está presente
            paciente = nodo.paciente
            if paciente:
                return paciente
            else:
                print("No se pudo obtener la información del paciente.")

    def agregar_evento_medico(self) -> None:
        tipo_es_valido = False
        detalles_valido = False

        # Validación del ID del paciente
        id_paciente = self.validar_id()

        # Validación del tipo de evento
        while not tipo_es_valido:
            tipo = input(
                "Tipo de evento (CONSULTA/DIAGNOSTICO/TRATAMIENTO): "
            ).upper()  # Convertimos a mayúsculas para evitar errores de capitalización
            if tipo in ["CONSULTA", "DIAGNOSTICO", "TRATAMIENTO"]:
                tipo_es_valido = True
            else:
                print(
                    "Tipo de evento no válido. Debe ser CONSULTA, DIAGNOSTICO o TRATAMIENTO."
                )

        # Validación de los detalles del evento
        while not detalles_valido:
            detalles = input(
                "Detalles del evento: "
            ).strip()  # Eliminamos espacios innecesarios al inicio o final
            if detalles:  # Verificamos que los detalles no estén vacíos
                detalles_valido = True
            else:
                print("Los detalles del evento no pueden estar vacíos.")

        # Buscar el paciente en el sistema
        paciente = self.buscar_paciente(id_paciente)

        if paciente:
            paciente.agregar_evento_medico(tipo, detalles)
            print(f"Evento médico agregado al paciente con ID {id_paciente}.")
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def agregar_medicamento(self) -> None:
        # Validación del ID del paciente
        id_paciente = self.validar_id()

        # Validación del nombre del medicamento
        nombre_medicamento_valido = False
        while not nombre_medicamento_valido:
            nombre_medicamento = input(
                "Nombre del medicamento: "
            ).strip()  # Eliminamos espacios en blanco al inicio y final
            if (
                nombre_medicamento
            ):  # Verificamos que el nombre del medicamento no esté vacío
                nombre_medicamento_valido = True
            else:
                print("El nombre del medicamento no puede estar vacío.")

        # Buscar el paciente en el sistema
        paciente = self.buscar_paciente(id_paciente)

        # Validar si el paciente existe y agregar el medicamento
        if paciente:
            paciente.agregar_medicamento(nombre_medicamento)
            print(
                f"Medicamento '{nombre_medicamento}' agregado al paciente con ID {id_paciente}."
            )
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def agregar_enfermedad(self) -> None:
        # Validación del ID del paciente
        id_paciente = self.validar_id()

        # Validación del nombre de la enfermedad
        nombre_enfermedad_valido = False
        while not nombre_enfermedad_valido:
            nombre_enfermedad = input(
                "Nombre de la enfermedad: "
            ).strip()  # Eliminamos espacios en blanco al inicio y final
            if (
                nombre_enfermedad
            ):  # Verificamos que el nombre de la enfermedad no esté vacío
                nombre_enfermedad_valido = True
            else:
                print("El nombre de la enfermedad no puede estar vacío.")

        # Buscar el paciente en el sistema
        paciente = self.buscar_paciente(id_paciente)

        # Validar si el paciente existe y agregar la enfermedad
        if paciente:
            paciente.agregar_enfermedad(nombre_enfermedad)
            print(
                f"Enfermedad '{nombre_enfermedad}' agregada al paciente con ID {id_paciente}."
            )
        else:
            print(f"No se encontró paciente con ID {id_paciente}.")

    def mostrar_historial_clinico(self) -> None:

        paciente = self.buscar_paciente()
        if paciente:
            print(paciente.detalle_completo())
        else:
            print(f"No se encontró paciente con ID {paciente.id_paciente}.")

    def mostrar_todos_pacientes(self) -> None:

        pacientes = self.arbol_pacientes.recorrido_inorden()
        for paciente in pacientes:
            print(paciente)

    def mostrar_cola_prioridad(self) -> None:
        if self.cola_prioridad.esta_vacia() == True:
            print("No hay pacientes en la cola de prioridad.")
        else:
            print("Pacientes en la cola de prioridad (de mayor a menor gravedad):")
            self.cola_prioridad.mostrar()

    def atender_paciente_mas_grave(self) -> None:
        paciente_atendido = (
            None  # Inicializamos el valor de retorno por defecto como None
        )

        # Validación para asegurarse de que la cola no esté vacía
        if not self.cola_prioridad.esta_vacia():
            paciente = (
                self.cola_prioridad.desacolar()
            )  # Desacolar al paciente más grave

            # Validación: Verificamos que el paciente no sea None
            if paciente:
                self.arbol_pacientes.eliminar(
                    paciente.id
                )  # Eliminamos al paciente del árbol
                paciente_atendido = paciente  # Asignamos el paciente atendido
                print(
                    f"\nPaciente atendido: {paciente_atendido.nombre} (ID: {paciente_atendido.id}, Gravedad: {paciente_atendido.gravedad})"
                )
            else:
                print("Hubo un error al obtener el paciente de la cola de prioridad.")
        else:
            print("La cola de prioridad está vacía.")  # Mensaje si la cola está vacía

    def validar_id(self) -> int:

        id_es_valido = False
        while not id_es_valido:
            id_paciente_input = input("Ingrese el ID del paciente: ")

            # Validación: Verificar que el ID sea un número entero positivo
            if id_paciente_input.isdigit():
                id_paciente = int(id_paciente_input)  # Convertir el ID a entero

                # Verificar que el ID sea positivo
                if id_paciente > 0:
                    id_es_valido = True  # ID válido, salir del bucle
                else:
                    print("El ID debe ser un número entero positivo.")
            else:
                print(
                    "El ID ingresado no es válido. Debe ser un número entero positivo."
                )

        return id_paciente  # Retorna el ID válido

    def obtener_id_hospital(self, mensaje: str, hospitales: dict) -> int:
        """
        Función para validar y obtener el ID de un hospital.
        """
        id_es_valido = False
        while not id_es_valido:
            entrada = input(mensaje)
            if entrada.isdigit():
                id_hospital = int(entrada)
                if id_hospital in hospitales:
                    id_es_valido = True
                else:
                    print(
                        f"El hospital con ID {id_hospital} no existe. Por favor ingrese un ID válido."
                    )
            else:
                print("El ID debe ser un número entero. Intente nuevamente.")

        return id_hospital

    def agregar_paso_diagnostico(self):
        id_paso = input("Ingrese el ID del paso de diagnóstico: ")
        descripcion = input("Ingrese la descripción del paso: ")
        sintomas = input(
            "Ingrese los síntomas requeridos (separados por coma) o deje en blanco: "
        ).split(",")
        sintomas = [s.strip() for s in sintomas if s.strip()]

        if not id_paso or not descripcion:
            print("Error: El ID y la descripción del paso son obligatorios.")
            return

        self.diagnostico_enfermedad.agregar_paso(id_paso, descripcion, sintomas)
        print(f"Paso de diagnóstico '{id_paso}' agregado.")

    def agregar_dependencia_diagnostico(self):
        paso_anterior = input("Ingrese el ID del paso que dependera del siguiente: ")
        paso_siguiente = input("Ingrese el ID del paso dependiende del anterior: ")

        if paso_anterior not in self.diagnostico_enfermedad.pasos:
            print(f"Error: El paso anterior '{paso_anterior}' no existe.")
            return
        if paso_siguiente not in self.diagnostico_enfermedad.pasos:
            print(f"Error: El paso siguiente '{paso_siguiente}' no existe.")
            return

        self.diagnostico_enfermedad.agregar_dependencia(paso_anterior, paso_siguiente)
        print(f"Dependencia agregada: {paso_anterior} -> {paso_siguiente}")

    def mostrar_secuencia_diagnostico(self):
        sintomas_presentes = input(
            "Ingrese los síntomas presentes (separados por coma): "
        ).split(",")
        sintomas_presentes = [s.strip() for s in sintomas_presentes if s.strip()]

        if not sintomas_presentes:
            print("Error: Debe ingresar al menos un síntoma.")
            return

        self.diagnostico_enfermedad.mostrar_secuencia_diagnostico(sintomas_presentes)

    def pacientes_ejemplos(self):
        pacientes_ejemplo = [
            {
                "id": 1,
                "nombre": "Juan Pérez",
                "edad": 30,
                "gravedad": 4,
                "id_hospital": 1,
            },  # Hospital Central
            {
                "id": 2,
                "nombre": "Ana Gómez",
                "edad": 45,
                "gravedad": 5,
                "id_hospital": 2,
            },  # Hospital San José
            {
                "id": 3,
                "nombre": "Carlos López",
                "edad": 60,
                "gravedad": 3,
                "id_hospital": 1,
            },  # Hospital Central
            {
                "id": 4,
                "nombre": "María Rodríguez",
                "edad": 25,
                "gravedad": 2,
                "id_hospital": 2,
            },  # Hospital San José
        ]

        # Agregamos los pacientes al sistema
        for paciente in pacientes_ejemplo:
            self.agregar_paciente(
                paciente["id"],
                paciente["nombre"],
                paciente["edad"],
                paciente["gravedad"],
                paciente["id_hospital"],
                solicitar_datos=False,
            )

        print("Pacientes de ejemplo agregados.\n")
