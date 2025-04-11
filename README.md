# 🏦 Sistema Bancário em Python

## ✨ Descrição
Este projeto faz parte de um desafio proposto pela **DIO (Digital Innovation One)**, onde foi desenvolvido um **Sistema Bancário** utilizando Python. O objetivo principal é implementar três operações essenciais:

- 💳 **Depósito**: Permite ao usuário adicionar dinheiro à sua conta.
- 💸 **Saque**: Possibilita a retirada de dinheiro, respeitando limite de saldo e quantidade de saques diários.
- 📝 **Extrato**: Exibe um histórico das transações realizadas.

O sistema visa simular operações bancárias e proporcionar uma experiência prática com lógica de programação e manipulação de dados.

---

## 🛠 Tecnologias Utilizadas
- 💻 **Python 3.x**
- 🎮 **Lógica de Programação**
- 🔄 **Estruturas Condicionais e Laços de Repetição**
- 🌐 **Manipulação de Strings e Listas**
- 🧱 **Programação Orientada a Objetos (POO)**

---

## 🔢 Regras de Negócio

- ✅ **Depósito**
  - Permitido apenas com valor **positivo**.
  - Depósitos bem-sucedidos são registrados no **histórico da conta**.

- ✅ **Saque**
  - Permitido se houver **saldo suficiente**.
  - Valor deve ser **positivo** e **não exceder R$ 500 por saque**.
  - Máximo de **3 saques por conta**.
  - Saques válidos são registrados no **histórico da conta**.

- ✅ **Extrato**
  - Mostra todas as transações realizadas (saques e depósitos).
  - Exibe também o **saldo atual** da conta.
  - Inclui **data e hora** de cada transação.

- ✅ **Clientes e Contas**
  - Cada cliente pode ter **múltiplas contas**.
  - No momento, o sistema **utiliza sempre a primeira conta do cliente**.
  - Cada conta possui um **histórico individual de transações**.

---

## 📌 Atualizações
- ✔️ Refatoração completa para **POO** com classes `Cliente`, `Conta`, `Transação`, entre outras.
- ✔️ Sistema de **histórico de transações com data/hora**.
- ✔️ Regras mais rígidas para saque e depósitos.
- ✔️ Organização das responsabilidades em métodos e classes para facilitar manutenção e testes futuros.
