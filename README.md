# Sistema de Biblioteca

Atividade Avaliativa T2 – Linguagem de Programação I

Sistema em Python, executado pelo terminal, para gerenciar o acervo de livros de uma biblioteca. Ele permite cadastrar, listar, consultar, alterar e excluir livros, e salva os dados em um arquivo JSON. Assim, os registros continuam disponíveis depois que o programa é fechado e aberto de novo.

## Integrantes

- NOME DO INTEGRANTE 1
- NOME DO INTEGRANTE 2
- NOME DO INTEGRANTE 3

## Funcionalidades

| Opção | Funcionalidade | Descrição |
|---|---|---|
| 1 | Cadastrar | Adiciona um livro com código, título, autor e ano. Não permite códigos repetidos. |
| 2 | Listar | Mostra todos os livros cadastrados. |
| 3 | Consultar | Busca um livro pelo código. |
| 4 | Alterar | Localiza um livro pelo código e atualiza título, autor e ano. |
| 5 | Excluir | Remove um livro pelo código. |
| 0 | Sair | Encerra o programa. |

Além disso, o sistema tem:

- **Persistência em arquivo.** Toda alteração é gravada em `livros.json`, que é lido sempre que o programa inicia.
- **Tratamento de erros.** Usa `try`/`except` para arquivo inexistente (primeira execução), arquivo JSON corrompido e falha ao salvar.
- **Validação de entradas.** Campos de texto não podem ficar vazios, e campos numéricos aceitam apenas inteiros não negativos. Quando a entrada é inválida, o programa pede o valor de novo em vez de encerrar.

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa. São usados só os módulos `json` e `os`, que já vêm com o Python.

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/T2_algoritmo.git
   cd T2_algoritmo
   ```

2. Execute o programa:

   ```bash
   python biblioteca.py
   ```

   No Windows, se o comando `python` não funcionar, use `py biblioteca.py`.

3. Digite o número da opção desejada no menu.

**No VS Code:** abra a pasta do projeto (File → Open Folder), abra o `biblioteca.py` e clique em ▶ (Run Python File). Se aparecer "Restricted Mode", confie na pasta para liberar a execução.

## Estrutura do projeto

```
T2_algoritmo/
├── biblioteca.py   # código-fonte do sistema
├── livros.json     # arquivo de dados (criado automaticamente)
└── README.md       # este arquivo
```

O arquivo `livros.json` é salvo na mesma pasta do `biblioteca.py`, não importa de qual pasta o programa seja executado. Se ele não existir, o sistema começa com a lista vazia e cria o arquivo no primeiro cadastro.

Exemplo de conteúdo:

```json
[
    {
        "codigo": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899
    }
]
```

## Organização do código

| Seção | Funções | Responsabilidade |
|---|---|---|
| Arquivo | `carregar`, `salvar` | Leitura e escrita do JSON |
| Validação | `ler_texto`, `ler_inteiro` | Entrada de dados com validação |
| Busca | `buscar` | Localiza um livro pelo código |
| Funcionalidades | `cadastrar`, `listar`, `consultar`, `alterar`, `excluir` | Operações do sistema |
| Principal | `main` | Menu e laço principal |

Os livros ficam em memória como uma **lista de dicionários**, e cada dicionário representa um livro.
