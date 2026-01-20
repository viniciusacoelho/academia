from banco_de_dados.criar_conexao import criar_conexao

def cadastrar_treino(tipo: str, nome_exercicio: str, peso: int, repeticoes: int, series: int, tempo_descanso: str, id_aluno: int, id_instrutor: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO treinos (tipo, nome_exercicio, peso, repeticoes, series, tempo_descanso, id_aluno, id_instrutor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [tipo, nome_exercicio, peso, repeticoes, series, tempo_descanso, id_aluno, id_instrutor])    
        conexao.commit()
        print("Treino cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_treinos() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treinos")
        conexao.commit()
        # print("treinos listados com sucesso!")
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
        cursor.execute("SELECT * FROM treinos WHERE nome = %s", [f"%{nome}%"])    
        conexao.commit()
        print("Treino buscado com sucesso!")
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_treino(id_treino, parametro_atributo: str | int, atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE treinos SET {atributo} = %s WHERE id_treino = %s", [parametro_atributo, id_treino])    
        conexao.commit()
        print(f"{atributo} de treino atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_treino(id_treino: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM treinos WHERE id = %s", [id_treino])
        conexao.commit()
        # print(f"Treino {nome} deletado com sucesso!")
        print("Treino deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar treino: {e}")
    finally:
        cursor.close()
        conexao.close()