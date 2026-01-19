import bcrypt

def criptografar(senha: str) -> bytes:
    senha_bytes = senha.encode("UTF-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bytes, salt)
    return hashed

def checar_senha(senha: bytes | str, hashed: bytes) -> bytes:
    senha_bytes = senha.encode("UTF-8")
    return bcrypt.checkpw(senha_bytes, hashed)