num1=input("Agora me fale o primeiro numero desta operação: ")
num1=int(num1)
num2=input("Agora me fale o segundo numero desta operação: ")
num2=int(num2)
print("Digite 1 para soma!")
print("Digite 2 para subtração!")
print("Digite 3 para multiplicação!")
print("Digite 4 para divisão!")
resposta=input("Me fale que tipo de operação básica voce gostaria de realizar hoje: ")

if resposta == "1": 
 r1 = num1 + num2
 print("A resposta para esta operação é ", r1)
if resposta == "2":
 r2 = num1 - num2
 print("A resposta para esta operação é ", r2)
if resposta == "3":
 r3 = num1 * num2
 print("A resposta para esta operação é ", r3)
if resposta == "4": 
 r4 = num1/num2
 print("A resposta para esta operação é ", r4)
else:
    print("Não foi possivel concluir sua operação!") 