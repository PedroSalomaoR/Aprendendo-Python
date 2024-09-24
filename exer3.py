print("Você está sendo investigado por um crime!")
print("Vou fazer 5 perguntas básicas, responda apenas com 1 para sim ou 2 para não!")

contadorderespstaspositivas = 0

resposta = input("TELEFONOU PARA A VÍTIMA? (1-sim/2-não): ")
if resposta == "1":
    contadorderespstaspositivas = contadorderespstaspositivas + 1
resposta = input("ESTEVE NO LOCAL DO CRIME? (1-sim/2-não): ")
if resposta == "1":
    contadorderespstaspositivas = contadorderespstaspositivas + 1
resposta = input("MORA PERTO DA VÍTIMA? (1-sim/2-não): ")
if resposta == "1":
    contadorderespstaspositivas = contadorderespstaspositivas + 1
resposta = input("DEVIA PARA A VÍTIMA? (1-sim/2-não): ")
if resposta == "1":
    contadorderespstaspositivas = contadorderespstaspositivas + 1
resposta = input("JÁ TRABALHOU COM A VÍTIMA? (1-sim/2-não): ")
if resposta == "1":
    contadorderespstaspositivas = contadorderespstaspositivas + 1

if contadorderespstaspositivas == 5:
    print("Assassino")
if contadorderespstaspositivas==3 or contadorderespstaspositivas==4:
    print("Cúmplice")   
if contadorderespstaspositivas==2:
    print("Suspeito")
if contadorderespstaspositivas<2:
    print("Inocente")         