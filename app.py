from flask import Flask,render_template,request
from Backend.usuarios import cadastrar_usuario as salvar_usuario, listar_usuarios as obter_usuarios

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
def pagina_cadastrar_usuario():
    if request.method == "POST":
        nome = request.form["nome"]
        setor = request.form["setor"]
        contato = request.form["contato"]
        email = request.form["email"]
        senha = request.form["senha"]

        salvar_usuario(nome, setor, contato, email, senha)
    return render_template("cadastrar_usuario.html")

@app.route("/usuarios/listar")
def listar_usuarios():
    usuarios = obter_usuarios()
    return render_template("listar_usuarios.html", usuarios=usuarios)

@app.route("/equipamentos/cadastrar")
def cadastrar_equipamento():
    return render_template("cadastrar_equipamento.html")

@app.route("/equipamentos/listar")
def listar_equipamentos():
    return render_template("listar_equipamentos.html")

if __name__ == "__main__":
    app.run(debug=True)