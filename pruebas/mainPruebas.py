from ARBOL_avl import ArbolAVL
from pacientes import Paciente

id_totales = 0

arbol = ArbolAVL()
raiz = None

# Insertar pacientes
#paciente1 = Paciente(1, "Juan Perez", 45)
#paciente2 = Paciente(2, "Ana Gomez", 30)
#paciente3 = Paciente(3, "Carlos Ruiz", 60)

#raiz = arbol.insertar(raiz, paciente1)
#raiz = arbol.insertar(raiz, paciente2)
#raiz = arbol.insertar(raiz, paciente3)



print(f"Opcion 1 = Agregar")
print(f"Opcion 2 = Eliminar")
print(f"Opcion 3 = Modificar")
respuesta = input("Elija una opcion: 1/2/3")

if respuesta != "1" or "2" or "3":
    TypeError


if respuesta == "1":
    id_a_agregar = id_totales + 1
    id_totales = id_a_agregar
    nombre = input(f"Ingrese el nombre del paciente: ")
    edad = input(f"Ingrese la edad del paciente: ")
    paciente1 = Paciente(id_a_agregar, nombre, edad)
    posee_enfermedad = input(f"¿El paciente posee alguna enfermedad?: (s/n)")
    if posee_enfermedad.lower() != "s" or "n":
        TypeError
    elif posee_enfermedad.lower() == "s":
        añade_enfermedades = True
        while añade_enfermedades:
            nueva_enfermedad = input(f"Ingrese la enfermedad a añadir: ")
            paciente1.añadir_enfermedad(nueva_enfermedad)
            respuesta = input(f"¿Desea añadir mas enfermedades?: s/n")
            if respuesta != "s" or "n":
                TypeError
            elif respuesta == "n":
                añade_enfermedades = False
            




elif respuesta == "2":

    id_a_buscar = input(f"Ingrese el ID del paciente a eliminar: ")
    paciente_encontrado = arbol.buscar(raiz, id_a_buscar)

    if paciente_encontrado:
        print(f"Paciente encontrado: {paciente_encontrado}")
    else:
        print(f"No se encontró un paciente con el ID {id_a_buscar}.")
    
elif respuesta == "3":

    id_a_buscar = input(f"Ingrese el ID del paciente a modificar: ")
    paciente_encontrado = arbol.buscar(raiz, id_a_buscar)

    if paciente_encontrado:                                                                     # EDITAR RESPUESTAS 2 Y 3
        print(f"Paciente encontrado: {paciente_encontrado}")                                    # FALTA QUE LA 2 ELIMINE AL PACIENTE, Y EN LA 3
    else:                                                                                       # FALTA PREGUNTAR QUE QUIERE MODIFICAR, Y QUE LO MODIFIQUE
        print(f"No se encontró un paciente con el ID {id_a_buscar}.")




# Buscar paciente
nodo = arbol.buscar(raiz, 2)
if nodo:
    print(f"Paciente encontrado: {nodo.paciente}")

# Eliminar paciente
raiz = arbol.eliminar(raiz, 2)