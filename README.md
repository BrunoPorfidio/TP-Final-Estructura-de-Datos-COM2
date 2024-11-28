# TP Final Estructura de Datos Com2. UNAB: Sistema de Gestión de Datos Medicos.

## Descripción del Proyecto
Este proyecto es un sistema de gestión hospitalaria desarrollado en Python. Permite la administración de pacientes, hospitales y la gestión de eventos médicos, medicamentos y enfermedades. El sistema está diseñado para facilitar la interacción entre los hospitales y los pacientes, así como para optimizar la atención médica a través de la gestión de la gravedad de los pacientes y la búsqueda de rutas entre hospitales.

## Finalidad
La finalidad de este proyecto es:
- **Gestión de Pacientes**: Permitir el registro, modificación y eliminación de pacientes, así como el seguimiento de su historial médico.
- **Gestión de Hospitales**: Administrar la información de los hospitales y sus especialidades, así como las conexiones entre ellos.
- **Navegación**: Proporcionar rutas óptimas para ambulancias entre hospitales utilizando algoritmos de búsqueda.

## Estructura del Proyecto
El proyecto está compuesto por varios módulos, cada uno con una responsabilidad específica:

- **Main.py**: Punto de entrada del sistema, donde se gestionan las interacciones del usuario.
- **Paciente.py**: Define la clase `Paciente`, que representa a un paciente y su historial médico.
- **Enfermedad.py**: Define la clase `Enfermedad`, que representa las enfermedades de un paciente.
- **Medicamento.py**: Define la clase `Medicamento`, que representa los medicamentos prescritos a un paciente.
- **EventoMedico.py**: Define la clase `EventoMedico`, que representa los eventos médicos registrados para un paciente.
- **Hospital.py**: Define la clase `Hospital`, que representa un hospital y sus conexiones con otros hospitales.
- **GrafoHospital.py**: Implementa la estructura de datos para gestionar hospitales y sus conexiones, así como algoritmos de búsqueda.
- **ArbolAVL.py**: Implementa un árbol AVL para gestionar pacientes de manera balanceada.
- **ColaPrioridad.py**: Implementa una cola de prioridad para gestionar pacientes según su gravedad.
- **DiagnosticoEnfermedad.py**: Gestiona los pasos de diagnóstico y sus dependencias.
- **Gestor.py**: Coordina las operaciones de gestión de pacientes, hospitales y diagnósticos.

## Ejemplo de Uso
A continuación se presentan algunos ejemplos de cómo utilizar el sistema:

## Gestión de Pacientes

### Opcion 1: Agregar un Paciente.
```
Ingrese el nombre del paciente: Juan Pérez
  Ingrese la edad del paciente: 30
  Ingrese la gravedad del paciente (1-5): 4
  Ingrese el ID del hospital: 1
```
#### Respuesta:
```
Paciente agregado con ID: 1
```

### Opcion 2: Eliminar Paciente.
```
Ingrese el ID del paciente a eliminar: 1
```
#### Respuesta:
```
Paciente con ID 1 eliminado exitosamente.
```

### Opcion 3: Modificar datos de un Paciente.
```
Ingrese el ID del paciente a modificar: 1
Nuevo nombre (dejar en blanco si no se desea modificar): Juan Carlos
Nueva edad (dejar en blanco si no se desea modificar): 31
Nueva gravedad (dejar en blanco si no se desea modificar): 5
```
#### Respuesta:
```
Paciente con ID 1 modificado.
```

### Opcion 4: Mostrar pacientes Registrados.
```
Lista de pacientes:
·ID: 1
 Nombre: Juan Pérez
 Edad: 30
 Gravedad: 4
 ID de hospital actual: 1

·ID: 2
 Nombre: Ana Gómez
 Edad: 45
 Gravedad: 3
 ID de hospital actual: 2

·ID: 3
 Nombre: Carlos López
 Edad: 60
 Gravedad: 5
 ID de hospital actual: 1
```

### Opcion 5: Buscar paciente por ID.
```
Ingrese el ID del paciente a buscar: 1
```
#### Respuesta:
```
Paciente encontrado:
·ID: 1
 Nombre: Juan Pérez
 Edad: 30
 Gravedad: 4
 ID de hospital actual: 1
```

### Opcion 6: Mostrar cola de prioridad de Pacientes.
```
Pacientes en la cola de prioridad (de mayor a menor gravedad):
Gravedad: 5, ID: 2, Nombre: Ana Gómez
Gravedad: 4, ID: 1, Nombre: Juan Pérez
Gravedad: 3, ID: 3, Nombre: Carlos López
```

### Opcion 7: Atender al paciente mas grave.
```
Paciente atendido: Ana Gómez (ID: 2, Gravedad: 5)
```

## Historial Medico:

### Opcion 8: Agregar evento medico a Paciente.
```
Ingrese el ID del paciente: 1
Tipo de evento (CONSULTA/DIAGNOSTICO/TRATAMIENTO): CONSULTA  
Detalles del evento: Agendar cita
Evento médico agregado al paciente con ID 1.
```

### Opcion 9: Mostrar historial clinico del Paciente.
```
Ingrese el ID del paciente: 1
```
#### Respuesta:
```
·ID: 1
 Nombre: Juan Pérez
 Edad: 30
 Gravedad: 4
 ID de hospital actual: 1
Historial:
    - CONSULTA: Agendar cita [Fecha: 27-11-2024 | 23:41]
Medicamentos:
    - Ungüento [Fecha: 27-11-2024 | 23:44]
Enfermedades:
    - Alergia al Mani [Fecha: 27-11-2024 | 23:43]
```

### Opcion 10: Agregar enfermedad a Paciente.
```
Ingrese el ID del paciente: 1
```
#### Respuesta:
```
Nombre de la enfermedad: Alergia al Mani
Enfermedad 'Alergia al Mani' agregada al paciente con ID 1.
```

### Opcion 11: Agregar Medicamento a Paciente.
```Seleccione una opción: 11
Ingrese el ID del paciente: 1
```
#### Respuesta:
```
Nombre del medicamento: Ungüento
Medicamento 'Ungüento' agregado al paciente con ID 1.
```

## Gestión de Hospitales:

### Opcion 12: Agregar Hospital.
```
Ingrese el nombre del hospital a agregar: Hospital Lucio Melendez
Ingrese la especialidad del hospital: Clinica Medica
Hospital 'Hospital Lucio Melendez' agregado.
```

### Opcion 13: Agregar conexión entre hospitales .
```
Lista de hospitales:
ID: 1, Nombre: Hospital Lucio Melendez, Especialidad: Clinica Medica
ID: 2, Nombre: Hospital 2, Especialidad: Pediatria
ID: 3, Nombre: Hospital 3, Especialidad: Pedagogia

Ingrese el ID del primer hospital: 1
Ingrese el ID del segundo hospital: 3

Ingrese la distancia (en KM) entre los hospitales: 100
```
#### Respuesta:
```
Conexión entre '1' y '3' agregada con distancia 100.
```

### Opcion 14: Mostrar todos los hospitales.
```
---------------------------------------------
Lista de hospitales:

Hospital Lucio Melendez:
     - ID: 1
     - Especialidad: Clinica Medica
Hospital 2:
     - ID: 2
     - Especialidad: Pediatria
Hospital 3:
     - ID: 3
     - Especialidad: Pedagogia
---------------------------------------------
```

## Rutas y Navegación:

### Opcion 15: Mostrar mejor ruta de ambulancia.

Yo de ejemplo agregue mas hospitales y realice sus conexiones, dejo aqui la distancia entre ellos:

```
Conexión entre '1' y '2' agregada con distancia 50.
Conexión entre '1' y '4' agregada con distancia 30.
Conexión entre '2' y '3' agregada con distancia 20.
Conexión entre '2' y '4' agregada con distancia 4.
Conexión entre '3' y '4' agregada con distancia 2.
```

Entonces siguiendo con la opcion 15:
```
Ingrese el hospital de origen: 1
Ingrese el hospital de destino: 3
```
#### Respuesta:
```
Ruta más corta desde el hospital de origen al destino:
Hospital Lucio Melendez -> Hospital 5 -> Hospital 3
Distancia total: 32 km
```

### Opcion 16: Encontrar Ruta usando BFS.
```
Lista de hospitales:
ID: 1, Nombre: Hospital Lucio Melendez, Especialidad: Clinica Medica
ID: 2, Nombre: Hospital 2, Especialidad: Pediatria
ID: 3, Nombre: Hospital 3, Especialidad: Pedagogia
ID: 4, Nombre: Hospital 5, Especialidad: Protesis.
Ingrese el ID del hospital de origen para BFS: 4
Ingrese el ID del hospital de destino para BFS: 2
```
#### Respuesta:
```
La ruta encontrada por BFS desde el hospital con ID 4 hasta el hospital con ID 2 es:
Hospital 5 -> Hospital 2
```

### Opcion 17: Encontrar ruta usando DFS.
```
Lista de hospitales:
ID: 1, Nombre: Hospital Lucio Melendez, Especialidad: Clinica Medica
ID: 2, Nombre: Hospital 2, Especialidad: Pediatria
ID: 3, Nombre: Hospital 3, Especialidad: Pedagogia
ID: 4, Nombre: Hospital 5, Especialidad: Protesis.
Ingrese el ID del hospital de origen para DFS: 2
Ingrese el ID del hospital de destino para DFS: 4
```
#### Respuesta:
```
La ruta encontrada por DFS desde el hospital con ID 2 hasta el hospital con ID 4 es:
Hospital 2 -> Hospital 5
```

## Diagnóstico de Enfermedad:

### Opcion 18: Agregar paso de diagnostico.
```
Ingrese el ID del paso de diagnóstico: Paso 1
Ingrese la descripción del paso: Tomar presion
Ingrese los síntomas requeridos (separados por coma) o deje en blanco: Mareo, sueño
Ingrese los síntomas presentes (separados por coma): hemorragia, Mareo
```

#### Respuesta:
```
Paso de diagnóstico 'Paso 1' agregado.
```
---------------------------------------------------

```
Ingrese el ID del paso de diagnóstico: Paso 2
Ingrese la descripción del paso: ejercer presion en la herida con bendas.
Ingrese los síntomas requeridos (separados por coma) o deje en blanco: hemorragia
Ingrese los síntomas presentes (separados por coma): hemorragia, Mareo
```

#### Respuesta:
```
Paso de diagnóstico 'Paso 2' agregado.
```
---------------------------------------------------

```
Ingrese el ID del paso de diagnóstico: Paso 3
Ingrese la descripción del paso: Tomar temperatura
Ingrese los síntomas requeridos (separados por coma) o deje en blanco: Fiebre
Ingrese los síntomas presentes (separados por coma): hemorragia, Mareo
```

#### Respuesta:
```
Paso de diagnóstico 'Paso 3' agregado.
```

### Opcion 19: Agregar dependencia entre pasos.
```
Ingrese el ID del paso que dependera del siguiente: Paso 2
Ingrese el ID del paso dependiende del anterior: Paso 1
Dependencia agregada: Paso 2 -> Paso 1

Ingrese el ID del paso que dependera del siguiente: Paso 3
Ingrese el ID del paso dependiende del anterior: Paso 2
Dependencia agregada: Paso 3 -> Paso 2
```

### Opcion 20: Mostrar secuencia de diagnostico.
```
Ingrese los síntomas presentes (separados por coma): hemorragia, Mareo
```

#### Respuesta:
```
Secuencia de diagnóstico basada en los síntomas:
- Paso 2: ejercer presion en la herida con bendas.
- Paso 1: Tomar presion
```
