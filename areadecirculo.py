raio=float(input("Fale qual a medida do raio do circulo que iremos te devolver a area: "))
resposta=input("Com o valor de pi? (Sim ou Não)")

if resposta == "Sim" or "sim":
    a=(raio**2) *3.141516
    print("A Area do circulo é de ", a)
else:
    pi="r"
    a=(raio**2)
    print("A area do circulo é de", a, pi)