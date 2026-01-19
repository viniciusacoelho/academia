from banco_de_dados.criar_conexao import criar_conexao

def cadastrar_plano(nome: str, descricao: str, tipo: str, preco: float):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO planos (nome, descricao, tipo, preco) VALUES (%s, %s, %s, %s)", [nome, descricao, tipo, preco])    
        conexao.commit()
        print("Plano cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_planos() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM planos")
        conexao.commit()
        # print("Planos listados com sucesso!")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar planos: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_plano(nome: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM planos WHERE nome = %s", [f"%{nome}%"])    
        conexao.commit()
        print("Plano buscado com sucesso!")
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_plano(atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE {atributo} FROM planos")    
        conexao.commit()
        print(f"{atributo} de plano atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_plano(id: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM planos WHERE id = %s", id)    
        conexao.commit()
        # print(f"Plano {nome} deletado com sucesso!")
        print("Plano deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar plano: {e}")
    finally:
        cursor.close()
        conexao.close()