from Backend.conexao import conectar

def cadastrar_usuario(nome, setor, contato, email, senha):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO usuarios
        (nome, setor, contato, email, senha)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (nome, setor, contato, email, senha)
    )

    conexao.commit()

    print("Usuário cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def listar_usuarios():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, setor, contato, email
        FROM usuarios
    """)

    usuarios = cursor.fetchall()

    cursor.close()
    conexao.close()
    return usuarios

def buscar_usuario_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, setor, email
        FROM usuarios
        WHERE nome = %s
    """, (nome,))

    usuario = cursor.fetchone()
    if usuario:
        print(f"Nome: {usuario[0]}")
        print(f"Setor: {usuario[1]}")
        print(f"E-mail: {usuario[2]}")
    else:
        print("Usuário não encontrado.")

    cursor.close()
    conexao.close()
