## Problema

### Descripción

Buscamos detectar a los estudiantes que más asisten a clases.

El código procesará un archivo de entrada. Puedes elegir si aceptar el input a través de la entrada estándar (e.g. si usaras Python: `cat input.txt | python yourcode.py`) o como un nombre de archivo entregado como parámetro (e.g. `python yourcode.py input.txt`).

Cada línea del archivo de entrada empieza con un comando. Hay dos comandos posibles.

El primero es `Student`, que registra un nuevo estudiante en la aplicación. Ejemplo:

```
Student Matthias
```

El segundo comando es `Presence`, que registra la presencia de un estudiante en la universidad. Esta línea tiene los siguientes datos separados por espacios:

- el comando (`Presence`)
- el nombre del estudiante
- el día de la semana
- la hora inicial de detección
- la hora final de detección
- el código de la sala en la que se realizó la detección

Observaciones:

- Los días de la semana van de 1 a 7
- Los tiempos se entregan en formato HH:MM, usando un reloj de 24 horas.
- También se asume que ningún estudiante se queda en la universidad después de media noche (es decir, la hora de inicio siempre será anterior a la hora de fin).

Ejemplo:

```
Presence Matthias 2 09:04 10:35 F100
```

Esto indica que Matthias estuvo en la sala F100 el día martes desde las 9:04 hasta las 10:35.

### Objetivo

Genera un reporte que liste cada estudiante con el total de minutos registrados y la cantidad de días que asistió a la universidad. Ordena el resultado por la cantidad de minutos de mayor a menor.

Descarta cualquier registro que indique presencias menores a 5 minutos.

Ejemplo de entrada:

```
Student Marco
Student David
Student Fran
Presence Marco 1 09:02 10:17 R100
Presence Marco 3 10:58 12:05 R205
Presence David 5 14:02 15:46 F505
```

Ejemplo de salida:

```
Marco: 142 minutes in 2 days
David: 104 minutes in 1 day
Fran: 0 minutes
```