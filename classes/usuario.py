class Usuario:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str):
        self.name = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return (f'Name: {self.name},  '
                f'CPF: {self.cpf}, '
                f'Data de Nascimento: {self.data_nascimento}, '
                f'Endereço: {self.endereco}')
