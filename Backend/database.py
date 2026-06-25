import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="sistema_inspecoes",
    user="postgres",
    password="ucs"
)

cursor = conexao.cursor()

cursor.execute("""
    SELECT nome, setor, email
    FROM usuarios
""")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(f"Nome: {usuario[0]}")
    print(f"Setor: {usuario[1]}")
    print(f"E-mail: {usuario[2]}")
    print("-" * 20)

cursor.close()
conexao.close()