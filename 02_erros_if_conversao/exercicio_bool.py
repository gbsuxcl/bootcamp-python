# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expr_and_1 = (
    input("Digite uma expressão booleana (ex: True ou False): ").strip().capitalize()
    == "True"
)
expr_and_2 = (
    input("Digite outra expressão booleana (ex: True ou False): ").strip().capitalize()
    == "True"
)

print(f"O resultado da operação AND é: {expr_and_1 and expr_and_2}")


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expr_or_1 = (
    input("Digite uma expressão booleana (ex: True ou False): ").strip().capitalize()
    == "True"
)
expr_or_2 = (
    input("Digite outra expressão booleana (ex: True ou False): ").strip().capitalize()
    == "True"
)

print(f"O resultado da operação OR é: {expr_or_1 or expr_or_2}")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expr_not = (
    input("Digite uma expressão booleana (ex: True ou False): ").strip().capitalize()
    == "True"
)

print(f"O resultado da operação NOT é: {not expr_not}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num_iguais_1 = int(input("Digite um número inteiro (ex: 5; 6; 10): "))
num_iguais_2 = int(input("Digite outro número inteiro (ex: 5; 6; 10): "))

print(f"Os números são iguais? {num_iguais_1 == num_iguais_2}")


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num_diff_1 = int(input("Digite um número inteiro (ex: 5; 6; 10): "))
num_diff_2 = int(input("Digite outro número inteiro (ex: 5; 6; 10): "))

print(f"Os números são diferentes? {num_diff_1 != num_diff_2}")
