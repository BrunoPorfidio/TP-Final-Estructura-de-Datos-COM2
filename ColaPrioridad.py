import heapq
from Paciente import Paciente

class ColaDePrioridad:
    
    def __init__(self):
        self.heap = []  # Lista de pacientes organizada por prioridad
        self.buscar_entrada = {}  # Mapeo de pacientes a sus entradas en la cola
        self.PACIENTE_ELIMINADO = '<paciente-eliminado>'  # Marcador de paciente eliminado
        self.contador = 0  # Contador único para el orden de inserción

    def agregar(self, paciente: Paciente):
        """Inserta un paciente en la cola de prioridad."""
        if paciente in self.buscar_entrada:
            self.eliminar(paciente)
        conteo = self.contador
        entrada = [-paciente.gravedad, conteo, paciente]  # Prioridad negativa para max-heap
        self.buscar_entrada[paciente] = entrada
        heapq.heappush(self.heap, entrada)
        self.contador += 1

    def eliminar(self, paciente: Paciente):

        """Elimina un paciente de la cola de prioridad."""
        if paciente in self.buscar_entrada:
            # Obtener la entrada del paciente en el diccionario
            entrada = self.buscar_entrada.pop(paciente)
            
            # Marca el paciente como eliminado (de forma lógica)
            entrada[-1] = self.PACIENTE_ELIMINADO  
            
            # Es necesario reorganizar el heap para que el paciente "eliminado" sea removido correctamente
            heapq.heapify(self.heap)  # Reorganiza el heap

    def actualizar_gravedad(self, paciente: Paciente, nueva_gravedad: int):
        """Actualiza la gravedad de un paciente en la cola."""
        self.eliminar(paciente)
        paciente.gravedad = nueva_gravedad
        self.agregar(paciente)

    def esta_vacia(self):
        """Verifica si la cola de prioridad está vacía."""
        return not self.buscar_entrada

    def cantidad(self) -> int:
        """Retorna la cantidad de pacientes en la cola de prioridad."""
        return len(self.buscar_entrada)

    def mostrar(self):
        """Muestra los pacientes ordenados por gravedad en la cola."""
        if not self.heap:  # Verifica si la cola está vacía
            print("No hay pacientes en la cola de prioridad.")
            return
        # Ordena la lista de pacientes en función de su gravedad
        pacientes_ordenados = sorted(self.buscar_entrada.keys(), key=lambda p: -p.gravedad)
    
        for paciente in pacientes_ordenados:
            print(f"Gravedad: {paciente.gravedad}, ID: {paciente.id}, Nombre: {paciente.nombre}")

    def desacolar(self):
        """Elimina y retorna el paciente con mayor gravedad (prioridad)."""
        while self.heap:
            # Extraemos el paciente con mayor gravedad
            prioridad, conteo, paciente = heapq.heappop(self.heap)
            # Si el paciente no ha sido eliminado, lo retornamos
            if paciente != self.PACIENTE_ELIMINADO:
                del self.buscar_entrada[paciente]
                return paciente
        # Si la cola está vacía
        print("La cola de prioridad está vacía.")
        return None