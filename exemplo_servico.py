from flask import Flask
from flask import jsonify

# criando instancia de um servico web
servico = Flask(__name__)

# criando rotas de acesso ao servico web
@servico.route("/info")
def get_info():
    return jsonify(
        version = "1.0",
        autor="luis paulo",
        email="luispscarvalho@gmail.com"
    )

@servico.route("/somar/<int:numero_a>/<int:numero_b>")
def somar(numero_a, numero_b):
    return str(numero_a + numero_b)


@servico.route("/subtrair/<int:numero_a>/<int:numero_b>")
def subtrair(numero_a, numero_b):
    return str(numero_a - numero_b)    

# coloca o servico web no ar
if __name__ == "__main__":
    servico.run()