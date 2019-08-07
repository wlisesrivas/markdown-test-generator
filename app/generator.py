import argparse
import sys

import jinja2
import markdown

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <meta charset="utf-8">
    <style>
        body {
            font-family: sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
        h1 code,
        h2 code,
        h3 code,
        h4 code,
        h5 code,
        h6 code {
            font-size: inherit;
        }
        ul li {
            list-style-type: none;
        }
        table {
            @extend .table;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""


def parse_args(args=None):
    desc = "Crear un archivo HTML con estilo desde un archivo Markdown."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("mdfile", type=argparse.FileType("r"), nargs="?",
                        default=sys.stdin,
                        help="File to convert. Defaults to stdin.")
    parser.add_argument("-o", "--out", type=argparse.FileType("w"),
                        default=sys.stdout,
                        help="Output file name. Defaults to stdout.")
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read()
    extensions = ["tables", "extensions.checkbox", "extensions.radio"]
    html = markdown.markdown(md, extensions=extensions, output_format="html5")
    doc = jinja2.Template(TEMPLATE).render(content=html)
    args.out.write(doc)


if __name__ == "__main__":
    sys.exit(main())
