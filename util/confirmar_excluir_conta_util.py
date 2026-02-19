from repository.alunos_repository import deletar_aluno
from repository.instrutores_repository import deletar_instrutor

def confirmar_excluir_conta(id: int, entidade: str):
    while True:
        resposta = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
        if resposta == "s" or resposta == "sim":
            if entidade == "Aluno":
                deletar_aluno(id)
            elif entidade == "Instrutor":
                deletar_instrutor(id)
            break
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            break
        else:
            print("Resposta inválida! Tente novamente.")