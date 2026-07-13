from Backend.conexao import conectar

def cadastrar_equipamento(nome, setor, descricao):
    conexao = conectar()

    cursor = conexao.cursor()

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
        SELECT id_equipamento, nome, setor, descricao
        FROM equipamentos
        ORDER BY id_equipamento
    """)

    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return equipamentos

def buscar_equipamento_por_id(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(""" 
                   SELECT id_equipamento, nome, setor, descricao 
                   FROM equipamentos
                   WHERE id_equipamento = %s
                   """,(id_equipamento,))
    
    equipamento = cursor.fetchone()

    cursor.close()
    conexao.close()

    return equipamento

def atualizar_equipamento(id_equipamento, nome, setor, descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                    UPDATE equipamentos
                    SET nome = %s, setor = %s, descricao = %s
                    WHERE id_equipamento = %s
                   """,(nome, setor, descricao,id_equipamento))
    
    conexao.commit()

    cursor.close()
    conexao.close()

def deletar_equipamento(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                    DELETE FROM equipamentos
                    WHERE  id_equipamento = %s
                   """,(id_equipamento,))
    
    conexao.commit()

    cursor.close()
    conexao.close()