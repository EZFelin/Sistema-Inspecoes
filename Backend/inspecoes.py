from Backend.conexao import conectar


def cadastrar_inspecao(usuario_id, equipamento_id, data_inspecao, status, observacao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO inspecoes
        (usuario_id, equipamento_id, data_inspecao, status, observacao)
        VALUES (%s, %s, %s, %s, %s)
    """, (usuario_id, equipamento_id, data_inspecao, status, observacao))

    conexao.commit()

    cursor.close()
    conexao.close()


def listar_inspecoes():
    pass


def buscar_inspecao_por_id():
    pass


def atualizar_inspecao():
    pass


def deletar_inspecao():
    pass