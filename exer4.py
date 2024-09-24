print("Este programa é responsavel pelo calculo do IRPF do Senhor(a)!")
salariobruto=float(input("Me fale o seu salário Bruto: "))


if salariobruto<2259.20:
    print("Você não precisa pagar IRPF")
    
if salariobruto>=2259.21 and salariobruto<= 2826.65:
    aliquota=0.075
    parceadedu=169.44
    salariopdesc=salariobruto*aliquota
    paradeirpf=salariopdesc-parceadedu
    print(f"Você deve pagar de IRPF {paradeirpf}")    
    
if salariobruto>=2826.66 and salariobruto<= 3751.05:
    aliquota=0.15
    parceadedu=381.44
    salariopdesc=salariobruto*aliquota
    paradeirpf=salariopdesc-parceadedu
    print(f"Você deve pagar de IRPF {paradeirpf}")
    
if salariobruto>=3751.06 and salariobruto<= 4664.68:
    aliquota=0.2250
    parceadedu=662.77
    salariopdesc=salariobruto*aliquota
    paradeirpf=salariopdesc-parceadedu
    print(f"Você deve pagar de IRPF {paradeirpf}")
    
if salariobruto>4664.68:
    aliquota=0.2750
    parceadedu=896
    salariopdesc=salariobruto*aliquota
    paradeirpf=salariopdesc-parceadedu
    print(f"Você deve pagar de IRPF {paradeirpf}")