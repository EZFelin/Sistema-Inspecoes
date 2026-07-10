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
        SELECT id_usuario, nome, setor, contato, email, senha
        FROM usuarios
        ORDER BY id_usuario
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

def buscar_usuario_por_id(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_usuario, nome, setor, contato, email, senha
        FROM usuarios
        WHERE id_usuario = %s
    """, (id_usuario,))

    usuario = cursor.fetchone()
    
    cursor.close()
    conexao.close()

    return usuario

def atualizar_usuario(id_usuario, nome, setor, contato, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE usuarios
        SET nome = %s, setor = %s, contato = %s, email = %s, senha = %s
        WHERE id_usuario = %s
    """, (nome, setor, contato, email, senha, id_usuario))

    conexao.commit()

    cursor.close()
    conexao.close()

def deletar_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM usuarios
        WHERE id_usuario = %s
    """, (id_usuario,))

    conexao.commit()

    cursor.close()
    conexao.close()