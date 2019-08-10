"""
    Desarrollado con mucho <3 por Wlises Rivas,
    <wlisesrivas@gmail.com>
"""
import argparse
import sys

import markdown
from jinja2 import Environment, PackageLoader, select_autoescape
from slimit import minify


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Crear un examen en HTML a partir de un archivo Markdown.")

    parser.add_argument(
        "mdfile", type=argparse.FileType("r"), nargs="?", default=sys.stdin, help="File to convert. Defaults to stdin."
    )

    parser.add_argument(
        "-o",
        "--out",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Nombre de archivo de resultante. Por defecto se muestra el resultado (stdout)."
    )

    return parser.parse_args(args)


def main(args=None) -> None:
    args = parse_args(args)
    md = args.mdfile.read()

    extensions = ["tables", "extensions.checkbox", "extensions.radio", "extensions.textbox"]

    html = markdown.markdown(md, extensions=extensions, output_format="html5")
    env = Environment(loader=PackageLoader('app', 'static'), autoescape=select_autoescape(['html', 'xml']))
    javascript = env.get_template('app.js').render()
    # minifier javascript
    # todo minifier js
    # js = minify(javascript)
    doc = env.get_template('base.html').render(content=html, javascript=javascript)

    args.out.write(doc)


if __name__ == "__main__":
    sys.exit(main())
