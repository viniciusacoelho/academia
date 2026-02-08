from banco_de_dados.criar_conexao import criar_conexao

def cadastrar_plano(nome: str, descricao: str, tipo: str, preco: float):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO planos (nome, descricao, tipo, preco) VALUES (%s, %s, %s, %s);", [nome, descricao, tipo, preco])    
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
        cursor.execute("SELECT * FROM planos ORDER BY id_plano ASC;")
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
        cursor.execute("SELECT * FROM planos WHERE nome = %s;", [f"%{nome}%"])    
        conexao.commit()
        print("Plano buscado com sucesso!")
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_plano(id_plano: int, parametro_atributo: str | float, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE planos SET {atributo} = %s WHERE id_plano = %s;", [parametro_atributo , id_plano])
        conexao.commit()
        print(f"{nome_atributo} de plano atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_plano(id_plano: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM planos WHERE id_plano = %s;", [id_plano])    
        conexao.commit()
        # print(f"Plano {nome} deletado com sucesso!")
        print("Plano deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar plano: {e}")
    finally:
        cursor.close()
        conexao.close()

def cadastrar_plano_aluno(id_aluno: int, id_plano: int, metodo_pagamento: str, data_hora: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO plano_aluno (id_plano, id_aluno, metodo_pagamento, data_hora) VALUES (%s, %s, %s, %s);", [id_plano, id_aluno, metodo_pagamento, data_hora])    
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_plano_aluno(id_aluno: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT p.id_plano, p.nome, p.descricao, p.tipo, p.preco FROM plano_aluno pa JOIN planos p ON p.id_plano = pa.id_plano WHERE id_aluno = %s ORDER BY id_plano;", [id_aluno])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_plano_aluno(id_plano: int, id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM plano_aluno WHERE id_plano = %s AND id_aluno = %s;", [id_plano, id_aluno])    
        conexao.commit()
        # print(f"Plano {nome} deletado com sucesso!")
        print("Plano deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar plano: {e}")
    finally:
        cursor.close()
        conexao.close()