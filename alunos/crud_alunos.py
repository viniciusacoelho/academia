from banco_de_dados.criar_conexao import criar_conexao
from criptografia.criptografar import criptografar, checar_senha

def cadastrar_aluno(nome: str, email: str, altura: float, peso: float, data_nacimento: str, senha: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)

        cursor.execute("INSERT INTO alunos (nome, email, altura, peso, data_nascimento, senha) VALUES (%s, %s, %s, %s, %s, %s)", [nome, email, altura, peso, data_nacimento, senha])    
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_aluno(email: str, senha: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        # if checar_senha(senha):


        cursor.execute("SELECT FROM alunos WHERE email = %s AND senha = %s", [email, senha])    
        conexao.commit()
        print("Aluno autenticado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao autenticar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_alunos() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        conexao.commit()
        # print("Alunos listados com sucesso!")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar alunos: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_aluno(nome: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE nome = %s", [f"%{nome}%"])    
        conexao.commit()
        print("Aluno buscado com sucesso!")
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_aluno(atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE {atributo} FROM alunos")    
        conexao.commit()
        print(f"{atributo} de aluno atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_aluno(id: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM alunos WHERE id = %s", id)    
        conexao.commit()
        # print(f"aluno {nome} deletado com sucesso!")
        print("Aluno deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()