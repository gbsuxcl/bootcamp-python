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
num1 = float(input("Informe um número: "))
operador = input("Informe o operador (+, -, /...): ")
num2 = float(input("Informe outro número: "))

if operador == "+":
    print(f"Resultado: {num1 + num2}")
elif operador == "-":
    print(f"Resultado: {num1 - num2}")
elif operador == "*":
    print(f"Resultado: {num1 * num2}")
elif operador == "/":
    print(f"Resultado: {num1 / num2}")
elif operador == "**":
    print(f"Resultado: {num1 ** num2}")
elif operador == "%":
    print(f"Resultado: {num1 % num2}")
elif operador == "//":
    print(f"Resultado: {num1 // num2}")
else:
    print("Operador inválido")


# 24: Classificador de Números
try:
    num = float(input("Digite um número: "))

    if num > 0:
        print("Número positivo")
    elif num < 0:
        print("Número negativo")
    else:
        print("Número igual a zero")

except ValueError as e:
    print("Por favor, insira apenas números")
    print(f"Erro: {e}")


# 25: Conversão de Tipo com Validação
ent_lista = input("Digite uma lista de números separados por vírgula: ")
nm_str = ent_lista.split(",")
nm_int = []

try:
    for num in nm_str:
        nm_int.append(int(num.strip()))
    print("Lista de inteiros", nm_int)
except ValueError:
    print("Erro: vefirique se todos os elementos são números inteiros e válidos")
