from pacientes import Paciente
from ARBOL_avl import ArbolAVL

class MenuPacientes:
    def __init__(self):
        self.arbol = ArbolAVL()  # Instancia del árbol AVL.
        self.raiz = None  # Raíz del árbol.

    def menu(self):
        while True:
            # Mostrar opciones del menú.
            print("\n--- Menú de Gestión de Pacientes ---")
            print("1. Añadir/Dar de alta a un paciente")
            print("2. Eliminar un paciente")
            print("3. Modificar datos de un paciente")
            print("4. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.añadir_paciente()
            elif opcion == "2":
                self.eliminar_paciente()
            elif opcion == "3":
                self.modificar_paciente()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")

    def añadir_paciente(self):
        print("\n--- Añadir Paciente ---")
        id_medico = int(input("ID Médico: "))
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        historial = input("Historial de enfermedades (separadas por coma): ").split(", ")
        medicamentos = input("Medicamentos actuales (separados por coma): ").split(", ")

        nuevo_paciente = Paciente(id_medico, nombre, edad, historial, medicamentos)
        self.raiz = self.arbol.insertar(self.raiz, nuevo_paciente)
        print("Paciente añadido exitosamente.")

    def eliminar_paciente(self):
        print("\n--- Eliminar Paciente ---")
        id_medico = int(input("Ingresa el ID Médico del paciente a eliminar: "))
        self.raiz = self.arbol.eliminar(self.raiz, id_medico)
        print("Paciente eliminado exitosamente (si existía).")

    def modificar_paciente(self):
        print("\n--- Modificar Paciente ---")
        id_medico = int(input("Ingresa el ID Médico del paciente a modificar: "))
        nodo = self.arbol.buscar(self.raiz, id_medico)

        if nodo:
            paciente = nodo.paciente
            print(f"\nPaciente encontrado:\n{paciente}")

            # Modificar los datos del paciente.
            nombre = input(f"Nuevo nombre (actual: {paciente.nombre}): ") or paciente.nombre
            edad = input(f"Nueva edad (actual: {paciente.edad}): ") or paciente.edad
            historial = input(f"Nuevo historial (actual: {', '.join(paciente.historial)}): ").split(", ") or paciente.historial
            medicamentos = input(f"Nuevos medicamentos (actual: {', '.join(paciente.medicamentos)}): ").split(", ") or paciente.medicamentos

            # Actualizar los datos del paciente.
            paciente.nombre = nombre
            paciente.edad = int(edad)
            paciente.historial = historial
            paciente.medicamentos = medicamentos

            print("Datos del paciente modificados exitosamente.")
        else:
            print("Paciente no encontrado.")

# Programa principal.
if __name__ == "__main__":
    menu = MenuPacientes()
    menu.menu()