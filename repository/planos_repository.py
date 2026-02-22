from config.banco_de_dados_config import criar_conexao

def cadastrar_plano(nome: str, descricao: str, tipo: str, preco: float):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO planos (nome, descricao, tipo, preco) VALUES (%s, %s, %s, %s);", [nome, descricao, tipo, preco])    
        conexao.commit()
        print(f"Plano '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_planos() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM planos ORDER BY id_plano ASC;")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar planos: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_plano(id_plano: int, parametro_atributo: str | float, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE planos SET {atributo} = %s WHERE id_plano = %s;", [parametro_atributo , id_plano])
        conexao.commit()
        nome_plano = listar_nome_plano(id_plano)

        for nome in nome_plano:
            print(f"{nome_atributo} de plano '{nome[0]}' atualizado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_plano(id_plano: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM planos WHERE id_plano = %s;", [id_plano])    
        nome_plano = listar_nome_plano(id_plano)

        for nome in nome_plano:
            print(f"Plano '{nome[0]}' deletado com sucesso!")

        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_plano(nome: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM planos WHERE nome LIKE %s ORDER BY id_plano ASC;", [f"%{nome}%"])
        print(f"Plano '{nome}' buscado com sucesso!")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_nome_plano(id_plano: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM planos WHERE id_plano = %s;", [id_plano])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar nome do plano: {e}")
    finally:
        cursor.close()
        conexao.close()