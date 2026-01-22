from bcrypt import gensalt, hashpw, checkpw

def criptografar(senha: str) -> bytes:
    senha_bytes = senha.encode("UTF-8")
    salt = gensalt()
    hashed = hashpw(senha_bytes, salt)
    return hashed

def checar_senha(senha: bytes | str, hashed: bytes) -> bytes:
    senha_bytes = senha.encode("UTF-8")
    return checkpw(senha_bytes, hashed)