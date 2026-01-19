import psycopg2

def criar_conexao():
    try:
        conexao = psycopg2.connect(
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