from conexao import conectar

def cadastrar_usuario():
    conexao = conectar()

    cursor = conexao.cursor()

    nome = input("Nome: ")
    setor = input("Setor: ")
    contato = input("Contato: ")
    email = input("Email: ")
    senha = input("Senha: ")

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
        SELECT nome, setor, email
        FROM usuarios
    """)

    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario[0]}")
            print(f"Setor: {usuario[1]}")
            print(f"E-mail: {usuario[2]}")
            print("-" * 20)

    cursor.close()
    conexao.close()
