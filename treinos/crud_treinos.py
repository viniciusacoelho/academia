from banco_de_dados.criar_conexao import criar_conexao
from criptografia.criptografar import criptografar, checar_senha

def cadastrar_treino(tipo: str, quantidade_exercicios: int, nome_exercicio: str, peso: float, repeticoes: int, tempo_descanco: str, series: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO treinos (tipo, quantidade_exercicios, nome_exercicio, peso, repeticoes, series, tempo_descanso) VALUES (%s, %s, %s, %s, %s, %s, %s)", [tipo, quantidade_exercicios, nome_exercicio, peso, repeticoes, tempo_descanco, series])    
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

def atualizar_treino(atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE {atributo} FROM treinos")    
        conexao.commit()
        print(f"{atributo} de treino atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_treino(id: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM treinos WHERE id = %s", id)    
        conexao.commit()
        # print(f"Treino {nome} deletado com sucesso!")
        print("Treino deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar treino: {e}")
    finally:
        cursor.close()
        conexao.close()