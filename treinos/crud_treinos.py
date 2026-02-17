from banco_de_dados.criar_conexao import criar_conexao

def cadastrar_treino(tipo: str, id_instrutor: int, id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO treinos (tipo, id_instrutor, id_aluno) VALUES (%s, %s, %s);", [tipo, id_instrutor, id_aluno])
        conexao.commit()
        print(f"Treino '{tipo}' cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_treinos() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treinos ORDER BY id_treino ASC;")
        conexao.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar treinos: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_treino(nome: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treinos WHERE nome LIKE %s;", [f"%{nome}%"])
        conexao.commit()
        treino = listar_nome_treino(nome, "email")

        for nome in treino:
            print(f"Treino '{nome[0]}' buscado com sucesso!")

        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_treino(id_treino, parametro_atributo: str, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE treinos SET {atributo} = %s WHERE id_treino = %s;", [parametro_atributo, id_treino])
        conexao.commit()
        nome_treino = listar_nome_treino(id_treino, "id_treino")

        for nome in nome_treino:
            print(f"{nome_atributo} de treino '{nome[0]}' atualizado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_treino(id_treino: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM treinos WHERE id = %s;", [id_treino])
        nome_treino = listar_nome_treino(id_treino, "id_treino")

        for nome in nome_treino:
            print(f"Treino '{nome[0]}' deletado com sucesso!")

        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_treino_aluno(id_aluno: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treinos WHERE id_aluno = %s ORDER BY id_treino ASC;", [id_aluno])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao visualizar treino de aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_treino_aluno(id_aluno: int, id_treino: int, nome_exercicio: str, parametro_atributo: str | int, atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE treinos SET {atributo} = %s WHERE id_treino = %s AND id_aluno = %s AND nome_exercicio = %s;", [parametro_atributo, id_treino, id_aluno, nome_exercicio])
        conexao.commit()
        print(f"{atributo} de treino atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_nome_treino(id_treino: int, atributo: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome FROM treinos WHERE {atributo} = %s;", [id_treino])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar nome do treino: {e}")
    finally:
        cursor.close()
        conexao.close()