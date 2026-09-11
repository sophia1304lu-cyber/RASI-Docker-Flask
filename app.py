from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Minha primeira aplicação Flask</title>
    </head>
    <body>
        <h1>Minha primeira aplicação Flask</h1>
        <p>Aplicação executando dentro de um container Docker!</p>
    </body>
    </html>
    """


@app.route("/sobre")
def sobre():
    return """
    <html>
    <head>
        <title>Sobre o Projeto</title>
    </head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Sobre o Projeto</h1>
        <p>Esta é a página sobre da nossa aplicação Flask.</p>
        <p>O projeto foi desenvolvido utilizando Python, Flask e Docker.</p>
        <a href="/">Voltar para o início</a>
    </body>
    </html>
    """


@app.route("/contato")
def contato():
    return """
    <html>
    <head>
        <title>Entre em Contato</title>
    </head>
    <body style="font-family: Arial; background: #eeeeee; padding: 50px;">
        <div style="background: white; padding: 30px; max-width: 500px; margin: auto;">
            <h1>Entre em Contato</h1>
            <p>Esta é a página de contato da aplicação.</p>
            <p>E-mail: contato@flask.com</p>
            <a href="/">Voltar para o início</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
