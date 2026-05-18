# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_soma_float_1 = float(input("Digite um número flutuante (ex: 2.3; 4.1): "))
num_soma_float_2 = float(input("Digite outro número flutuante (ex: 2.3; 4.1): "))
soma_float = num_soma_float_1 + num_soma_float_2

print(f"A soma dos dois números é: {soma_float}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_media_float_1 = float(input("Digite um número flutuante (ex: 2.3; 4.1): "))
num_media_float_2 = float(input("Digite outro número flutuante (ex: 2.3; 4.1): "))
media_float = (num_media_float_1 + num_media_float_2) / 2

print(f"A média dos dois números é: {media_float}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
num_base_float = float(input("Digite um número flutuante (ex: 2.3; 4.1): "))
num_expo_float = float(input("Digite um número flutuante (ex: 2.3; 4.1): "))
pot_float = num_base_float**num_expo_float

print(f"A potência de{num_base_float} elevado a {num_expo_float} é: {pot_float}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
graus_celsius = float(input("Digite a temperatura em graus Celsius (ex: 32.4): "))
conversor_celsius_fahrentheit = (graus_celsius * 9 / 5) + 32

print(f"A temperatura em Fahrenheit é: {conversor_celsius_fahrentheit}")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
PI = 3.14
num_raio = float(input("Digite um número do raio do círculo: "))
area = PI * (num_raio**2)

print(f"A área do círculo é: {area}")
