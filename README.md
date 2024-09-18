# DESAFIO 3 | MODELANDO O SISTEMA BANCÁRIO EM POO COM PYTHON

Este projeto implementa um sistema bancário básico em Python, permitindo criar usuários, abrir contas e realizar operações bancárias como saques, depósitos e exibição de extratos.

## 🔧 FUNCIONALIDADES


- **Criação de Usuário**: Crie novos usuários com nome, CPF, data de nascimento e endereço.
- **Abertura de Conta**: Abra contas bancárias para os usuários registrados, vinculando contas a um usuário existente.
- **Operações Bancárias**:
  - Realize saques com limite diário.
  - Faça depósitos com um valor máximo permitido.
  - Verifique o saldo da conta.
  - Imprima um extrato das transações realizadas.

## 💻REQUISITOS

Este projeto é um script Python simples, sem dependências externas, exceto o Python 3.x.

## Estrutura de Arquivos


O projeto está estruturado em dois principais módulos:

1. `Conta` - Representa uma conta bancária.
2. `Usuario` - Representa um usuário do banco.

```bash
├── classes/
│   ├── conta.py    # Implementação da classe Conta
│   └── usuario.py  # Implementação da classe Usuario
└── main.py         # Lógica principal do sistema bancário
```

## Contribuições

Sinta-se à vontade para sugerir melhorias ou correções. Você pode abrir uma issue ou fazer um pull request neste repositório.
