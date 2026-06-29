from persistence import salvar_dados


def buscar_por_id(livros, id_livro):

    for livro in livros:

        if livro["id"] == id_livro:
            return livro

    return None


def cadastrar_livro(livros):
    """
    Cadastro de livros.
    """

    try:

        id_livro = int(input("ID: "))

        if buscar_por_id(livros, id_livro):
            print("ERRO: ID já cadastrado.")
            return

        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        categoria = input("Categoria: ").strip()

        ano = int(input("Ano: "))
        quantidade = int(input("Quantidade: "))

        if titulo == "":
            print("Título obrigatório.")
            return

        if autor == "":
            print("Autor obrigatório.")
            return

        if ano <= 0:
            print("Ano inválido.")
            return

        if quantidade < 0:
            print("Quantidade inválida.")
            return

        livro = {
            "id": id_livro,
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "ano": ano,
            "quantidade": quantidade
        }

        livros.append(livro)

        salvar_dados(livros)

        print("Livro cadastrado com sucesso!")

    except ValueError:
        print("Digite apenas números nos campos numéricos.")


def consultar_livro(livros):

    print("\n1 - Buscar por ID")
    print("2 - Buscar por Título")
    print("3 - Buscar por Categoria")

    opcao = input("Escolha: ")

    if opcao == "1":

        try:

            id_livro = int(input("ID: "))

            livro = buscar_por_id(
                livros,
                id_livro
            )

            if livro:
                print(livro)
            else:
                print("Livro não encontrado.")

        except ValueError:
            print("ID inválido.")

    elif opcao == "2":

        titulo = input("Título: ").lower()

        encontrou = False

        for livro in livros:

            if titulo in livro["titulo"].lower():

                print(livro)
                encontrou = True

        if not encontrou:
            print("Nenhum livro encontrado.")

    elif opcao == "3":

        categoria = input("Categoria: ").lower()

        encontrou = False

        for livro in livros:

            if categoria == livro["categoria"].lower():

                print(livro)
                encontrou = True

        if not encontrou:
            print("Nenhum livro encontrado.")


def atualizar_livro(livros):

    try:

        id_livro = int(
            input("Digite o ID do livro: ")
        )

        livro = buscar_por_id(
            livros,
            id_livro
        )

        if not livro:
            print("Livro não encontrado.")
            return

        livro["titulo"] = input(
            "Novo título: "
        )

        livro["autor"] = input(
            "Novo autor: "
        )

        livro["categoria"] = input(
            "Nova categoria: "
        )

        livro["ano"] = int(
            input("Novo ano: ")
        )

        livro["quantidade"] = int(
            input("Nova quantidade: ")
        )

        salvar_dados(livros)

        print("Livro atualizado!")

    except ValueError:
        print("Dados inválidos.")


def excluir_livro(livros):

    try:

        id_livro = int(
            input("ID do livro: ")
        )

        livro = buscar_por_id(
            livros,
            id_livro
        )

        if livro:

            livros.remove(livro)

            salvar_dados(livros)

            print("Livro removido.")

        else:
            print("Livro não encontrado.")

    except ValueError:
        print("ID inválido.")


def relatorios(livros):

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    print("\n📊 RELATÓRIOS DA BIBLIOTECA")
    print("════════════════════════════")

    total_livros = len(livros)

    total_exemplares = sum(
        livro["quantidade"]
        for livro in livros
    )

    media = (
        total_exemplares /
        total_livros
    )

    print(f"📚 Total de livros: {total_livros}")

    print(f"📦 Total de exemplares: {total_exemplares}")
    print(f"📈 Média de exemplares: {media:.2f}")

    mais_antigo = min(
        livros,
        key=lambda x: x["ano"]
    )

    print(
        f"\nLivro mais antigo:"
        f" {mais_antigo['titulo']}"
        f" ({mais_antigo['ano']})"
    )

    print(
        "\n===== POR CATEGORIA ====="
    )

    categorias = {}

    for livro in livros:

        categoria = livro["categoria"]

        categorias[categoria] = (
            categorias.get(categoria, 0)
            + 1
        )

    for categoria, qtd in categorias.items():

        print(
            f"{categoria}: {qtd}"
        )

    print(
        "\n===== TOP 5 ====="
    )

    ranking = sorted(
        livros,
        key=lambda x: x["quantidade"],
        reverse=True
    )

    for livro in ranking[:5]:

        print(
            f"{livro['titulo']} "
            f"- {livro['quantidade']}"
        )

    print(
        "\n===== ORDEM ALFABÉTICA ====="
    )

    ordenados = sorted(
        livros,
        key=lambda x: x["titulo"]
    )

    for livro in ordenados:

        print(
            f"{livro['titulo']} "
            f"- {livro['categoria']}"
        )