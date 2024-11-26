from Gestor import GestorPacientes
from GrafoHospital import (
    GrafoHospitales,
    Hospital,
)


def main():
    gestor = GestorPacientes()
    grafo_hospitales = GrafoHospitales()  # Instancia de GrafoHospitales
    id_hospital = 1  # Contador para asignar ID a los hospitales

    while True:
        print("\n--- Menú ---")
        print("1. Agregar paciente nuevo")
        print("2. Eliminar paciente")
        print("3. Modificar datos de un paciente")
        print("4. Mostrar Pacientes Registrados")
        print("5. Agregar evento médico a paciente")
        print("6. Mostrar historial clínico de paciente")
        print("7. Buscar paciente")
        print("8. Agregar enfermedad a paciente")
        print("9. Agregar medicamento a paciente")
        print("10. Mostrar cola de prioridad de pacientes")
        print("11. Mostrar ruta óptima entre departamentos")
        print("12. Atender al paciente más grave")
        print("13. Agregar hospital")
        print("14. Agregar conexión entre hospitales")
        print("15. Mostrar mejor ruta de ambulancia")
        print("16. Buscar hospital")
        print("17. Mostrar todos los hospitales")
        print("18. Encontrar ruta usando BFS")
        print("19. Encontrar ruta usando DFS")
        print("20. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            gravedad = int(input("Gravedad del paciente (1-5): "))
            gestor.agregar_paciente(nombre, edad, gravedad)

        elif opcion == "2":
            id_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
            if gestor.eliminar_paciente(id_paciente):
                print("Paciente eliminado.")
            else:
                print("Paciente no encontrado.")

        elif opcion == "3":
            id_paciente = int(input("Ingrese el ID del paciente a modificar: "))
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

        elif opcion == "4":
            pacientes = gestor.mostrar_todos_pacientes()
            for paciente in pacientes:
                print(paciente)

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
            pacientes = gestor.mostrar_cola_prioridad()
            if pacientes:
                print("Pacientes en la cola de prioridad (de mayor a menor gravedad):")
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No hay pacientes en la cola de prioridad.")

        elif opcion == "11":
            origen = input("Ingrese el departamento de origen: ")
            destino = input("Ingrese el departamento de destino: ")
            gestor.mostrar_ruta_optima(origen, destino)

        elif opcion == "12":
            paciente_atendido = gestor.atender_paciente_mas_grave()
            if paciente_atendido:
                print(f"Se ha atendido al paciente más grave: {paciente_atendido}")
            else:
                print("No hay pacientes en espera para atender.")

        elif opcion == "13":
            nombre_hospital = input("Ingrese el nombre del hospital a agregar: ")
            especialidades = input(
                "Ingrese las especialidades del hospital (separadas por comas): "
            ).split(",")
            grafo_hospitales.agregar_hospital(
                id_hospital, nombre_hospital, [esp.strip() for esp in especialidades]
            )
            print(f"Hospital '{nombre_hospital}' agregado.")
            id_hospital += 1  # Incrementar el ID para el próximo hospital
            
        elif opcion == "14":
            hospital1 = input("Ingrese el nombre del primer hospital: ")
            hospital2 = input("Ingrese el nombre del segundo hospital: ")
            distancia = int(input("Ingrese la distancia entre los hospitales: "))
            grafo_hospitales.agregar_conexion(hospital1, hospital2, distancia)
            print(
                f"Conexión entre '{hospital1}' y '{hospital2}' agregada con distancia {distancia}."
            )

        elif opcion == "15":
            origen = input("Ingrese el hospital de origen: ")
            destino = input("Ingrese el hospital de destino: ")
            grafo_hospitales.mejor_ruta_ambulancia(origen, destino)

        elif opcion == "16":
            nombre_hospital = input("Ingrese el nombre del hospital a buscar: ")
            if nombre_hospital in grafo_hospitales.hospitales:
                print(grafo_hospitales.hospitales[nombre_hospital])
            else:
                print(f"El hospital '{nombre_hospital}' no se encuentra en el sistema.")

        elif opcion == "17":
            print("Lista de hospitales:")
            for hospital in grafo_hospitales.hospitales.values():
                print(hospital)

        elif opcion == "18":
            origen = input("Ingrese el hospital de origen para BFS: ")
            destino = input("Ingrese el hospital de destino para BFS: ")
            ruta_bfs = grafo_hospitales.bfs(origen, destino)
            if ruta_bfs:
                print(f"La ruta encontrada por BFS desde {origen} hasta {destino} es:")
                print(" -> ".join(ruta_bfs))
            else:
                print(f"No se encontró una ruta desde {origen} a {destino}.")

        elif opcion == "19":
            origen = input("Ingrese el hospital de origen para DFS: ")
            destino = input("Ingrese el hospital de destino para DFS: ")
            ruta_dfs = grafo_hospitales.dfs(origen, destino)
            if ruta_dfs:
                print(f"La ruta encontrada por DFS desde {origen} hasta {destino} es:")
                print(" -> ".join(ruta_dfs))
            else:
                print(f"No se encontró una ruta desde {origen} a {destino}.")

        elif opcion == "20":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
