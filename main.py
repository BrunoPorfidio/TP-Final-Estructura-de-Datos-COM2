from Gestor import GestorPacientes
from GrafoHospital import GrafoHospitales


def main():
    gestor = GestorPacientes()
    grafo_hospitales = GrafoHospitales()  # Instancia de GrafoHospitales
    gestor.pacientes_ejemplos()  # Llama al método para agregar pacientescon datos estaticos
    grafo_hospitales.hospitales_ejemplos()  # Llama al método para agregar hospitales y conexiones con datos estaticos
    grafo_hospitales.conexiones_ejemplos()  # Llama al método para agregar conexiones de hospitales con datos estaticos

    sigue_eligiendo = True

    while sigue_eligiendo:
        print("\n" + "=" * 80)
        print("{:^80}".format("SISTEMA DE GESTIÓN HOSPITALARIA"))
        print("=" * 80)

        categorias = {
            "Gestión de Pacientes": [
                " Agregar paciente nuevo",
                " Eliminar paciente",
                " Modificar datos de un paciente",
                " Mostrar Pacientes Registrados",
                " Buscar paciente", 
                " Mostrar cola de prioridad de pacientes", 
                " Atender al paciente más grave" 
            ],
            "Historial Médico": [
                " Agregar evento médico a paciente", 
                " Mostrar historial clínico de paciente", 
                " Agregar enfermedad a paciente", 
                " Agregar medicamento a paciente" 
            ],
            "Gestión de Hospitales": [
                " Agregar hospital", 
                " Agregar conexión entre hospitales", 
                " Mostrar todos los hospitales" 
            ],
            "Rutas y Navegación": [
                " Mostrar mejor ruta de ambulancia", 
                " Encontrar ruta usando BFS", 
                " Encontrar ruta usando DFS" 
            ],
            "Diagnóstico de Enfermedad": [
                " Agregar paso de diagnóstico",
                " Agregar dependencia entre pasos",
                " Mostrar secuencia de diagnóstico"
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

        if opcion == "1":                       # YA VALIDADO
            gestor.agregar_paciente()

        elif opcion == "2":                     # YA VALIDADO
            gestor.eliminar_paciente()     

        elif opcion == "3":                     # YA VALIDADO
            gestor.modificar_paciente()

        elif opcion == "4":                     # NO REQUIERE VALIDACION, SOLO ES MOSTRAR PACIENTES
            gestor.mostrar_todos_pacientes()

        elif opcion == "5":                     # YA VALIDADO
            paciente = gestor.buscar_paciente()
            print(paciente)

        elif opcion == "6":                     # NO REQUIERE VALIDACION, SOLO ES MOSTRAR COLA DE PRIORIDAD
            gestor.mostrar_cola_prioridad()

        elif opcion == "7":                     # YA VALIDADO
            gestor.atender_paciente_mas_grave()

        elif opcion == "8":                     # YA VALIDADO
            gestor.agregar_evento_medico()

        elif opcion == "9":                     # YA VALIDADO
            gestor.mostrar_historial_clinico()
            
        elif opcion == "10":                    # YA VALIDADO
            gestor.agregar_enfermedad()

        elif opcion == "11":                    # YA VALIDADO
            gestor.agregar_medicamento()

        elif opcion == "12":                    # YA VALIDADO
            grafo_hospitales.agregar_hospital()
            
        elif opcion == "13":                    # YA VALIDADO
            grafo_hospitales.agregar_conexion()

        elif opcion == "14":                    # NO REQUIERE VALIDACION, SOLO ES MOSTRAR LOS HOSPITALES
            grafo_hospitales.mostrar_hospitales()

        elif opcion == "15":                    # YA VALIDADO
            grafo_hospitales.mejor_ruta_ambulancia()

        elif opcion == "16":                    # YA VALIDADO

            # Mostrar los hospitales disponibles
            grafo_hospitales.mostrar_hospitales()
            origen = gestor.obtener_id_hospital("Ingrese el ID del hospital de origen para BFS: ", grafo_hospitales.hospitales)
            destino = gestor.obtener_id_hospital("Ingrese el ID del hospital de destino para BFS: ", grafo_hospitales.hospitales)
            # Llamar a la función BFS utilizando los IDs de los hospitales
            ruta_bfs = grafo_hospitales.bfs(origen, destino)

            # Mostrar el resultado de la búsqueda
            if ruta_bfs:
                print(f"La ruta encontrada por BFS desde el hospital con ID {origen} hasta el hospital con ID {destino} es:")
                print(" -> ".join(str(grafo_hospitales.hospitales[hospital_id].nombre) for hospital_id in ruta_bfs))
            else:
                print(f"No se encontró una ruta desde el hospital con ID {origen} a {destino}.")

        elif opcion == "17":                    # YA VALIDADO

            # Mostrar los hospitales disponibles
            grafo_hospitales.mostrar_hospitales()
            origen = gestor.obtener_id_hospital("Ingrese el ID del hospital de origen para DFS: ", grafo_hospitales.hospitales)
            destino = gestor.obtener_id_hospital("Ingrese el ID del hospital de destino para DFS: ", grafo_hospitales.hospitales)

            # Llamar a la función DFS utilizando los IDs de los hospitales
            ruta_dfs = grafo_hospitales.dfs(origen, destino)

            # Mostrar el resultado de la búsqueda
            if ruta_dfs:
                print(f"La ruta encontrada por DFS desde el hospital con ID {origen} hasta el hospital con ID {destino} es:")
                # Mostrar la ruta usando los nombres de los hospitales correspondientes a los IDs
                print(" -> ".join(str(grafo_hospitales.hospitales[hospital_id].nombre) for hospital_id in ruta_dfs))
            else:
                print(f"No se encontró una ruta desde el hospital con ID {origen} a {destino}.")

        elif opcion == "18":
            gestor.agregar_paso_diagnostico() 

        elif opcion == "19":
            gestor.agregar_dependencia_diagnostico()

        elif opcion == "20":
            gestor.mostrar_secuencia_diagnostico()

        elif opcion == "21":
            print("Saliendo del sistema...")
            sigue_eligiendo = False


        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()