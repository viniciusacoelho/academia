from limpar_tela.limpar_tela import limpar_tela
from treinos.crud_treinos import listar_treinos, buscar_treino, atualizar_treino, deletar_treino
from treinos.crud_treinos import cadastrar_treino
from treinos.validar_treino import validar_nome, validar_quantidade_exercicios

def menu_treino():
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Menu Treino\n--------------------------------------------")

        menu = ["Cadastrar Treino", "Listar Treinos", "Buscar Treino", "Atualizar Treino", "Deletar Treino", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: registrar_treino()
                case 2:
                    imprimir_treinos()
                    if len(listar_treinos) != 0:
                        print("Treinos listados com sucesso!")
                case 3: procurar_treino()
                case 4: atualizar_treino()
                case 5: remover_treino()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def registrar_treino(id_instrutor: int, id_aluno: int):
    limpar_tela()

    print("--------------------------------------------\n              Cadastrar Treino\n--------------------------------------------")

    while True:
        nome = input("Digite o nome do treino: ")
        nome_valido = validar_nome(nome)

        if nome_valido:
            break
        else:
            print("Nome inválido. Tente novamente.")

    while True:
        menu = ["Empurrar", "Puxar", "Inferior"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            id_tipo_treino = int(input("Digite o ID do tipo de treino: "))
            
            match id_tipo_treino:
                case 1:
                    tipo = "Empurrar"
                    break
                case 2:
                    tipo = "Puxar"
                    break
                case 3:
                    tipo = "Inferior"
                    break
                case _:
                    print("ID de treino inválido! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

    cadastrar_treino(nome, tipo, id_aluno, id_instrutor)

    # while True:
    #     try:
    #         quantidade_exercicios = int(input("Digite a quantidade de exercícios: "))
    #         quantidade_exercicios_validada = validar_quantidade_exercicios(quantidade_exercicios)

    #         if quantidade_exercicios_validada:
    #             break
    #         else:
    #             print("Quantidadde de exercícios inválida! Tente novamente.")
    #     except ValueError:
    #         print("[ERRO]: Digite um número!")

    # for i in range(quantidade_exercicios):
    #     nome_exercicio = input(f"Digite o nome do exercício {i + 1}: ")
    #     peso = int(input(f"Digite o peso do exercício {i + 1}: "))
    #     repeticoes = int(input(f"Digite o número de repetições do exercício {i + 1}: "))
    #     series = int(input(f"Digite a quantidade de séries do exercício {i + 1}: "))
    #     # TODO: Colocar time no tempo de descanço
    #     # tempo_descanso = float(input(f"Digite o tempo de descanso do exercício {i + 1}: "))
    #     tempo_descanso = input(f"Digite o tempo de descanso do exercício {i + 1}: ")

        # cadastrar_treino(tipo, nome_exercicio, peso, repeticoes, series, tempo_descanso, id_aluno, id_instrutor)

def imprimir_treinos():
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        treinos = listar_treinos()

        for treino in treinos:
            print(f"Treino {treino[0]}\nTipo: {treino[1]}\nExercícios: {treino[2]}\nID do Aluno: {treino[3]}\nID do Instrutor: {treino[4]}")
            print("--------------------------------------------")

def procurar_treino():
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        nome = input("Digite o nome do treino para buscar: ")
        treino_identificado = identificar_treino(nome, 1)

        if treino_identificado:
            treino_busca = buscar_treino(nome)
            print("--------------------------------------------")

            for treino in treino_busca:
                print(f"Treino {treino[0]}\nTipo: {treino[1]}\nExercícios: {treino[2]}\nDescrição: {treino[3]}\nTipo: {treino[4]}\nPreço: {treino[5]}")

        else:
            print("Nome do treino inválido! Tente novamente.")

def remover_treino():
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        listar_treinos()
        id_treino = int(input("Digite o ID do treino para deletar: "))
        treino_identificado = identificar_treino(id_treino, 0)

        if treino_identificado:
            deletar_treino(id_treino)
        else:
            print("ID do treino inválido! Tente novamente.")

def identificar_treino(atributo: int, posicao: int):
    treinos = listar_treinos()

    for treino in treinos:
        if atributo == treino[posicao]:
            return True

    return False

# Treinos de academia eficientes combinam musculação (treino de força) com cardio, organizados por divisões como ABC (peito/ombro/tríceps, costas/bíceps, pernas) ou ABCDE para níveis avançados, priorizando exercícios compostos como agachamentos e supinos para maior ganho muscular. A frequência ideal varia entre 3 a 5 dias por semana, incluindo períodos de descanso para recuperação. 
# Estruturas de Treino Comuns
# Iniciante (Full Body): Treinar o corpo inteiro em uma única sessão, 3 vezes na semana, focando em exercícios compostos e adaptação.
# Intermediário/Avançado (ABC):
# A (Peito, Ombro, Tríceps): Supino reto, supino inclinado, desenvolvimento, elevação lateral, pulley, rosca testa.
# B (Costas, Bíceps, Abdômen): Pulley frente, remada fechada, remada aberta, rosca scott/direta.
# C (Pernas): Agachamento, leg press, cadeira extensora, mesa flexora, panturrilha.
# Avançado (ABCDE): Divisão de 5 dias focada em um grupo muscular por dia (ex: Peito, Costas, Ombros, Pernas, Braços). 
# Dicas para Melhores Resultados
# Prioridade: Exercícios multiarticulares (que usam várias articulações) vêm antes dos isolados.
# Cardio: 20-30 minutos de cardio (esteira, elíptico) ou HIIT (15 min) ajudam na queima calórica e condicionamento.
# Execução: Manter o tronco firme, abdômen contraído e técnica correta, especialmente em exercícios de ombro e agachamentos.
# Volume: Geralmente 3 a 4 séries de 10-15 repetições com carga moderada a alta. 
# Exemplo de Rotina Semanal
# Segunda (Sup): Peito, Ombro, Tríceps + 20 min Cardio
# Terça (Inf): Pernas Completo + 15 min HIIT
# Quarta: Descanso Ativo (cardio leve)
# Quinta (Sup): Costas, Bíceps + 20 min Cardio
# Sexta (Inf): Pernas Foco em Glúteo/Posterior
# Sábado/Domingo: Descanso 
# Para emagrecimento, aumentar a intensidade e diminuir o tempo de descanso entre as séries é recomendado, enquanto para ganho de massa, focar na progressão de cargas é essencial. 