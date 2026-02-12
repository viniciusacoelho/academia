from banco_de_dados.criar_conexao import criar_conexao

def cadastrar_exercicio(nome: str, quantidade_series: int, numero_repeticoes: int, peso: float, tempo_descanso: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO exercicios (nome, quantidade_series, numero_repeticoes, peso, tempo_descanso) VALUES (%s, %s, %s, %s, %s);", [nome, quantidade_series, numero_repeticoes, peso, tempo_descanso])    
        conexao.commit()
        print("Exercício cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_exercicios() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM exercicios ORDER BY id_exercicio ASC;")
        conexao.commit()
        # print("Exercícios listados com sucesso!")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar exercícios: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_exercicio(nome: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM exercicios WHERE nome = %s;", [f"%{nome}%"])    
        conexao.commit()
        print("Exercício buscado com sucesso!")
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_exercicio(id_exercicio: int, parametro_atributo: str | float, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE exercicios SET {atributo} = %s WHERE id_exercicio = %s;", [parametro_atributo , id_exercicio])
        conexao.commit()
        print(f"{nome_atributo} de exercicio atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_exercicio(id_exercicio: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM exercicios WHERE id_exercicio = %s;", [id_exercicio])    
        conexao.commit()
        # print(f"exercicio {nome} deletado com sucesso!")
        print("Exercício deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def cadastrar_exercicio_aluno(id_aluno: int, id_exercicio: int, metodo_pagamento: str, data_hora: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO exercicio_aluno (id_exercicio, id_aluno, metodo_pagamento, data_hora) VALUES (%s, %s, %s, %s);", [id_exercicio, id_aluno, metodo_pagamento, data_hora])    
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_exercicio_aluno(id_aluno: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT p.id_exercicio, p.nome, p.descricao, p.tipo, p.preco FROM exercicio_aluno pa JOIN exercicios p ON p.id_exercicio = pa.id_exercicio WHERE id_aluno = %s ORDER BY id_exercicio;", [id_aluno])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_exercicio_aluno(id_exercicio: int, id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM exercicio_aluno WHERE id_exercicio = %s AND id_aluno = %s;", [id_exercicio, id_aluno])    
        conexao.commit()
        # print(f"exercicio {nome} deletado com sucesso!")
        print("Exercício deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()