from persistence import carregar_dados

from controller import (
    cadastrar_livro,
    consultar_livro,
    atualizar_livro,
    excluir_livro,
    relatorios
)

def exibir_banner():

    print("""
╔══════════════════════════════════════════════╗
║      📚 SISTEMA DE BIBLIOTECA 📚            ║
║      Fundamentos de Computação - UFMA       ║
╚══════════════════════════════════════════════╝
""")


def exibir_menu():

    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║              MENU PRINCIPAL         ║")
    print("╠══════════════════════════════════════╣")
    print("║ 1 ➜ Cadastrar Livro                 ║")
    print("║ 2 ➜ Consultar Livro                 ║")
    print("║ 3 ➜ Atualizar Livro                 ║")
    print("║ 4 ➜ Excluir Livro                   ║")
    print("║ 5 ➜ Relatórios                      ║")
    print("║ 6 ➜ Listar Todos                    ║")
    print("║ 0 ➜ Sair                            ║")
    print("╚══════════════════════════════════════╝")


def listar_todos(livros):

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    print("\n===== LIVROS CADASTRADOS =====")

    for livro in livros:

        print(
            f"\nID: {livro['id']}"
        )

        print(
            f"Título: {livro['titulo']}"
        )

        print(
            f"Autor: {livro['autor']}"
        )

        print(
            f"Categoria: {livro['categoria']}"
        )

        print(
            f"Ano: {livro['ano']}"
        )

        print(
            f"Quantidade: {livro['quantidade']}"
        )


def main():

    livros = carregar_dados()
    exibir_banner()

    while True:

        exibir_menu()

        opcao = input(
            "\nEscolha uma opção: "
        )

        if opcao == "1":

            cadastrar_livro(livros)

        elif opcao == "2":

            consultar_livro(livros)

        elif opcao == "3":

            atualizar_livro(livros)

        elif opcao == "4":

            excluir_livro(livros)

        elif opcao == "5":

            relatorios(livros)

        elif opcao == "6":

            listar_todos(livros)

        elif opcao == "0":

            print(
                "\nSistema encerrado."
            )

            break

        else:

            print(
                "Opção inválida."
            )


if __name__ == "__main__":
    main()