from limpar_tela.limpar_tela import limpar_tela
from datetime import datetime

def pagamento():
    while True:    
        limpar_tela()
        print("--------------------------------------------\n            Pagamento\n--------------------------------------------")

        menu = ["Crédito", "Débito", "Dinheiro", "Pix", "Boleto"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            # metodo_pagamento = menu[opcao]
            match opcao:
                # case 1 | 2 | 3 | 4 | 5: metodo_pagamento = menu[opcao]
                case 1: metodo_pagamento = "Crédito"
                case 2: metodo_pagamento = "Débito"
                case 3: metodo_pagamento = "Dinheiro"
                case 4: metodo_pagamento = "Pix" # TODO: 10% de desconto do PIX
                case 5: metodo_pagamento = "Boleto"
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

        data_hora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        return metodo_pagamento, data_hora