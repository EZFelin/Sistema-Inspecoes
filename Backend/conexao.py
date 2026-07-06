import psycopg2

def conectar():
    conexao = psycopg2.connect(
        host="localhost",
        database="sistema_inspecoes",
        user="postgres",
        password="ucs"
    )
    return conexao