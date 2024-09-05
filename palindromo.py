palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas (caso a palavra tenha letras maiúsculas)
palavra = palavra.replace(" ", "").lower()

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")