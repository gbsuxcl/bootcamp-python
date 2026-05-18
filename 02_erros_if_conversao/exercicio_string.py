# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
letra = input("Digite uma letra:")

print(f"A letra em maiúsculo é: {letra.upper()}")


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite o seu nome completo: ")

print(f"O seu nome em maiúsculo é: {nome_completo.upper()}")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Escreva uma frase: ")

print(f"Sua frase sem espaços é: {frase.strip()}")


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Informe uma data (ex: dd/mm/aaaa): ")

print(f"A data separada é: {data.split('/')}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
palavra_1 = input("Digite uma palavra: ")
palavra_2 = input("Digite outra palavra: ")

print(f"As palavras juntas: {palavra_1 + palavra_2}")
