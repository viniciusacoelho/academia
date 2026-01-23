from datetime import datetime

agora = datetime.now()
print(agora)

###

from datetime import date

hoje = date.today()
print(hoje)

###

hora_atual = datetime.now().time()
print(hora_atual)

###

from datetime import datetime

data = datetime(2026, 1, 21, 14, 30, 0)
print(data)

###

agora = datetime.now()

print(agora.year)    # ano
print(agora.month)   # mês
print(agora.day)     # dia
print(agora.hour)    # hora
print(agora.minute)  # minuto

###

agora = datetime.now()

formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
print(formatado)

###

print(agora.strftime("%d/%m/%Y"))

###

from datetime import datetime

texto = "21/01/2026"
data = datetime.strptime(texto, "%d/%m/%Y")
print(data)

###

from datetime import datetime, timedelta

hoje = datetime.now()
amanha = hoje + timedelta(days=1)

print(amanha)

###

ontem = hoje - timedelta(days=1)

###

data1 = datetime(2026, 1, 21)
data2 = datetime(2026, 1, 10)

diferenca = data1 - data2
print(diferenca.days)

###

if data1 > data2:
    print("Data1 é mais recente")

###

from datetime import datetime

print("Login realizado em:", datetime.now().strftime("%d/%m/%Y %H:%M"))

import msvcrt

def input_com_asterisco(mensagem=""):
    print(mensagem, end="", flush=True)
    senha = ""

    while True:
        char = msvcrt.getch()

        if char in {b'\r', b'\n'}:  # Enter
            print()
            break
        elif char == b'\x08':  # Backspace
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        else:
            senha += char.decode("utf-8")
            print("*", end="", flush=True)

    return senha

senha = input_com_asterisco("Digite sua senha: ")
print("Senha capturada!")