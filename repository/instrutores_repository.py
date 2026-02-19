from config.banco_de_dados_config import criar_conexao
from config.criptografia_config import criptografar, checar_senha

def cadastrar_instrutor(nome: str, email: str, cpf: str, senha: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)

        cursor.execute("INSERT INTO instrutores (nome, email, cpf, senha) VALUES (%s, %s, %s, %s);", [nome, email, cpf, senha])
        conexao.commit()
        print(f"Instrutor {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_instrutores() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM instrutores ORDER BY id_instrutor;")
        conexao.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar instrutores: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_instrutor(id_instrutor: int, parametro_atributo: str, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE instrutores SET {atributo} = %s WHERE id_instrutor = %s;", [parametro_atributo, id_instrutor])
        conexao.commit()
        nome_instrutor = listar_nome_instrutor(id_instrutor, "id_instrutor")

        for nome in nome_instrutor:
            print(f"{nome_atributo} de instrutor '{nome[0]}' atualizado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_instrutor(id_instrutor: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM instrutores WHERE id = %s;", [id_instrutor])
        conexao.commit()
        nome_instrutor = listar_nome_instrutor(id_instrutor, "is_instrutor")

        for nome in nome_instrutor:
            print(f"Instrutor '{nome[0]}' deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_instrutor(email: str, senha: str) -> tuple | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM instrutores WHERE email = %s;", [email])
        instrutor = cursor.fetchone()

        if instrutor and checar_senha(senha, bytes(instrutor[4])):
            print("Instrutor autenticado com sucesso!")
            return instrutor

    except Exception as e:
        print(f"[ERRO]: Falha ao autenticar instrutor: {e}")
        return None
    finally:
        cursor.close()
        conexao.close()

def buscar_instrutor(email: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM instrutores WHERE email LIKE %s;", [f"%{email}%"])
        conexao.commit()
        nome_instrutor = listar_nome_instrutor(email, "email")

        for nome in nome_instrutor:
            print(f"Instrutor '{nome[0]}' buscado com sucesso!")

        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_aluno_instrutor(id_instrutor: int) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome FROM treinos t JOIN alunos a ON a.id_aluno = t.id_aluno ORDER BY a.id_aluno WHERE id_instrutor = %s;", [id_instrutor])
        conexao.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar instrutores: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_nome_instrutor(id_instrutor: int, atributo: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome FROM instrutores WHERE {atributo} = %s;", [id_instrutor])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar nome do instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()