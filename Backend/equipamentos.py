from conexao import conectar

def cadastrar_equipamento():
    conexao = conectar()

    cursor = conexao.cursor()

    nome = input("Nome: ")
    setor = input("Setor: ")
    descricao = input("Descrição: ")


    cursor.execute(
        """
        INSERT INTO equipamentos
        (nome, setor, descricao)
        VALUES (%s, %s, %s)
        """,
        (nome, setor, descricao)
    )

    conexao.commit()

    print("Equipamento cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def listar_equipamentos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, setor, descricao
        FROM equipamentos
        """)
    
    equipamentos = cursor.fetchall()
    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
    else:
        for equipamento in equipamentos:
            print(f"Nome: {equipamento[0]}")
            print(f"Setor: {equipamento[1]}")
            print(f"Descrição: {equipamento[2]}")
            print("-" * 20)

    cursor.close()
    conexao.close()

