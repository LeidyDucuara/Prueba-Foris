## Prueba Foris

## Autor ✒️

* **Leidy Marcela Ducuara** - [LeidyDucuara](https://github.com/LeidyDucuara)

### Descripción Problema

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
### Solución

Para desarrollar esta solución voy a utilizar python y programación orientada a objetos.

Principalmente se envidencian tres clases   importantes = Los estudiantes, La presencia de dicho estudiante en alguna sala, en determinado momento y un resumen de asistencia general.

<image src="Asistencia_foris\docs\img_class.PNG" alt="Clases">

Como la idea era amplicar un poco la idea y no realizarlo en una simple función cree un modelo tipo servicios donde el entry point recibe el parametro de tipo txt y lo envia a la clase Ap_asistence, esta clase usara los servicios creados para dar solucion a los requerimientos.

Por otro lado tendre las entidades en la carpeta model donde definire la clase, sus atributos y metodos. Para tener persistencia creer una lista para almacenar los objetos de tipo estudiante y otra para almacenar los de tipo presencia, para asistencia cree un atributo de clase de tipo diccionario donde podremos almacenar y actualizar la asistecia de cada estudiante.

En la carpeta services cree la clase abstracta de cada modulo para despues heredar e implementar sus servicios.

<image src="Asistencia_foris\docs\img_componentes.PNG" alt="Componentes">


Este principalmente cuenta con dos procesos importantes, lee y registra los datos ingresados y genera un reporte o resumen donde se puede envidenciar la asistencia de los estudiantes a lo largo de la semana.

### Ejecución

Para ejecutar nuestro script debemos estar en la ubicacion donde se almacenen nuestros archivos y usar el siguiente comando

```
python App.py prueba.txt

```

### Casos de prueba o Validaciones

* Validamos el comando ingresado al comenzar cada linea para verificar que lo soportamos

<image src="Asistencia_foris\docs\prueba4.PNG" alt="Componentes">

* Al registrar un estudiante validamos que no se encuentre ya registrado
* Validación dia de la semana esta entre 1-7

<image src="Asistencia_foris\docs\prueba2.PNG" alt="Componentes">

* El tiempo registrado debe ser mayor a 5 minutos

<image src="Asistencia_foris\docs\prueba5.PNG" alt="Componentes">

* Validamos que el estudiante identificado en la presencia si se encuentre registrado como estudiante

<image src="Asistencia_foris\docs\prueba3.PNG" alt="Componentes">

* Ordenamos de mayor a menor a los estudiantes de acuerdo a la cantidad de minutos

<image src="Asistencia_foris\docs\prueba1.PNG" alt="Componentes">


## Licencia 

Este proyecto fue creado bajo la Licencia (MIT) - mira el archivo [LICENSE.md](LICENSE.md) para detalles






