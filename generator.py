"""
    Desarrollado con mucho <3 por Wlises Rivas,
    <wlisesrivas@gmail.com>
"""
import sys
import os

import markdown
from jinja2 import Environment, PackageLoader, select_autoescape

# Renderizar el resultando incluyendo jQuery, Bootstrap.
WRAPPER_RENDER = True


def render_test(file_name: str, markdown_content: str) -> None:
    """Renderizar examen en formato Markdown a un HTML."""

    extensions = ["tables", "extensions.checkbox", "extensions.radio", "extensions.textbox"]

    html = markdown.markdown(markdown_content, extensions=extensions, output_format="html5")
    env = Environment(loader=PackageLoader('app', 'static'), autoescape=select_autoescape(['html', 'xml']))

    javascript = env.get_template('app.js').render()

    test_html = env.get_template('base.html').render(content=html, javascript=javascript)
    if WRAPPER_RENDER:
        test_html = env.get_template('wrapper.html').render(content=test_html)

    with open(f"./{file_name[:-2]}html", "w+") as file:  # create final file
        file.write(test_html)


if __name__ == "__main__":
    # Convertir todos los archivos .md (markdown) dentro de la carpeta [examenes]
    print("-" * 50 + "\nTest Generator v0.1\n" + "-" * 50)
    for file_name in os.listdir("./examenes"):
        if file_name not in [".", ".."]:
            with open(f"./examenes/{file_name}", "r") as file:
                print(f"Convirtiendo Markdown ({file_name}) ...")
                render_test(file_name, file.read())

    sys.exit(0)
