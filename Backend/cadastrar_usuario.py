import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="sistema_inspecoes",
    user="postgres",
    password="ucs"
)

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