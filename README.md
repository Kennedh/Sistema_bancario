# 🏦 Sistema Bancário em Python

## ✨ Descrição
Este projeto faz parte de um desafio proposto pela **DIO (Digital Innovation One)**, onde foi desenvolvido um **Sistema Bancário** utilizando Python. O objetivo principal é implementar três operações essenciais:

- 💳 **Depósito**: Permite ao usuário adicionar dinheiro à sua conta.
- 💸 **Saque**: Possibilita a retirada de dinheiro, respeitando limite de saldo e quantidade de saques diários.
- 📝 **Extrato**: Exibe um histórico das transações realizadas.

O sistema visa simular operações bancárias e proporcionar uma experiência prática com lógica de programação e manipulação de dados.

---

## 🎨 Versão com Interface Gráfica (CustomTkinter)

Além da versão em terminal, o sistema conta agora com uma **interface desktop moderna** desenvolvida com **CustomTkinter**, oferecendo:

- 🌙 **Modo escuro (Dark Mode)** por padrão
- 🖱️ **Interface intuitiva com botões e campos de entrada**
- 👤 **Sistema de login por CPF**
- 📊 **Extrato visual com cores diferenciadas** (verde para depósitos, vermelho para saques)
- 🎨 **Design profissional e arredondado**

---

## 🛠 Tecnologias Utilizadas
- 💻 **Python 3.x**
- 🎮 **Lógica de Programação**
- 🔄 **Estruturas Condicionais e Laços de Repetição**
- 🌐 **Manipulação de Strings e Listas**
- 🧱 **Programação Orientada a Objetos (POO)**
- 🧩 **Classes Abstratas (ABC)**
- 🖼️ **CustomTkinter** - Interface gráfica moderna

---

## 🔢 Regras de Negócio

- ✅ **Depósito**
  - Permitido apenas com valor **positivo**.
  - Depósitos bem-sucedidos são registrados no **histórico da conta**.

- ✅ **Saque**
  - Permitido se houver **saldo suficiente**.
  - Valor deve ser **positivo** e **não exceder R$ 500 por saque**.
  - Máximo de **3 saques por dia**.
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

## 🏗️ Estrutura do Projeto

O sistema foi desenvolvido utilizando **Programação Orientada a Objetos** com as seguintes classes:

| Classe | Descrição |
|--------|------------|
| **Cliente** | Classe base para representação de clientes |
| **PessoaFisica** | Herda de Cliente, adiciona CPF, nome e data de nascimento |
| **Conta** | Classe base para contas bancárias |
| **ContaCorrente** | Herda de Conta, implementa regras específicas como limite de saque |
| **Historico** | Gerencia o registro de transações com data/hora |
| **Transacao** | Classe abstrata para diferentes tipos de transações |
| **Saque** | Implementação concreta de saque |
| **Deposito** | Implementação concreta de depósito |
| **BancoApp** | Interface gráfica com CustomTkinter (nova versão) |

---

## 🚀 Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Execute o arquivo principal: `python sistema_bancario.py`
3. Siga as opções do menu interativo

---

## 📌 Atualizações
- ✔️ Refatoração completa para **POO** com classes `Cliente`, `Conta`, `Transação`, entre outras.
- ✔️ Sistema de **histórico de transações com data/hora**.
- ✔️ Regras mais rígidas para saque e depósitos.
- ✔️ Organização das responsabilidades em métodos e classes para facilitar manutenção e testes futuros.
- ✔️ Correção de imports e decoradores abstratos.
- ✔️ Correção do formato de data no histórico de transações.
- ✔️ Implementação correta do limite de saques diários.

---

## ⚠️ Correções Realizadas

### v1.0.1
- Corrigido import de `ABC` e `abstractmethod`
- Ajustado formato de data no extrato (`%S` maiúsculo para segundos)
- Atualizada documentação para refletir regra de "3 saques por dia"
- Removidos códigos FIXME e comentários desatualizados

### v2.0.0 (Interface Gráfica)
- Adicionada interface desktop com CustomTkinter
- Sistema de login por CPF
- Extrato visual com cores diferenciadas
- Modo escuro como padrão
- Validação de campos em tempo real
