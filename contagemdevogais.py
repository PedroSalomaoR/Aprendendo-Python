texto=str(input("Digite um texto e vamos contar quantas vogais tem nele: "))

vogais="aeiouAEIOU"
contador=0

for chr in texto:
    if chr in vogais:
        contador=contador+1
       
    
print("O texto possui ",contador, "Vogais!")