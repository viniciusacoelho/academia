from config.banco_de_dados_config import criar_conexao
from repository.exercicios_repository import listar_nome_exercicio

def cadastrar_treino_exercicio(id_treino: int, id_exercicio: int):
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

def listar_treino_exercicio(id_treino: int) -> list | None:
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

def deletar_treino_exercicio(id_exercicio: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM treino_exercicio WHERE id_exercicio = %s;", [id_exercicio])
        conexao.commit()
        nome_exercicio = listar_nome_exercicio(id_exercicio, "id_exercicio")

        for nome in nome_exercicio:
            print(f"Exercício '{nome[0]}' deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar exercício: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_treino_exercicio_join(id_treino: int) -> list | None:
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

# TODO: ->
def listar_treino_exercicio_instrutor(id_instrutor: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT te.* FROM treino_exercicio te JOIN treinos t ON t.id_treino = te.id_treino JOIN instrutores i ON i.id_instrutor = t.id_treino WHERE i.id_instrutor = %s ORDER BY id_treino ASC;", [id_instrutor])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar exercícios do instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_treino_exercicio_aluno(id_aluno: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT te.* FROM treino_exercicio te JOIN treinos t ON t.id_treino = te.id_treino JOIN alunos a ON a.id_aluno = t.id_treino WHERE a.id_aluno = %s ORDER BY id_treino ASC;", [id_aluno])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar exercícios do aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

