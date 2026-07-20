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
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
                    SELECT 
                        i.id_inspecao,
                        u.nome,
                        e.nome,
                        i.data_inspecao,
                        i.status,
                        i.observacao
                    FROM inspecoes i
                    JOIN usuarios u
                    ON i.usuario_id = u.id_usuario
                    JOIN equipamentos e
                    ON i.equipamento_id = e.id_equipamento
                    ORDER BY i.id_inspecao
                   """)
    
    inspecoes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return inspecoes

def buscar_inspecao_por_id(id_inspecao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id_inspecao,
            usuario_id,
            equipamento_id,
            data_inspecao,
            status,
            observacao
        FROM inspecoes
        WHERE id_inspecao = %s
    """, (id_inspecao,))

    inspecao = cursor.fetchone()

    cursor.close()
    conexao.close()

    return inspecao

def atualizar_inspecao(id_inspecao, usuario_id, equipamento_id, data_inspecao, status, observacao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE inspecoes
        SET
            usuario_id = %s,
            equipamento_id = %s,
            data_inspecao = %s,
            status = %s,
            observacao = %s
        WHERE id_inspecao = %s
    """, (
        usuario_id,
        equipamento_id,
        data_inspecao,
        status,
        observacao,
        id_inspecao
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

def deletar_inspecao(id_inspecao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM inspecoes
        WHERE id_inspecao = %s
    """, (id_inspecao,))

    conexao.commit()

    cursor.close()
    conexao.close()