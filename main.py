from Gestor import GestorPacientes
from GrafoHospital import (
    GrafoHospitales
)


def main():
    gestor = GestorPacientes()
    grafo_hospitales = GrafoHospitales()  # Instancia de GrafoHospitales
    id_hospital = 1  # Contador para asignar ID a los hospitales

#---------------------------------------------------------------------------------------------------------------

    grafo_hospitales.agregar_hospital(1, "Hospital A", "Cardiología")
    id_hospital +=1
    grafo_hospitales.agregar_hospital(2, "Hospital B", "Neurología")
    id_hospital +=1
    grafo_hospitales.agregar_hospital(3, "Hospital C", "Pediatría")
    id_hospital +=1
    grafo_hospitales.agregar_hospital(4, "Hospital D", "Traumatología")
    id_hospital +=1
    grafo_hospitales.agregar_hospital(5, "Hospital E", "Ginecología")
    id_hospital +=1
    print("Hospitales de ejemplo agregados.\n")

    # Agregar conexiones entre hospitales
    grafo_hospitales.agregar_conexion(1, 2, 10)  # Hospital A <-> Hospital B
    grafo_hospitales.agregar_conexion(2, 3, 15)  # Hospital B <-> Hospital C
    grafo_hospitales.agregar_conexion(3, 4, 20)  # Hospital C <-> Hospital D
    grafo_hospitales.agregar_conexion(4, 5, 25)  # Hospital D <-> Hospital E
    grafo_hospitales.agregar_conexion(1, 5, 30)  # Hospital A <-> Hospital E


    pacientes_ejemplo = [
        {"nombre": "Juan Pérez", "edad": 30, "gravedad": 4, "id_hospital": "1"},  # Hospital Central
        {"nombre": "Ana Gómez", "edad": 45, "gravedad": 5, "id_hospital": "2"},  # Hospital San José
        {"nombre": "Carlos López", "edad": 60, "gravedad": 3, "id_hospital": "1"},  # Hospital Central
        {"nombre": "María Rodríguez", "edad": 25, "gravedad": 2, "id_hospital": "2"},  # Hospital San José
    ]
    
    # Agregamos los pacientes al sistema
    for paciente in pacientes_ejemplo:
        gestor.agregar_paciente(
            paciente["nombre"], 
            paciente["edad"], 
            paciente["gravedad"], 
            paciente["id_hospital"]
        )
    
    print("Pacientes de ejemplo agregados.\n")
#---------------------------------------------------------------------------------------------------------------------

    sigue_eligiendo = True

    while sigue_eligiendo:
        print("\n" + "=" * 80)
        print("{:^80}".format("SISTEMA DE GESTIÓN HOSPITALARIA"))
        print("=" * 80)

        categorias = {
            "Gestión de Pacientes": [
                "Agregar paciente nuevo",
                "Eliminar paciente",
                "Modificar datos de un paciente",
                "Mostrar Pacientes Registrados",
                "Buscar paciente",
                "Mostrar cola de prioridad de pacientes",
                "Atender al paciente más grave"
            ],
            "Historial Médico": [
                "Agregar evento médico a paciente",
                "Mostrar historial clínico de paciente",
                "Agregar enfermedad a paciente",
                "Agregar medicamento a paciente"
            ],
            "Gestión de Hospitales": [
                "Agregar hospital",
                "Agregar conexión entre hospitales",
                "Buscar hospital",
                "Mostrar todos los hospitales"
            ],
            "Rutas y Navegación": [
                "Mostrar ruta óptima entre departamentos",
                "Mostrar mejor ruta de ambulancia",
                "Encontrar ruta usando BFS",
                "Encontrar ruta usando DFS"
            ]
        }

        opcion_counter = 1
        for categoria, opciones in categorias.items():
            print(f"\n{categoria}:")
            print("-" * 80)
            for opcion in opciones:
                print(f"│ {opcion_counter:2}. {opcion:<74} │")
                opcion_counter += 1

        print("\n" + "-" * 80)
        print(f"│ {opcion_counter:2}. {'Salir':<74} │")
        print("=" * 80)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            gravedad = int(input("Gravedad del paciente (1-5): "))
            grafo_hospitales.mostrar_hospitales()
            id_hospital_paciente = input("ID del Hospital del paciente: ")
            gestor.agregar_paciente(nombre, edad, gravedad, id_hospital_paciente)

        elif opcion == "2":
            id_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
            if gestor.eliminar_paciente(id_paciente):
                print("Paciente eliminado.")
            else:
                print("Paciente no encontrado.")

        elif opcion == "3":
            id_paciente = int(input("Ingrese el ID del paciente a modificar: "))
            paciente = gestor.buscar_paciente(id_paciente)
            print(paciente) if paciente else print("Paciente no encontrado.")
            nombre = input("Nuevo nombre (dejar en blanco si no se desea modificar): ")
            edad = input("Nueva edad (dejar en blanco si no se desea modificar): ")
            gravedad = input(
                "Nueva gravedad (dejar en blanco si no se desea modificar): "
            )
            edad = int(edad) if edad else None
            gravedad = int(gravedad) if gravedad else None
            gestor.modificar_paciente(
                id_paciente, nombre if nombre else None, edad, gravedad
            )
            print(gestor.buscar_paciente(id_paciente))

        elif opcion == "4":
            pacientes = gestor.mostrar_todos_pacientes()

        elif opcion == "5":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            tipo = input("Tipo de evento (CONSULTA/DIAGNOSTICO/TRATAMIENTO): ")
            detalles = input("Detalles del evento: ")
            gestor.agregar_evento_medico(id_paciente, tipo, detalles)

        elif opcion == "6":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            gestor.mostrar_historial_clinico(id_paciente)

        elif opcion == "7":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            paciente = gestor.buscar_paciente(id_paciente)
            print(paciente) if paciente else print("Paciente no encontrado.")
            
        elif opcion == "8":
            id_paciente = int(
                input("Ingrese el ID del paciente para agregar enfermedad: ")
            )
            nombre_enfermedad = input("Nombre de la enfermedad: ")
            gestor.agregar_enfermedad(id_paciente, nombre_enfermedad)

        elif opcion == "9":
            id_paciente = int(
                input("Ingrese el ID del paciente para agregar medicamento: ")
            )
            nombre_medicamento = input("Nombre del medicamento: ")
            gestor.agregar_medicamento(id_paciente, nombre_medicamento)

        elif opcion == "10":
            gestor.mostrar_cola_prioridad()

        elif opcion == "11":
            origen = int(input("Ingrese el hospital de origen: "))
            destino = int(input("Ingrese el hospital de destino: "))
            grafo_hospitales.mejor_ruta_ambulancia(origen, destino)

        elif opcion == "12":

            paciente_atendido = gestor.atender_paciente_mas_grave()
            if paciente_atendido:
                print(f"\nPaciente atendido: {paciente_atendido.nombre} (ID: {paciente_atendido.id}, Gravedad: {paciente_atendido.gravedad})")
            else:
                print("No hay pacientes en espera para atender.")

        elif opcion == "13":
            nombre_hospital = input("Ingrese el nombre del hospital a agregar: ")
            especialidad = input("Ingrese la especialidad del hospital: ")
            grafo_hospitales.agregar_hospital(id_hospital, nombre_hospital, especialidad)
            print(f"Hospital '{nombre_hospital}' agregado.")
            id_hospital += 1  # Incrementar el ID para el próximo hospital
            
        elif opcion == "14":

            grafo_hospitales.mostrar_hospitales()
            hospital1 = int(input("Ingrese el ID del primer hospital: "))
            hospital2 = int(input("Ingrese el ID del segundo hospital: "))
            distancia = int(input("Ingrese la distancia (en KM) entre los hospitales: "))
            grafo_hospitales.agregar_conexion(hospital1, hospital2, distancia)

        elif opcion == "15":
            print("---------------------------------------------")
            print("Lista de hospitales: \n")
            for hospital in grafo_hospitales.hospitales.values():

                print(hospital)

            print("---------------------------------------------")

        elif opcion == "16":

            # Solicitar los IDs de los hospitales de origen y destino
            grafo_hospitales.mostrar_hospitales()
            try:
                origen = int(input("Ingrese el ID del hospital de origen para BFS: "))
                destino = int(input("Ingrese el ID del hospital de destino para BFS: "))
            except ValueError:
                print("Por favor ingrese un ID válido (un número entero).")
                return
            
            # Llamar a la función BFS utilizando los IDs
            ruta_bfs = grafo_hospitales.bfs(origen, destino)
            
            # Mostrar el resultado de la búsqueda
            if ruta_bfs:
                print(f"La ruta encontrada por BFS desde el hospital con ID {origen} hasta el hospital con ID {destino} es:")
                print(" -> ".join(str(grafo_hospitales.hospitales[hospital_id].nombre) for hospital_id in ruta_bfs))
            else:
                print(f"No se encontró una ruta desde el hospital con ID {origen} a {destino}.")

        elif opcion == "17":

            grafo_hospitales.mostrar_hospitales()
            # Solicitar al usuario los IDs de los hospitales en lugar de los nombres
            origen_id = int(input("Ingrese el ID del hospital de origen para DFS: "))
            destino_id = int(input("Ingrese el ID del hospital de destino para DFS: "))
            
            # Llamada al método DFS usando los IDs de los hospitales
            ruta_dfs = grafo_hospitales.dfs(origen_id, destino_id)
            
            if ruta_dfs:
                print(f"La ruta encontrada por DFS desde el hospital con ID {origen_id} hasta el hospital con ID {destino_id} es:")
                # Mostrar la ruta usando los nombres de los hospitales correspondientes a los IDs
                print(" -> ".join(str(grafo_hospitales.hospitales[hospital_id].nombre) for hospital_id in ruta_dfs))
            else:
                print(f"No se encontró una ruta desde el hospital con ID {origen_id} a {destino_id}.")

        elif opcion == "28":
            print("Saliendo del sistema...")
            sigue_eligiendo = False

        else:
            print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()