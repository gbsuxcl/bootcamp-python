from etl import ler_csv, filtrar_produtos_entregues, somar_valores_dos_produtos
from pathlib import Path

BASE_DIR = Path(__file__).parent
path_arquivo = BASE_DIR / "venda.csv"


csv_lido = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(csv_lido)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)