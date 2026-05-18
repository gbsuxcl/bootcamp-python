# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    temp_fahrenheit = (celsius * 9 / 5) + 32
    print(f"A temperatura em Fahrenheit é: {temp_fahrenheit}")

except ValueError as e:
    print("\nPor favor, insira apenas números")
    print(f"Erro: {e}")


# 22: Verificador de Palíndromo
import re

frase = input("Digite uma frase: ")

# 01. Limpeza
limpeza = re.sub(r"[^A-Za-z0-9]", "", frase)

# 02. Remove espaços
remove_espacos = limpeza.replace(" ", "")

# 03. Inverte a string
inversao = remove_espacos[::-1]

# 04. Compara as frases
if frase == frase[::-1]:
    print("A frase é um políndromo")
else:
    print("A frase não é um políndromo")


# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
