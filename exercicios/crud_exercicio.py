from banco_de_dados.criar_conexao import criar_conexao

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

def cadastrar_exercicio_aluno(id_treino: int, id_exercicio: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO treino_exercicio (id_treino, id_exercicio) VALUES (%s, %s);", [id_treino, id_exercicio])
        conexao.commit()
        print("Exercício cadastrado ao treino com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar exercício do treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_exercicio_aluno(id_treino: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treino_exercicio WHERE id_treino = %s ORDER BY id_exercicio;", [id_treino])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar exercícios do treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_imprimir_exercicio_aluno(id_treino: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        # cursor.execute("SELECT t.nome, t.tipo, e.nome, e.quantidade_series, e.numero_repeticoes, e.peso, e.tempo_descanso FROM treino_exercicio te JOIN exercicios e ON e.id_exercicio = te.id_exercicio JOIN treinos t ON t.id_treino = te.id_treino WHERE t.id_treino = %s ORDER BY e.id_exercicio;", [id_treino])
        cursor.execute("SELECT e.id_exercicio, e.nome, e.quantidade_series, e.numero_repeticoes, e.peso, e.tempo_descanso FROM treino_exercicio te JOIN exercicios e ON e.id_exercicio = te.id_exercicio JOIN treinos t ON t.id_treino = te.id_treino WHERE t.id_treino = %s ORDER BY e.id_exercicio;", [id_treino])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar exercícios do treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_exercicio_aluno(id_treino: int, id_exercicio: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM treino_exercicio WHERE id_treino = %s AND id_exercicio = %s;", [id_treino, id_exercicio])
        conexao.commit()
        nome_exercicio = listar_nome_exercicio(id_exercicio, "id_exercicio")

        for nome in nome_exercicio:
            print(f"Exercício '{nome[0]}' deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar exercício: {e}")
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