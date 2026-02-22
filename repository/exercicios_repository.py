from config.banco_de_dados_config import criar_conexao

def cadastrar_exercicio(nome: str, quantidade_series: int, numero_repeticoes: int, peso: float, tempo_descanso: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO exercicios (nome, quantidade_series, numero_repeticoes, peso, tempo_descanso) VALUES (%s, %s, %s, %s, %s) RETURNING id_exercicio;", [nome, quantidade_series, numero_repeticoes, peso, tempo_descanso])
        conexao.commit()
        print(f"Exercício {nome} cadastrado com sucesso!")
        return cursor.fetchall()
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
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar exercícios: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_exercicio(id_exercicio: int, parametro_atributo: str | float, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE exercicios SET {atributo} = %s WHERE id_exercicio = %s;", [parametro_atributo , id_exercicio])
        conexao.commit()
        nome_exercicio = listar_nome_exercicio(id_exercicio, "id_exercicio")

        for nome in nome_exercicio:
            print(f"{nome_atributo} de exercício '{nome[0]}' atualizado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_exercicio(id_exercicio: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM exercicios WHERE id_exercicio = %s;", [id_exercicio])
        conexao.commit()
        nome_exercicio = listar_nome_exercicio(id_exercicio, "id_exercicio")

        for nome in nome_exercicio:
            print(f"Exercício '{nome[0]}' deletado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao deletar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_exercicio(nome: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM exercicios WHERE nome LIKE %s;", [f"%{nome}%"])
        conexao.commit()
        exercicio = listar_nome_exercicio(nome, "email")

        for nome in exercicio:
            print(f"Exercício '{nome[0]}' buscado com sucesso!")

        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_nome_exercicio(id_exercicio: int, atributo: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome FROM exercicios WHERE {atributo} = %s;", [id_exercicio])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar nome do exercicio: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_exercicio_(id_exercicio: int, atributo: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome FROM exercicios WHERE {atributo} = %s;", [id_exercicio])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar nome do exercicio: {e}")
    finally:
        cursor.close()
        conexao.close()