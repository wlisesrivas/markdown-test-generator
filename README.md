# markdown-test-generator
Es una herramienta para generar exámenes a partir de un archivo Markdown. Esto significa
que puedes estructurar el formato que tendrá el texto, negrita, cursiva, tablas, etc.

Markdown<br>
![p1](https://raw.githubusercontent.com/wlisesrivas/markdown-test-generator/development/app/static/sample-md.png)

Examen generado<br>
![p2](https://raw.githubusercontent.com/wlisesrivas/markdown-test-generator/development/app/static/sample-animation.gif)

### Requerimientos
[Python-3.7.x](https://www.python.org/downloads/release/python-374/)
Asegúrate de instalar **pip** al instalar python.

### Instalación
Una vez `python` y `pip` estén instalados, simplemente ejecute `install.bat`, este archivo por
lotes simplemente hará la instalación de los paquetes requeridos.

Si desea hacerlo manual, simplemente ejecute (dentro de la aplicación ya descargada):
`python -m pip install -r requirements.txt`

### Generar Exámenes
La aplicación generara todos los archivos **.md** (Markdown) que estén dentro del folder 
`./examenes/**`, note que en el folder ya existe un examen de prueba (prueba-evaluacion.md).

Puede agregar tantos como quiera, todos se van a generar en archivos separados.

Para generar los exámenes, hay dos archivos por lotes,
1. `generar-local.bat`
Es un archivo por lotes que simplemente ejecuta `python generator.py` y generaran los 
exámenes incluyendo las librerías requeridas (Bootstrap, jQuery) para ejecutarlo independientemente
en el navegador (usualmente para verificar que todo esté bien).

2. `generar-embed.bat` 
Es un archivo por lotes que simplemente ejecuta `python generator.py embed` de esta forma
se generarán los exámenes sin incluir ninguna librería externa, se asume que se va a incluir en otra
Web como (Embedded).

Los exámenes resultantes tendrán el mismo nombre del archivo markdown pero con su extensión .html, se crearan
en el folder principal de la aplicación.

### Estructura del examen (Markdown)
Aunque es basado en markdown para su formato de estilo, por el momento se soportan los siguientes tipos de preguntas:

1. **Pregunta de una selección**:
```text
1. Las variables estadísticas pueden ser cualitativa y cuantitativa:
    - (x) Verdadero
    - ( ) Falso
```
Note que la respuesta correcta esta especificada con una **x** (x o X, mayúscula o minúscula) y deben estar en 
paréntesis para especificar que es solo una que se va a seleccionar, por ejemplo, para preguntas de falso o verdadero.

2. **Pregunta de selección múltiple**:
```text
3. Algunos ejemplos de variables cuantitativas continuas son:
    - [ ] Personas de un hogar
    - [x] Altura de una persona
    - [x] Pi (3.1415...)
```
Muy similar a la anterior pero este tipo de pregunta permite seleccionar más de una a la vez, deben estar entre corchetes
con una *x* a las respuestas correctas. El resultado a este tipo de preguntas es prorrateado, es decir, debe seleccionar solo las
correctas para que esa pregunta se interprete como correcta.

Note que para los tipos de preguntas 1 y 2, debe dejar un espacio para las respuesta incorrectas, ej. ( ) o [ ],
las preguntas deben ser de selección múltiple o de una selección, no puede mezclarlas.

3. **Pregunta abierta** (escriba el texto)
```text
4. Es la rama de las matemáticas que estudia la variabilidad?
    - R:= estadistica
```
Es una pregunta donde se debe escribir la respuesta correcta, esta se especifica en la siguiente línea de la pregunta
 precedida por **R:=** (R o r, mayúscula o minúscula) luego la respuesta correcta (se valida sin importar que sea mayúscula o minúscula)

### Diseñar el examen
Hay varias herramientas por ahí en internet (en línea y/o descargables) que te permiten previsualizar archivos Markdown.
Algunas online de ejemplo:

1. https://dillinger.io/
2. https://markdownlivepreview.com/
