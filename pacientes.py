class Paciente:
    def __init__(self, id_medico, nombre, edad, historial_enfermedades=None, medicamentos=None):
        self.id_medico = id_medico
        self.nombre = nombre
        self.edad = edad
        self.historial_enfermedades = historial_enfermedades or []
        self.medicamentos = medicamentos or []

    def añadir_enfermedad(self, enfermedad):                                        # SE PODRIA PONER LOS METODOS EN PRIVADO
        self.historial_enfermedades.append(enfermedad)

    def eliminar_enfermedad(self, enfermedad):
        if enfermedad in self.historial_enfermedades:
            self.historial_enfermedades.remove(enfermedad)

    def añadir_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def eliminar_medicamento(self, medicamento):
        if medicamento in self.medicamentos:
            self.medicamentos.remove(medicamento)

    def modificar_datos(self, nombre=None, edad=None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
    

def buscar_termino(lista, termino, indice=0):
    if indice >= len(lista):
        return False
    if termino.lower() in lista[indice].lower():
        return True
    return buscar_termino(lista, termino, indice + 1)