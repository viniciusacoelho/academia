from repository.instrutores_repository import listar_instrutores

def identificar_instrutor(atributo: int, posicao: int):
    instrutores = listar_instrutores()

    for instrutor in instrutores:
        if atributo == instrutor[posicao]:
            return True

    return False

def selecionar_instrutor():
    try:
        id_instrutor = int(input("Digite o ID do instrutor: "))
        instrutor_identificado = identificar_instrutor(id_instrutor, 0)

        if instrutor_identificado:
            return id_instrutor
        else:
            print("ID do instrutor inválido! Tente novamente.")
            return False

    except ValueError:
        print("[ERRO]: Digite um número!")
        return False