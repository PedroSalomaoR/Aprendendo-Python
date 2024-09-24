print("Código             Produto             Preço Unitário(R$)")
print("100             Cachorro quente             R$1,70")
print("101              Bauru Simples              R$2,30")
print("102              Bauru com ovo              R$2,60")
print("103               Hamburguer                R$2,40")
print("104              Cheeseburguer              R$2,50")
print("105              Refrigerante               R$1,00")

codigo=int(input("Digite o código do produto que você desejar: "))

match codigo:
    case 100:
        print("Você escolheu o Cachorro quente!")
        unidades=int(input("Quantas unidades você gostaria? "))
        cachorroquente=1.70
        vlrconta=unidades*cachorroquente
        print(f"Cachorro quente --- R${cachorroquente} X {unidades} unidade(s)= R${vlrconta}")
    case 101:
        print("Você escolheu o Bauru simples!")
        unidades=int(input("Quantas unidades você gostaria? "))
        bauru=2.3
        vlrconta=unidades*bauru
        print(f"Bauru Simples --- R${bauru} X {unidades} unidade(s)= R${vlrconta}")
    case 102:
        print("Você escolheu o Bauru com ovo!")
        unidades=int(input("Quantas unidades você gostaria? "))
        baurucovo=2.60
        vlrconta=unidades*baurucovo
        print(f"Bauru com ovo --- R${baurucovo} X {unidades} unidade(s)= R${vlrconta}")
    case 103:
        print("Você escolheu o Hamburguer!")
        unidades=int(input("Quantas unidades você gostaria? "))
        hamburguer=2.40
        vlrconta=unidades*hamburguer
        print(f"Hamburguer --- R${hamburguer} X {unidades} unidade(s)= R${vlrconta}")
    case 104:
        print("Você escolheu o Cheeseburguer!")
        unidades=int(input("Quantas unidades você gostaria? "))
        cheeseburguer=2.50
        vlrconta=unidades*cheeseburguer
        print(f"Cheeseburguer --- R${cheeseburguer} X {unidades} unidade(s)= R${vlrconta}")
    case 105:
        print("Você escolheu o Refrigerante!")
        unidades=int(input("Quantas unidades você gostaria? "))
        refri=1
        vlrconta=unidades*refri
        print(f"Refrigerante --- R${refri} X {unidades} unidade(s)= R${vlrconta}")
    case _:
        print("ERRO NA OPERAÇÃO!")    
              
if (codigo > 99) and (codigo < 106):
    print("===================================================")
    print("            OPÇÕES DE PAGAMENTO")              
    print("===================================================")      
    print("1-Pagamento á vista(Débito/Dinheiro)-Desconto de 5%")        
    print("2-Pagamento á vista via Pix-Desconto de 8%")        
    print("3-Pagamento em 3x- Sem juros")        
    print("4-Pagamentos com 4 ou mais parcelas (máximo 10x) Juros por mes de 2%")
    
    opcaodepag=int(input("Como você gostaria de fazer o pagamento? "))
    
    match opcaodepag:
        case 1:
            vlrpagamento=vlrconta-vlrconta*0.05
            print("Com o pagamento á vista(Débito/Dinheiro), você ganha desconto de 5%")
            print(f"Você ira pagar R${vlrpagamento}")
        case 2:
            vlrpagamento=vlrconta-vlrconta*0.08
            print("Com o pagamento á vista via Pix, você ganha desconto de 8%")
            print(f"Você ira pagar R${vlrpagamento}") 
        case 3:
            parcelas=3
            vlrpagamento=vlrconta/parcelas
            print(f"Você decidiu parcelar em {parcelas} vezes- Sem juros")
            print(f"Você ira pagar {parcelas} parcelas de R${vlrpagamento}")     
        case 4:
            numeroparcelas=int(input("Em quantas parcelas você gostaria de realizar a compra? "))
            if numeroparcelas>3 and numeroparcelas<=10:
                juros=0.02
                pbruto=vlrconta/numeroparcelas
                valorcomjuros=pbruto*((1+juros)**numeroparcelas-1)/0.02
                vlrdeparcelascjuros=valorcomjuros/numeroparcelas
                print(f"Você ira pagar {numeroparcelas} parcelas de R${vlrdeparcelascjuros}")
            else:
                print("Não foi possivel concluir sua compra")    