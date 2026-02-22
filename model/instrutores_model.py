from repository.instrutores_repository import listar_instrutores

def selecionar_instrutor():
    from view.instrutores_view.menu_instrutor_administrador import imprimir_instrutores
    quantidade_instrutores = len(listar_instrutores())

    if quantidade_instrutores == 0:
        print("Nenhum instrutor cadastrado anteriormente.")
    else:
        imprimir_instrutores()

        try:
            id_instrutor = int(input("Digite o ID do instrutor para atualizar: "))
            instrutor_identificado = identificar_instrutor(id_instrutor, 0)

            if instrutor_identificado:
                return id_instrutor
            else:
                return "ID do instrutor inválido! Tente novamente."

        except ValueError:
            return "[ERRO]: Digite um número!"

def selecionar_instrutor():
    from view.instrutores_view.menu_instrutor_administrador import imprimir_instrutores
    quantidade_instrutores = len(listar_instrutores())

    if quantidade_instrutores == 0:
        print("Nenhum instrutor cadastrado anteriormente.")
    else:
        imprimir_instrutores()

        try:
            id_instrutor = int(input("Digite o ID do instrutor: "))
            instrutor_identificado = identificar_instrutor(id_instrutor, 0)

            if instrutor_identificado:
                return id_instrutor
            else:
                return "ID do instrutor inválido! Tente novamente."

        except ValueError:
            return "[ERRO]: Digite um número!"

def identificar_instrutor(atributo: int, posicao: int):
    instrutores = listar_instrutores()

    for instrutor in instrutores:
        if atributo == instrutor[posicao]:
            return True

    return False