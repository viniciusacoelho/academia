from util.limpar_tela_util import limpar_tela
from view.administrador_view import login_administrador
from view.alunos_view.menu_aluno import menu_aluno
from view.instrutores_view.menu_instrutor import menu_instrutor

while True:
    limpar_tela()

    print("--------------------------------------------\n                  Academia\n--------------------------------------------")
    print("Identifique-se\n")
    menu = ["Administrador", "Aluno", "Instrutor", "Sair"]

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    try:
        print("--------------------------------------------")
        opcao = int(input("Digite uma opção: "))

        match opcao:
            case 1: login_administrador()
            case 2: menu_aluno()
            case 3: menu_instrutor()
            case 4:
                print("Saindo...")
                limpar_tela()
                print("--------------------------------------------\n                Desenvolvedor\n--------------------------------------------")
                print("LinkedIn: https://www.linkedin.com/in/viniciusacoelho/")
                print("GitHub: https://github.com/viniciusacoelho")
                print("--------------------------------------------")
                break
            case _:
                print("Opção inválida! Tente novamente.")

    except ValueError:
        print("[ERRO]: Digite um número!")

"""
    Fazer esse nas férias, juntando Python com PostgreSQL:
    Academia - planos, alunos, treinos, instrutores.

    Em uma academia, você encontra diferentes planos de assinatura, como mensal ou trimestral, e modelos de gestão de alunos (com sistemas de controle e atendimento), além de diversas opções de treinos, elaborados por instrutores que também orientam e monitoram o aluno durante o uso dos equipamentos para garantir segurança e eficácia. 
    Planos
    Tipos: Existem planos mensais, sem fidelidade, que oferecem maior flexibilidade ao aluno, mas resultam em maior custo. 
    Benefícios: Alguns planos oferecem acesso a todas as aulas coletivas, à estrutura da academia, a programas de bem-estar ou a mais de uma unidade da rede. 
    Exemplos: Algumas redes de academia oferecem planos com diferentes níveis de acesso, como a Bluefit, que tem planos com valores diferentes e acesso a aulas coletivas e à estrutura da academia. 
    Alunos 
    Gerenciamento: Sistemas de gestão de academias, como o Next Fit, ajudam a controlar os alunos, gerenciar seus treinos e agendamentos.
    Atendimento: Os instrutores se dedicam a criar um bom relacionamento com os alunos, focando no atendimento e na orientação personalizada.
    Treinos
    Elaboração: A ficha de treino é a parte central do plano de treino e contém informações sobre exercícios, séries, repetições, cargas e tempo de descanso. 
    Personalização: Os instrutores podem montar treinos personalizados de acordo com os objetivos de cada aluno. 
    Instrutores
    Função: O instrutor é o profissional que acompanha os alunos, orienta a execução correta dos exercícios e garante a segurança para evitar lesões. 
    Disponibilidade: Eles estão disponíveis para ajudar e orientar, além de montarem o treino de cada aluno para o atingimento de seus objetivos.

    Instrutor cadastrar treino para o aluno.

    E colocar todos os exercícios A, AB, ABC, ABCD, ABCDE

    Fazer com o pgadmin4 e só join, sem o inner

    Plano: nome, descrição e preço

    Quando o cliente pagar o plano ele mostra o dia e a hora que foi pago, cobrar o pagamento se passar o dia (e ficar bloqueado o treino).

    Outro tipo de docstring

    Usar o pgadmin4

    Treino
    Exercício, peso, tempo de descanso, series
    Aparecer o instrutor tbm

    O aluno pode editar o treino (repetições, peso, tempo de descanço, quantas séries), menos o exercício.

    Colocar senha com * quando o usuário digita.

    Ter histórico de treinos feitos do aluno no projeto de academia

    Quantidade de alunos geral matriculados na academia

    Treino tem dia/hora de começo e fim e o tempo de treino

    Academia: horário de funcionamento, endereço
"""