from classes.usuario import Usuario


class Conta:
    def __init__(self, numero_conta, usuario: Usuario):
        self.agencia: str = "0001"
        self.numero_conta: int = numero_conta
        self.saldo: float = 0.0
        self.limite_saque: int = 3
        self.usuario: Usuario = usuario
        self.transacoes = []

    def saque(self, valor: float):
        if self.limite_saque > 0:
            self.saldo -= valor
            self.limite_saque -= 1
            self.transacoes.append(f"Saque: R$ -{valor:.2f}")
            print(f"Saque realizado! Seu novo saldo é: R$ {self.saldo:.2f}\nVocê tem {self.limite_saque} saques disponíveis.")
        else:
            print("Limite de saque excedido.")

    def deposito(self, valor: float):
        if valor <= 500:
            self.transacoes.append(f"Depósito: R$ +{valor:.2f}")
            self.saldo += valor
            print(f"Depósito realizado! Seu novo saldo é: R$ {self.saldo:.2f}")
        else:
            print("Valor máximo para depósito: R$ 500.00")

    def ver_saldo(self):
        return self.saldo
    
    def imprimir_extrato(self):
        print("....::::EXTRATO::::....")
        for transacao in self.transacoes:
            print(f"{transacao}")

    def __str__(self):
        return (f'Agência: {self.agencia},  '
                f'Número da Conta: {self.numero_conta}, '
                f'Saldo: {self.saldo:.2f}, '
                f'Limite de Saque: {self.limite_saque},  '
                f'[Usuário: {self.usuario}]')
