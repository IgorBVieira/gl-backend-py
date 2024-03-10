from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulação de um banco de dados em memória
dados_cadastro = ["teste"]


@app.route("/cadastro", methods=["GET", "POST"])
def gerenciar_cadastro():
    if request.method == "POST":
        novo_cadastro = request.json
        dados_cadastro.append(novo_cadastro)
        return jsonify(novo_cadastro), 201
    else:
        return jsonify(dados_cadastro)


if __name__ == "__main__":
    app.run(debug=True)
