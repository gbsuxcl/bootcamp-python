from pathlib import Path
import pandas as pd
import os
import glob

# Uma função de Extract que Lê e Consolida os JSONs
def extrair_e_concatenar(pasta: str) -> pd.DataFrame:
    """
    Extrai e concatena todos os arquivos JSON de uma pasta.

    Args:
        path (str): O caminho para a pasta contendo os arquivos JSON.

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados concatenados.
    """
    arquivos_jsons = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_jsons]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# Uma função  de Transformação
def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# Uma função de Carregamento/Load em CSV ou Parquet
def carregar_dados(df: pd.DataFrame, formato_saida: list):

    for formato in formato_saida: 
        if formato == "csv":
            df.to_csv("dados_vendas_total.csv", sep=";")
        elif formato == "parquet":
            df.to_parquet("dados_vendas_total.parquet")
        else:
            print("Formato inválido")


if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    pasta_arquivo: str = BASE_DIR / 'data'
    data_frame = extrair_e_concatenar(pasta=pasta_arquivo)
    dataframe_calculado = calcular_kpi_total_de_vendas(data_frame)
    tipo_saida: list = ["csv", "parquet"]
    carregar_dados(df=dataframe_calculado, formato_saida=tipo_saida)
