from config.banco_de_dados_config import criar_conexao
from repository.planos_repository import listar_nome_plano

def assinar_plano_aluno(id_plano: int, id_aluno: int, metodo_pagamento: str, data_hora: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO plano_aluno (id_plano, id_aluno, metodo_pagamento, data_hora) VALUES (%s, %s, %s, %s);", [id_plano, id_aluno, metodo_pagamento, data_hora])
        conexao.commit()
        nome_plano = listar_nome_plano(id_plano)

        for nome in nome_plano:
            print(f"Plano '{nome[0]}' assinado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao assinar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def visualizar_plano_aluno(id_aluno: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT p.* FROM plano_aluno pa JOIN planos p ON p.id_plano = pa.id_plano WHERE id_aluno = %s ORDER BY id_plano;", [id_aluno])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao visualizar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def cancelar_plano_aluno(id_plano: int, id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM plano_aluno WHERE id_plano = %s AND id_aluno = %s;", [id_plano, id_aluno])
        nome_plano = listar_nome_plano(id_plano)
        conexao.commit()

        for nome in nome_plano:
            print(f"Plano '{nome[0]}' cancelado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao cancelar plano: {e}")
    finally:
        cursor.close()
        conexao.close()