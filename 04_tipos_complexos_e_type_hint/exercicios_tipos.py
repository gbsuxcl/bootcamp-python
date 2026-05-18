# ### Exercícios de Listas e Dicionários resolvidos
# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
import enum

emails: list[str] = [
    "user@example.com",
    "admin@example.com",
    "user@example.com",
    "manager@example.com",
]
emails_unique: list[str] = list(set(emails))
print(emails_unique)


# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades: list[int] = [22, 15, 30, 17, 18]

idades_maiores_18: list[int] = [idade for idade in idades if idade >= 18]
print(idades_maiores_18)


# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas: list[dict[str, int | str]] = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20},
]

pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)


# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
numeros: list[int] = [10, 20, 30, 40, 50]

media = sum(numeros) / len(numeros)
print(media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valores_pares: list[int] = [x for x in valores if x % 2 == 0]
valores_impares: list[int] = [x for x in valores if x % 2 != 0]

print(f"Pares: {valores_pares}")
print(f"Ímpares: {valores_impares}")


# ### Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
