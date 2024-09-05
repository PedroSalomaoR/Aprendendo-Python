print("Vamos somar todos os numeros de 1 a 100 que sejam impares")

somaimpares=0

for i in range(1, 101):
    if i % 2 != 0:
         somaimpares+=i
        
        
print("A soma de todos os numeros impares é ",somaimpares)