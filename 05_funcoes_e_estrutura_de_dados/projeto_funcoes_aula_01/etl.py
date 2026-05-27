import csv

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma 
    lista de dicionários
    """
    lista = []

    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=",")
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valores_dos_produtos(filtrar_produtos_entregues: list[dict]) -> int:
    """
    Função que lê os produtos entregues 
    e soma os valores dos produtos
    """
    valor_total = 0
    for produto in filtrar_produtos_entregues:
        valor_total += int(produto.get("price"))
    return valor_total