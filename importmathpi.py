from math import pi

raio=float(input("Fale qual a medida do raio do circulo que iremos te devolver a area: "))

a=(raio**2)*pi
cac=2*pi*raio

print(f"A area do circulo de {raio} é de ",a, f", e o seu arco é de {cac}")
#com o f(precisa ser minusculo) voce pode colocar o valor só com as chaves antes do texto
