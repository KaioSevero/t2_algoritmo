import json
import os

# Salva o JSON na mesma pasta do script (funciona independente da pasta aberta no VS Code)
ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "livros.json")


# ---------- ARQUIVO ----------
def carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # primeira execução: ainda não existe arquivo
    except json.JSONDecodeError:
        print("Arquivo com problema, começando vazio.")
        return []


def salvar(livros):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(livros, f, ensure_ascii=False, indent=4)
    except OSError:
        print("Erro ao salvar o arquivo!")


# ---------- VALIDAÇÃO ----------
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Campo obrigatório.")


def ler_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 0:
                print("Digite um número positivo.")
            else:
                return numero
        except ValueError:
            print("Digite um número inteiro válido.")


def buscar(livros, codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            return livro
    return None


# ---------- FUNCIONALIDADES ----------
def cadastrar(livros):
    codigo = ler_inteiro("Código: ")
    if buscar(livros, codigo) is not None:
        print("Já existe um livro com esse código.")
        return
    livro = {
        "codigo": codigo,
        "titulo": ler_texto("Título: "),
        "autor": ler_texto("Autor: "),
        "ano": ler_inteiro("Ano: "),
    }
    livros.append(livro)
    salvar(livros)
    print("Livro cadastrado!")


def listar(livros):
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(livro["codigo"], "-", livro["titulo"], "-", livro["autor"], "-", livro["ano"])


def consultar(livros):
    codigo = ler_inteiro("Código do livro: ")
    livro = buscar(livros, codigo)
    if livro is None:
        print("Livro não encontrado.")
    else:
        print(livro["codigo"], "-", livro["titulo"], "-", livro["autor"], "-", livro["ano"])


def alterar(livros):
    codigo = ler_inteiro("Código do livro: ")
    livro = buscar(livros, codigo)
    if livro is None:
        print("Livro não encontrado.")
        return
    livro["titulo"] = ler_texto("Novo título: ")
    livro["autor"] = ler_texto("Novo autor: ")
    livro["ano"] = ler_inteiro("Novo ano: ")
    salvar(livros)
    print("Livro alterado!")


def excluir(livros):
    codigo = ler_inteiro("Código do livro: ")
    livro = buscar(livros, codigo)
    if livro is None:
        print("Livro não encontrado.")
        return
    livros.remove(livro)
    salvar(livros)
    print("Livro excluído!")


# ---------- PROGRAMA PRINCIPAL ----------
def main():
    livros = carregar()
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Consultar")
        print("4 - Alterar")
        print("5 - Excluir")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar(livros)
        elif opcao == "2":
            listar(livros)
        elif opcao == "3":
            consultar(livros)
        elif opcao == "4":
            alterar(livros)
        elif opcao == "5":
            excluir(livros)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()