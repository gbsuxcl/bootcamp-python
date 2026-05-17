CONSTANTE_BONUS = 1000

# 1. Solicita ao usuário que digite seu nome
nome = input("Digite o seu nome: ")

# 2. Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um numéro de ponto flutuante
salario = float(input("Por favor, informe o seu salário: "))

# 3. Solicite ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Por favor, informe o valor do bônus recebido: "))

# 4. Calcule o valor do bônus final
kpi = CONSTANTE_BONUS + salario * bonus

# 6. Imprime a mensagem personalizada incluindo o nome do usuário, salário e o bônus
print(f"Olá {nome}, o valor do bônus a ser recebido é: {kpi}, Parabéns!")


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
"""
    Riscos:
    - Não existe uma validação de dados inseridos pelo usuário.
    - Não tem uma regra de negócio para saber se o bônus está correto, ou 
    se deveria receber.
    
    Bugs:
    - O cálculo do bônus não está convertendo para porcentagem. O resultado
    está superestimado.
"""
