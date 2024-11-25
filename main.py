from Gestor import GestorPacientes

def main():
    gestor = GestorPacientes()
    while True:
        print("\n--- Menú ---")
        print("1. Agregar paciente nuevo")
        print("2. Eliminar paciente")
        print("3. Modificar datos de un paciente")
        print("4. Mostrar Pacientes Registrados")
        print("5. Agregar evento médico a paciente (CONSULTA, DIAGNOSTICO O TRATAMIENTO)")
        print("6. Mostrar historial clínico de paciente")
        print("7. Buscar paciente")
        print("8. Agregar enfermedad a paciente")
        print("9. Agregar medicamento a paciente")
        print("10. Buscar medicamento o enfermedad clave")
        print("11. Mostrar cola de prioridad de pacientes")
        print("12. Atender paciente mas grave")
        print("13. Salir")
        
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
            gravedad = input("Nueva gravedad (dejar en blanco si no se desea modificar): ")
            edad = int(edad) if edad else None
            gravedad = int(gravedad) if gravedad else None
            gestor.modificar_paciente(id_paciente, nombre if nombre else None, edad, gravedad)

        elif opcion == "4":
            pacientes = gestor.arbol_pacientes.recorrido_inorden()
            for paciente in pacientes:
                print(paciente)

        elif opcion == "5":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            tipo = input("Tipo de evento (CONSULTA/DIAGNOSTICO/TRATAMIENTO): ")
            detalles = input("Detalles del evento: ")
            if tipo == "CONSULTA":
                gestor.agregar_evento_historial(id_paciente, tipo, detalles)
            elif tipo == "DIAGNOSTICO":
                id_raiz = id(paciente.historial.raiz)  # Obtener ID del evento raíz
                gestor.agregar_evento_historial(1, tipo , detalles, id_raiz)
            elif tipo == "TRATAMIENTO":
                id_diagnostico = id(paciente.historial.raiz.hijos[0])  # Obtener ID del diagnóstico
                gestor.agregar_evento_historial(1, tipo, detalles, id_diagnostico)

        elif opcion == "6":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            gestor.mostrar_historial_paciente(id_paciente)

        elif opcion == "7":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            paciente = gestor.buscar_paciente(id_paciente)
            print(paciente) if paciente else print("Paciente no encontrado.")

        elif opcion == "8":
            id_paciente = int(input("Ingrese el ID del paciente para agregar enfermedad: "))
            nombre_enfermedad = input("Nombre de la enfermedad: ")
            gestor.agregar_enfermedad(id_paciente, nombre_enfermedad)

        elif opcion == "9":
            id_paciente = int(input("Ingrese el ID del paciente para agregar medicamento: "))
            nombre_medicamento = input("Nombre del medicamento: ")
            gestor.agregar_medicamento(id_paciente, nombre_medicamento)

        elif opcion == "10":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            medicamento_a_buscar = input("Ingrese el nombre del elemento a buscar: ")
            tipo = input("Ingrese si busca una enfermedad o un medicamento: ")
            while tipo.lower() not in ["medicamento", "enfermedad"]:
                print("Tipo de búsqueda inválido. Usa 'medicamentos' o 'enfermedades'.")
                tipo = input("Ingrese si busca una enfermedad o un medicamento: ")
            gestor.buscar_en_historial(id_paciente, medicamento_a_buscar, tipo)

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()