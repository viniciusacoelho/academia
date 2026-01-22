from psycopg2 import connect

def criar_conexao():
    try:
        conexao = connect(
            dbname = "academia",
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "5432"
        )
        # print("Conexão criada com sucesso!")
        return conexao
    except Exception as e:
        print(f"[ERRO]: Falha ao conectar ao banco de dados: {e}")
        return None