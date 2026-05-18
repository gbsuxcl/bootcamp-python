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
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
