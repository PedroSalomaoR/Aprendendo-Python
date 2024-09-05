# Solicita ao usuário uma lista de números separados por espaço
entrada = input("Digite uma lista de números separados por espaço: ")

# Converte a entrada em uma lista de números (inteiros)
numeros = list(map(int, entrada.split()))

# Ordena a lista em ordem crescente
ordem_crescente = sorted(numeros)

# Ordena a lista em ordem decrescente
ordem_decrescente = sorted(numeros, reverse=True)

# Exibe a lista em ordem crescente
print("Lista em ordem crescente:", ordem_crescente)

# Exibe a lista em ordem decrescente
print("Lista em ordem decrescente:", ordem_decrescente)
