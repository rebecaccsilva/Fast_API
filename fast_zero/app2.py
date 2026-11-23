from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
        <head>
             <title>Nosso olá mundo!!</title>
        </head>
        <body>
            <h1> Olá Mundo! </h1>
            <h3> MASSA DEMAIS ISSO </h3>
        </body>
    </html>"""
