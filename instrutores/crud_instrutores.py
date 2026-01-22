from banco_de_dados.criar_conexao import criar_conexao
from criptografia.criptografar import criptografar, checar_senha

def cadastrar_instrutor(nome: str, email: str, cpf: str, senha: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)

        cursor.execute("INSERT INTO instrutores (nome, email, cpf, senha) VALUES (%s, %s, %s, %s);", [nome, email, cpf, senha])    
        conexao.commit()
        print("Instrutor cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_instrutor(email: str, senha: str):
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

def listar_instrutores() -> list | None:
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM instrutores;")
        conexao.commit()
        # print("Instrutores listados com sucesso!")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar instrutores: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_instrutor(email: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM instrutores WHERE email = %s;", [f"%{email}%"])    
        conexao.commit()
        print("Instrutor buscado com sucesso!")
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_instrutor(id_instrutor: int, parametro_atributo: str, atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE instrutores SET {atributo} = %s WHERE id_instrutor = %s;", [parametro_atributo, id_instrutor])    
        conexao.commit()
        print(f"{atributo} de instrutor atualizado com sucesso!")
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
        # print(f"instrutor {nome} deletado com sucesso!")
        print("Instrutor deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar instrutor: {e}")
    finally:
        cursor.close()
        conexao.close()