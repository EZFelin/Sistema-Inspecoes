from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/equipamentos")
def equipamentos():
    return render_template("equipamentos.html")

@app.route("/usuarios/cadastrar", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        nome = request.form["nome"]
        setor = request.form["setor"]
        email = request.form["email"]
        
        print(nome)
        print(setor)
        print(email)
    return render_template("cadastrar_usuario.html")

@app.route("/usuarios/listar")
def listar_usuarios():
    return render_template("listar_usuarios.html")

@app.route("/equipamentos/cadastrar")
def cadastrar_equipamento():
    return render_template("cadastrar_equipamento.html")

@app.route("/equipamentos/listar")
def listar_equipamentos():
    return render_template("listar_equipamentos.html")

if __name__ == "__main__":
    app.run(debug=True)