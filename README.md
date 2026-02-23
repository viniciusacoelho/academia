![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue?logo=postgresql) ![License](https://img.shields.io/badge/License-MIT-green)

# 🏋️‍♂️ Sistema de Gerenciamento de Academia

## 🐍 Sobre o Projeto

O **Sistema de Gerenciamento de Academia** é uma aplicação desenvolvida para auxiliar no controle e organização de uma academia, permitindo o gerenciamento de alunos, instrutores, planos, treinos e exercícios de forma estruturada.

O projeto foi construído com foco em **organização de código, separação de responsabilidades e boas práticas de arquitetura**, seguindo uma estrutura modular para facilitar manutenção e escalabilidade.

---

## 📌 Funcionalidades Principais

### 💳 Planos

* CRUD completo de planos
* Definição de nome, tipo (Mensal, Semestral, Anual) e preço
* Associação plano ↔ aluno
* Visualizar, assinar ou cancelar plano

### 📋 Treinos

* CRUD completo de treinos
* Associação treino ↔ exercício
* Visualização dos treinos com os exercícios e aluno vinculados

### 🏋️ Exercícios

* CRUD completo de exercícios
* Listagem de exercícios
* Navegação otimizada no painel

### 🧑‍🏫 Instrutores

* CRUD completo de instrutores
* Criação de conta e login
* Cadastro de treinos e exercícios
* Associação de exercícios aos treinos

### 👤 Alunos

* CRUD completo de alunos
* Criação de conta e login
* Visualização de treinos, exercícios e instrutor vinculados

---

Perfeito ✅
Você pode adicionar esta seção ao seu README:

---

## 🗄️ Banco de Dados

O sistema utiliza **PostgreSQL** como banco de dados relacional, organizado para manter a integridade e o relacionamento entre alunos, instrutores, treinos, exercícios e planos.

### 📋 Estrutura das Tabelas

* alunos
* instrutores
* planos
* exercicios
* treinos
* plano_aluno (tabela associativa)
* treino_exercicio (tabela associativa)

---

### 🔐 Relacionamentos

* Um aluno possui um plano
* Um instrutor pode cadastrar vários exercícios e treinos
* Um treino pode conter vários exercícios
* Um aluno pode possuir vários treinos

---

## 🏗️ Estrutura do Projeto

O projeto segue uma arquitetura organizada em camadas:

```
academia/
│
├── config/        # Configurações do sistema
├── model/         # Modelos e regras de negócio
├── repository/    # Acesso ao banco de dados
├── service/       # Regras e lógica de aplicação
├── util/          # Funções utilitárias
├── view/          # Menus e interação com usuário
├── .gitignore
├── LICENSE
├── main.py        # Arquivo principal do sistema
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **PostgreSQL**
* **psycopg2** (conexão com banco de dados PostgreSQL)
* **bcrypt** (criptografia de senhas)
* **re** (validação com expressões regulares)
* **datetime** (manipulação de datas)
* **msvcrt** (input com asterisco)
* **os** (limpeza de tela)

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o sistema:

```bash
python main.py
```

---

## 🎯 Objetivos do Projeto

* Praticar organização de projetos em Python
* Aplicar separação de camadas (Config, Model, Repository, Service, Util, View)
* Trabalhar com banco de dados relacional
* Melhorar lógica de programação
* Simular um sistema real de academia

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

---

## 👨‍💻 Autor

Desenvolvido por **Vinícius Araújo Coêlho** 
Estudante de Sistemas de Informação

---