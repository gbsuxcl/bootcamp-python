from typing import List
import statistics

#### Exercícios
# 1. Calcular Média de Valores em uma Lista
def calcula_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

# 2. Filtrar Dados Acima de um Limite
def filtrar_dados_acima_do_limite(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

# 3. Contar Valores Únicos em uma Lista
def contador_de_valores_unicos(valores: List[float]) -> int:
    """ Retorna o total de valores únicos em uma lista

        Args:
            valores (List[float]): Lista de valores
        
        Return:
            int: a quantidade de valores únicos da lista
    """
    return len(set(valores))

# 4. Converter Celsius para Fahrenheit em uma Lista
def conversor_celsius_para_fahrenheit(celsius: List[float]) -> List[float]:
    """ Converte graus celsius para fahreheit

        Args:
            celsius List[float]: Temperatura em graus celsius
        
        Return:
            List[float]: Temperatura em fahreheit
    """
    for temperatura in celsius:
        temp_fahrenheit = (temperatura * 9/5) + 32
    return temp_fahrenheit

# 5. Calcular Desvio Padrão de uma Lista
def calcula_desvio_padrao(numero: List[float]) -> List[float]:
    for num in numero:
        desvio_padrao = statistics.stdev(num)
    return desvio_padrao

# 6. Encontrar Valores Ausentes em uma Sequência
def encontra_valores_missing(valores: List[int]) -> List[int]:
    
    # Crie uma sequencia do menor ao maior numero encontrado
    sequencia = set(range(min(valores), max(valores) + 1))

    # Encontrando a diferença
    vlr_vazio = sorted(list(sequencia - set(valores)))

    return vlr_vazio

