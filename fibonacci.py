print("Vamos mostrar para voce os 10 primeiros numeros da sequencia de fibonacci! ")

a, b = 0, 1

# Loop para gerar e imprimir os termos da sequência
for _ in range(10):
    # Imprime o termo atual
    print(a, end=' ')
    
    # Atualiza os termos para o próximo par de números
    a, b = b, a + b

    
  