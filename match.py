x = int(input("Digite um numero de 1 a 5: "))

match x:
    case 1:
        print("Voce escolheu o numero 1")
    case 2:
        print("Voce escolheu o numero 2")
    case 3:
        print("Voce escolheu o numero 3")
    case 4:
        print("Voce escolheu o numero 4")
    case 5:
        print("Voce escolheu o numero 5")
    case _ :
        print("Voce não escolheu nenhuma opção correta!")                