from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
LIMITE_TRANSACOES = 10

def deposito():
    global saldo
    global extrato
    global LIMITE_TRANSACOES

    while True:
        if LIMITE_TRANSACOES == 10:
            print("Não foi possivel realizar a transação. Limite de transações excedido.")
            break
        deposit = float(input("Insira o valor que você deseja depositar: "))
        if deposit < 0:
            print("Valor inválido, digite o valor correto")
        elif deposit > 5000:
            print("Valor excede o limite de deposito (R$ 5000)")
        else:
            saldo += deposit
            print("Deposito concluido!")
            extrato += f"\nDeposito: R$ {deposit:.2f} Data: {datetime.now().replace(microsecond=0)}"
            LIMITE_TRANSACOES += 1
            break

def saque():
    global saldo
    global limite
    global LIMITE_TRANSACOES
    global extrato

    while True:
        if LIMITE_TRANSACOES == 10:
            print("Não foi possivel realizar a transação. Limite de transações excedido.")
            break
        if saldo == 0:
            print("Você não possui saldo, deposite algum valor para poder sacar.")
            break
        valor = float(input("Insira o valor que deseja sacar:"))
        if valor > saldo:
            print(f"Saldo insuficiente\n\nSaldo Atual: {saldo}")
        elif valor > limite:
            print("Valor maior que limite permitido por saque (R$ 500)")
            break
        elif valor < float(0):
            print("Valor não permitido")
        else:
            saldo -= valor
            print("Saque efetuado com sucesso!")
            extrato += f"\nSaque: R$ {valor:.2f} Data: {datetime.now().replace(microsecond=0)}"
            LIMITE_TRANSACOES += 1
            break

def consulta_extrato():
    print(f"{extrato}\n\nSaldo atual: R$ {saldo:.2f}")

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito()
    elif opcao == "s":
        saque()
    elif opcao == "e":
        consulta_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação não encontrada")