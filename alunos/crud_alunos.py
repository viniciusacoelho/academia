from banco_de_dados.criar_conexao import criar_conexao
from criptografia.criptografar import criptografar, checar_senha

def cadastrar_aluno(nome: str, email: str, altura: float, peso: float, data_nacimento: str, senha: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)

        cursor.execute("INSERT INTO alunos (nome, email, altura, peso, data_nascimento, senha) VALUES (%s, %s, %s, %s, %s, %s);", [nome, email, altura, peso, data_nacimento, senha])
        conexao.commit()
        print(f"Aluno '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_aluno(email: str, senha: str) -> tuple | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE email = %s;", [email])    
        aluno = cursor.fetchone()

        if aluno and checar_senha(senha, bytes(aluno[6])):
            print("Aluno autenticado com sucesso!")
            return aluno

    except Exception as e:
        print(f"[ERRO]: Falha ao autenticar aluno: {e}")
        return None

    finally:
        cursor.close()
        conexao.close()

def listar_alunos() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos ORDER BY id_aluno;")
        conexao.commit()
        # print("Alunos listados com sucesso!")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar alunos: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_aluno(email: str)  -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE email LIKE %s;", [f"%{email}%"])
        conexao.commit()
        nome_aluno = listar_nome_aluno(email, "email")

        for nome in nome_aluno:
            print(f"Aluno '{nome[0]}' buscado com sucesso!")

        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_aluno(id_aluno: int, parametro_atributo: str | float, atributo: str, nome_atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE alunos SET {atributo} = %s WHERE id_aluno = %s;", [parametro_atributo, id_aluno])
        conexao.commit()
        nome_aluno = listar_nome_aluno(id_aluno, "id_aluno")

        for nome in nome_aluno:
            print(f"{nome_atributo} de aluno '{nome[0]}' atualizado com sucesso!")

    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar {atributo} de aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_aluno(id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM alunos WHERE id_aluno = %s;", [id_aluno])
        nome_aluno = listar_nome_aluno(id_aluno, "id_aluno")

        for nome in nome_aluno:
            print(f"Aluno '{nome[0]}' buscado com sucesso!")

        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_nome_aluno(id_aluno: int, atributo: str) -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome FROM alunos WHERE {atributo} = %s;", [id_aluno])
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar nome do aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

