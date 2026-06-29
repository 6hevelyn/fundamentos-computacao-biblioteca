import csv
import os

ARQUIVO = "livros.csv"


def carregar_dados():
    """
    Carrega os livros do arquivo CSV.
    """

    livros = []

    try:
        if os.path.exists(ARQUIVO):

            with open(
                ARQUIVO,
                "r",
                newline="",
                encoding="utf-8"
            ) as arquivo:

                leitor = csv.DictReader(arquivo)

                for linha in leitor:

                    livros.append({
                        "id": int(linha["id"]),
                        "titulo": linha["titulo"],
                        "autor": linha["autor"],
                        "categoria": linha["categoria"],
                        "ano": int(linha["ano"]),
                        "quantidade": int(linha["quantidade"])
                    })

    except Exception as erro:
        print(f"Erro ao carregar dados: {erro}")

    return livros


def salvar_dados(livros):
    """
    Salva os livros no arquivo CSV.
    """

    try:

        with open(
            ARQUIVO,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            campos = [
                "id",
                "titulo",
                "autor",
                "categoria",
                "ano",
                "quantidade"
            ]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()

            for livro in livros:
                escritor.writerow(livro)

    except Exception as erro:
        print(f"Erro ao salvar dados: {erro}")