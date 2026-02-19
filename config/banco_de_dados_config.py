from psycopg2 import connect

def criar_conexao() -> list | None:
    try:
        conexao = connect(
            dbname = "academia",
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "5432"
        )
        return conexao
    except Exception as e:
        print(f"[ERRO]: Falha ao conectar ao banco de dados: {e}")
        return None