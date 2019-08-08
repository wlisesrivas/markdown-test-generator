
# Wrapper para plantilla resultante HTML
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
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" 
            integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" 
            crossorigin="anonymous"></script>
</head>
<body>
<div class="container">
    <div class="form-row">
        <div class="container">
            {{content}}
        </div>
    </div>
    <div class="alert alert-success" role="alert">
      3 de 3 Preguntas correctas! <b>Calificaci&oacute;n: 100% </b>
    </div>
    <div class="row">
        <button class="btn btn-lg btn-success">Verificar</button>
        <button class="btn btn-link">Reiniciar Todo</button>
    </div>
</div>
</body>
</html>
"""