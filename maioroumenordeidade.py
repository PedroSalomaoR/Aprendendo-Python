nome=(input("Qual o seu nome? "))

resposta=(input("Quantos anos voce tem? "))
resposta=int(resposta)

if resposta >= 18:
    print( nome, ", Voce é maior de idade, porque tem ",resposta, " anos! ")
else:
    print( nome, ", Voce não é maior de idade!")  