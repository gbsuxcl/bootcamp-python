### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.
preco = 20000
quantidade = 10

if preco > 0 and quantidade > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# 18°C <= Temperatura <= 25°C é 'Normal'
# Temperatura > 25°C é 'Alta'

temperatura = 30

if temperatura < 18:
    print("Temperatura Baixa")
elif temperatura >= 18 and temperatura <= 25:
    print("Temperatura Normal")
elif temperatura > 25:
    print("Temperatura Alta")
else:
    print("Temperatura não identificada")
