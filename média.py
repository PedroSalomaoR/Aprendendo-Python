nome=input("Digite o nome do aluno: ")
print("Olá", nome)

nota1=input("Digite a nota do primeiro trimestre: ")
nota1=float(nota1)

nota2=input("Digite a nota do segundo trimestre: ")
nota2=float(nota2)

nota3=input("Digite a nota do terceiro trimestre: ")
nota3=float(nota3)

média=(nota1+nota2+nota3)/3

print(nome, ", a sua média final é de: ", média)