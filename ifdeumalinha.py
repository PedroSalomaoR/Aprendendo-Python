x = int(input("Dependendo do valor da sua compra vc ganhara desconto, fale o valor da compra: "))

desconto= 0.20 if x >= 1500 else 0

x=x+x*(-1*desconto)
print(f"O valor da compra ficou em {x}")