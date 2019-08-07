"""
    Desarrollado con mucho <3 por Wlises Rivas,
    <wlisesrivas@gmail.com>
"""
import argparse
import sys

import jinja2
import markdown

from config import TEMPLATE


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

    extensions = ["tables", "extensions.checkbox", "extensions.radio"]

    html = markdown.markdown(md, extensions=extensions, output_format="html5")
    doc = jinja2.Template(TEMPLATE).render(content=html)

    args.out.write(doc)


if __name__ == "__main__":
    sys.exit(main())
