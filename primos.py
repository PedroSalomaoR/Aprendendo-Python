num=int(input("Digite um numero e vamos falar se ele é primo ou não: "))

if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
    print("Não é primo")
else: 
    print(num ,"É primo")    