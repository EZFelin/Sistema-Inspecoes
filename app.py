from flask import Flask,render_template,request,redirect
from Backend.usuarios import (
    cadastrar_usuario as salvar_usuario, 
    listar_usuarios as obter_usuarios, 
    buscar_usuario_por_id as obter_usuario_por_id,
    atualizar_usuario,  
    deletar_usuario as excluir_usuario
)
from Backend.equipamentos import ( 
    cadastrar_equipamento as salvar_equipamento, 
    listar_equipamentos as obter_equipamentos, 
    buscar_equipamento_por_id as obter_equipamento_por_id,
    atualizar_equipamento, 
    deletar_equipamento as excluir_equipamento
)
from Backend.inspecoes import (
    cadastrar_inspecao as salvar_inspecao,
    listar_inspecoes as obter_inspecoes,
    buscar_inspecao_por_id as obter_inspecao_por_id,
    atualizar_inspecao,
    deletar_inspecao as excluir_inspecao
)
import psycopg2

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

@app.route("/inspecoes")
def inspecoes():
    return render_template("inspecoes.html")

# =========================
# USUÁRIOS
# =========================

@app.route("/usuarios/cadastrar", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        nome = request.form["nome"]
        setor = request.form["setor"]
        contato = request.form["contato"]
        email = request.form["email"]
        senha = request.form["senha"]

        salvar_usuario(nome, setor, contato, email, senha)
        return redirect("/usuarios/listar")
    
    return render_template("cadastrar_usuario.html")

@app.route("/usuarios/listar")
def listar_usuarios():
    usuarios = obter_usuarios()
    return render_template("listar_usuarios.html", usuarios=usuarios)

@app.route("/usuarios/editar/<int:id_usuario>", methods=["GET", "POST"])
def editar_usuario(id_usuario):
    if request.method == "POST":
        nome = request.form["nome"]
        setor = request.form["setor"]
        contato = request.form["contato"]
        email = request.form["email"]
        senha = request.form["senha"]

        atualizar_usuario(id_usuario, nome, setor, contato, email, senha)
        return redirect("/usuarios/listar")
    usuario = obter_usuario_por_id(id_usuario)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/usuarios/deletar/<int:id_usuario>", methods=["POST"])
def deletar_usuario(id_usuario):
    try:
        excluir_usuario(id_usuario)
        return redirect("/usuarios/listar")

    except psycopg2.errors.ForeignKeyViolation:
        return """
        <script>
            alert("Este usuário possui uma ou mais inspeções cadastradas e não pode ser excluído.");
            window.location.href = "/usuarios/listar";
        </script>
        """

# =========================
# EQUIPAMENTOS
# =========================

@app.route("/equipamentos/cadastrar", methods=["GET", "POST"])
def cadastrar_equipamento():
    if request.method == "POST":
        nome = request.form["nome"]
        setor = request.form["setor"]
        descricao = request.form["descricao"]

        salvar_equipamento(nome, setor, descricao) 

        return redirect("/equipamentos/listar")
    return render_template("cadastrar_equipamento.html")

@app.route("/equipamentos/listar")
def listar_equipamentos():
    equipamentos = obter_equipamentos()
    return render_template("listar_equipamentos.html", equipamentos=equipamentos)

@app.route("/equipamentos/editar/<int:id_equipamento>", methods=["GET", "POST"])
def editar_equipamento(id_equipamento):
    if request.method == "POST":
        nome = request.form["nome"]
        setor = request.form["setor"]
        descricao = request.form["descricao"]

        atualizar_equipamento(id_equipamento, nome, setor, descricao)
        return redirect("/equipamentos/listar")
    equipamento = obter_equipamento_por_id(id_equipamento)
    return render_template("editar_equipamento.html", equipamento=equipamento)

@app.route("/equipamentos/deletar/<int:id_equipamento>", methods=["POST"])
def deletar_equipamento(id_equipamento):
    excluir_equipamento(id_equipamento)
    return redirect("/equipamentos/listar")

# =========================
# INSPEÇÕES
# =========================

@app.route("/inspecoes/cadastrar", methods=["GET", "POST"])
def cadastrar_inspecao():
    return render_template("cadastrar_inspecao.html")


@app.route("/inspecoes/listar")
def listar_inspecoes():
    return render_template("listar_inspecoes.html")


@app.route("/inspecoes/editar/<int:id_inspecao>", methods=["GET", "POST"])
def editar_inspecao(id_inspecao):
    return render_template("editar_inspecao.html")


@app.route("/inspecoes/deletar/<int:id_inspecao>", methods=["POST"])
def deletar_inspecao(id_inspecao):
    return redirect("/inspecoes/listar")

if __name__ == "__main__":
    app.run(debug=True)