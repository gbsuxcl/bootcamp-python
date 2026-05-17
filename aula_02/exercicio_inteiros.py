# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_soma_1 = int(input("Digite um número inteiro (ex: 5; 6; 10): "))
num_soma_2 = int(input("Digite outro número inteiro (ex: 5; 6; 10): "))
soma = num_soma_1 + num_soma_2

print(f"A soma dos dois números é: {soma}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num_resto_divisao = int(input("Digite um número inteiro (ex: 5; 6; 10): "))
resto_divisao = num_resto_divisao % 5

print(f"O resto da divisão é: {resto_divisao}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num_mult_1 = int(input("Digite um número inteiro (ex: 5; 6; 10): "))
num_mult_2 = int(input("Digite outro número inteiro (ex: 5; 6; 10): "))
mult = num_mult_1 * num_mult_2

print(f"O resultado da multiplicação é:{mult}")


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
div_num_1 = int(input("Digite um número inteiro (ex: 5; 6; 10): "))
div_num_2 = int(input("Digite outro número inteiro (ex: 5; 6; 10): "))
div_inteira = div_num_1 // div_num_2

print(f"O resultado da divisão inteira é: {div_inteira}")


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num_usuario = int(input("Digite um número: "))
quadrado = num_usuario**2

print(f"O quadrado do número {num_usuario} é: {quadrado}")
