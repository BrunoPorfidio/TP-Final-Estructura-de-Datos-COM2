from collections import defaultdict

class DiagnosticoEnfermedad:
    
    def __init__(self):
        self.pasos = {}
        self.grafo = defaultdict(list)
        self.sintomas = defaultdict(list)

    def agregar_paso(self, id_paso, descripcion, sintomas_requeridos=None):
        self.pasos[id_paso] = descripcion
        if sintomas_requeridos:
            for sintoma in sintomas_requeridos:
                self.sintomas[sintoma].append(id_paso)

    def agregar_dependencia(self, paso_anterior, paso_siguiente):
        if paso_anterior in self.pasos and paso_siguiente in self.pasos:
            self.grafo[paso_anterior].append(paso_siguiente)
        else:
            print("Error: Uno o ambos pasos no existen.")

    def ordenamiento_topologico(self):
        visitado = set()
        pila = []

        def dfs(paso):
            visitado.add(paso)
            for siguiente in self.grafo[paso]:
                if siguiente not in visitado:
                    dfs(siguiente)
            pila.append(paso)

        for paso in self.pasos:
            if paso not in visitado:
                dfs(paso)

        return pila[::-1]

    def diagnosticar(self, sintomas_presentes):
        pasos_aplicables = set()
        for sintoma in sintomas_presentes:
            pasos_aplicables.update(self.sintomas[sintoma])

        secuencia_diagnostico = self.ordenamiento_topologico()
        secuencia_filtrada = [paso for paso in secuencia_diagnostico if paso in pasos_aplicables]

        return secuencia_filtrada

    def mostrar_secuencia_diagnostico(self, sintomas_presentes):
        secuencia = self.diagnosticar(sintomas_presentes)
        if secuencia:
            print("Secuencia de diagnóstico basada en los síntomas:")
            for paso in secuencia:
                print(f"- {paso}: {self.pasos[paso]}")
        else:
            print("No se ha encontrado una secuencia de diagnóstico para los síntomas dados.")