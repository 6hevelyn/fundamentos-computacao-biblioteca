# 📚 Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido para a disciplina de Fundamentos de Computação da Universidade Federal do Maranhão (UFMA).

## Objetivo

O sistema permite o gerenciamento de livros através das operações CRUD (Create, Read, Update e Delete), além da geração de relatórios analíticos para auxiliar no controle do acervo.

## Funcionalidades

✅ Cadastro de livros

✅ Consulta por ID

✅ Consulta por título

✅ Consulta por categoria

✅ Atualização de registros

✅ Exclusão de registros

✅ Relatórios estatísticos

✅ Persistência em arquivo CSV

## Tecnologias Utilizadas

* Python 3
* CSV
* Programação Estruturada
* Arquitetura Modular

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```text
Sistema_Biblioteca/

│
├── main.py                     # Ponto de entrada da aplicação
│                               # Menu principal do sistema
│
├── controller.py               # Regras de negócio
│                               # CRUD e geração de relatórios
│
├── persistence.py              # Manipulação dos dados
│                               # Leitura e gravação do arquivo CSV
│
├── livros.csv                  # Banco de dados do sistema
│                               # Armazena todos os livros cadastrados
│
├── README.md                   # Documentação do sistema
│
└── .gitignore                  # Arquivos ignorados pelo GitHub
```

## 🦉 Descrição dos Comandos Principais

O sistema funciona através de um menu numérico interativo no terminal. Abaixo estão as funcionalidades disponibilizadas em cada opção:

### 1. Cadastrar Livro
Inicia o formulário de cadastro solicitando ID, Título, Autor, Categoria, Ano e Quantidade.

**Validações:**
- ID único
- Título obrigatório
- Autor obrigatório
- Ano maior que zero
- Quantidade não negativa

### 2. Consultar Livro
Permite localizar livros através de:
- ID
- Título
- Categoria

### 3. Atualizar Livro
Permite alterar os dados de um livro existente, mantendo o cadastro sempre atualizado.

### 4. Excluir Livro
Remove permanentemente um livro do sistema após confirmação do usuário.

### 5. Relatórios
Disponibiliza análises do acervo:

- Total de livros cadastrados
- Total de exemplares
- Média de exemplares por livro
- Quantidade por categoria
- Livro mais antigo
- Ranking dos livros com mais exemplares
- Listagem em ordem alfabética

### 6. Listar Todos
Exibe todos os livros cadastrados juntamente com suas informações completas.

## Como Executar

python main.py

## Autores

* Hevelyn Fenanda
* Paula Angela
* Vitória dos Reis
* Universidade Federal do Maranhão (UFMA)
