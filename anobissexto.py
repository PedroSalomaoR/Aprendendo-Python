ano=int(input("Fale um ano e diremos se ele é bissexto ou não: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 ==0 ):
    print("É bissexto")
else:
    print("Não é bissexto")    