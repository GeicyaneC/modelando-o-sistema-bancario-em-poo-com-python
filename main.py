from classes.conta import Conta
from classes.usuario import Usuario
from datetime import datetime

usuarios = []
contas = []
num_contas = 1

def menu_inicial():
    return ("""
:::::::::::::::::::::::::::::
..::Bem-vindo ao Banco Py::..
:::::::::::::::::::::::::::::

Selecione a opção abaixo:

[1] Novo Usuário
[2] Nova Conta
[3] Acessar Conta
[0] Sair

Digite sua escolha: """)


def menu_conta(usuario: str, agencia: str, conta: int):
    return (f"""
    
{datetime.now().strftime('%d.%m.%Y %H:%M')}

Usuário: {usuario}
Agencia: {agencia} 
Conta: {conta}

O que deseja fazer hoje?

[1] Saque
[2] Depósito
[3] Ver Saldo
[4] Imprimir Extrato
[0] Sair

Digite sua escolha: """)


def novo_usuario():
    global usuarios
    usuario = Usuario(input("Nome: "), input("CPF: "), input("Data de Nascimento: "), input("Endereço: "))
    usuarios.append(usuario)
    print(f"Usuário {usuario.name} criado com sucesso!")


def nova_conta(cpf: str):
    global contas, num_contas
    for usuario in usuarios:
        if cpf == usuario.cpf:
            contas.append(Conta(num_contas, usuario))
            num_contas += 1
            print(f"Conta vinculada ao usuário: {usuario.name}")
            return
    print("Usuário não encontrado!")


def acessar_conta(cpf: str) -> Conta | None:
    global contas
    for conta in contas:
        if conta.usuario.cpf == cpf:
            return conta
    return None


def main():
    while True:
        try:
            op = int(input(menu_inicial()))
        except ValueError:
            print("Por favor, insira uma opção válida.")
            continue

        if op == 1:
            novo_usuario()

        elif op == 2:
            nova_conta(input("Informe seu CPF: "))
            input("Pressione Enter para continuar...")

        elif op == 3:
            conta = acessar_conta(input("Informe seu CPF: "))
            if conta is None:
                print("Não foram encontradas contas para o CPF fornecido.")
            else:
                while True:
                    try:
                        op_conta = int(input(menu_conta(conta.usuario.name, conta.agencia, conta.numero_conta)))
                    except ValueError:
                        print("Por favor, insira uma opção válida.")
                        continue

                    if op_conta == 1:
                        try:
                            valor = float(input("Digite o valor do Saque: "))
                            conta.saque(valor)
                        except ValueError:
                            print("Por favor, insira um valor numérico válido.")
                    elif op_conta == 2:
                        try:
                            valor = float(input("Digite o valor do Depósito: "))
                            conta.deposito(valor)
                        except ValueError:
                            print("Por favor, insira um valor numérico válido.")
                    elif op_conta == 3:
                        print(f"Seu saldo é: {conta.ver_saldo()}")
                    elif op_conta == 4:
                        conta.imprimir_extrato()
                    elif op_conta == 0:
                        break
                    else:
                        print("Opção inválida, tente novamente.")
                    input("Pressione Enter para continuar...")

        elif op == 0:
            print("Saindo do sistema. Obrigado por usar o Banco Py!")
            break

        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter para continuar...")

main()
