from Gestor import GestorPacientes

def main():
    gestor = GestorPacientes()
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
        print("10. Salir")
        
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
            gestor.agregar_evento_medico(id_paciente, tipo, detalles)
        elif opcion == "6":
            id_paciente = int(input("Ingrese el ID del paciente: "))
            gestor.mostrar_historial_clinico(id_paciente)
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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()