# markdown-test-generator
Es una herramienta para generar examenes a partir de un archivo markdown. Esto significa
que puedes estructurar el formato que tendra el texto, negrita, cursiva, tablas, etc.

Markdown<br>
![p1](https://raw.githubusercontent.com/wlisesrivas/markdown-test-generator/develop/app/static/sample-md.png)

Examen genrado<br>
![p2](https://raw.githubusercontent.com/wlisesrivas/markdown-test-generator/develop/app/static/sample-animation.gif)

### Requerimientos
[Python-3.7.x](https://www.python.org/downloads/release/python-374/)
Asegurate de instalar **pip** al instalar python.

### Instalacion
Una vez `python` y `pip` estan intalados, simplemente ejecute `install.bat`, este archivo por
lotes simplemente hara la instalacion de los paquetes requeridos.

Si desea hacerlo manual, simplemente ejecute (dentro de la aplicacion ya descargada):
`python -m pip install -r requirements.txt`

### Generar Examenes
La aplicacion generara todos los arhivos **.md** (Markdown) que esten dentro del folder 
`./examenes/**`, note que en el folder ya existe un examen de prueba (prueba-evaluacion.md).

Puede agregar tantos como quiera, todos se van a generar en archivos separados.

Para generar los examenes, hay dos arhivos por lotes,
1. `generar-local.bat`
Es un archivo por lotes que simplemente ejecuta `python generator.py` y generaran los 
examenes incluyendo las librerias requeridas (Bootstrap, jQuery) para ejecutarlo independientemente
en el navegador (usalmente para verificar que todo este bien).

2. `generar-embed.bat` 
Es un archivo por lotes que simplemente ejecuta `python generator.py embed` de esta forma
se generaran los examenes sin incluir ninguna libreria externa, se asume que se va a incluir en otra
Web como (Embedded).

Los examenes resultantes tendran el mismo nombre del archivo markdown pero con su extension .html, se crearan
en el folder principal de la aplicacion.

### Estructura del examen (Markdown)
Aunque es basado en markdown para su formato de estilo, por el momento se soportan los siguientes tipos de preguntas:

1. **Pregunta de una seleccion**:
```text
1. Las variables estadísticas pueden ser cualitativa y cuantitativa:
    - (x) Verdadero
    - ( ) Falso
```
Note que la respuesta correcta esta especificada con una **x** (x o X, mayuscula o minuscula) y deben estar en 
parentesis para espeficiar que es solo una que se va a seleccionar, por ejemplo, para preguntas de falso o verdadero.

2. **Pregunta de seleccion multiple**:
```text
3. Algunos ejemplos de variables cuantitativas continuas son:
    - [ ] Personas de un hogar
    - [x] Altura de una persona
    - [x] Pi (3.1415...)
```
Muy similar a la anterior pero este tipo de pregunta permite seleccionar mas de una a la vez, deben estar entre corchetes
con una *x* a las respuestas correctas. El resultado a este tipo de preguntas es prorateado, es decir, debe seleccionar solo las
correctas para que esa pregunta se interprete como correcta.

Note que para los tipos de preguntas 1 y 2, debe dejar un espacio para las respuesta incorretas, ej. ( ) o [ ],
las preguntas deben ser de seleccion multiple o de una seleccion, no puede mezclarlas.

3. **Pregunta abierta** (escriba el texto)
```text
4. Es la rama de las matemáticas que estudia la variabilidad?
    - R:= estadistica
```
Es una pregunta donde se debe escribir la respuesta correcta, esta se especifica en la siguiente linea de la pregunta
 precedida por **R:=** (R o r, mayuscula o minuscula) luego la respuesta correcta (se valida sin importar que sea mayuscula o minuscula)

### Disenar el examen
Hay varias herramientas por ahi en internet (en linea y/o descargables) que te premiten pre-visualizar archivos Markdown.
Algunas online de ejemplo:

1. https://dillinger.io/
2. https://markdownlivepreview.com/