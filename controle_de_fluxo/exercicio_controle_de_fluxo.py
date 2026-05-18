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


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {
    "timestamp": "2021-06-23 10:00:00",
    "level": "ERROR",
    "message": "Falha na conexão",
}

if log["level"] == "ERROR":
    print(log["message"])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
idade = 20
email = "user@example.com"

while idade != True or email != True:
    try:

        if not 18 <= idade <= 65:
            idade == False
            print("Idade invalida. Insira a idade novamente")
        elif "@" not in email or "." not in email:
            email == False
            print("Email invalido. Insira o email novamente")
        else:
            idade == True and email == True
            print("Dados de usuario validos")
    except TypeError as e:
        print(f"{e}")
