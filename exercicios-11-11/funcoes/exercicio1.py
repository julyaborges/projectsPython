def imprimir(n):
    # imprime cada linha
    for i in range(1, n + 1):
        # imprime o número x vezes
        for x in range(i):
            print(i, end=" ")
        
        # pula para a próxima linha
        print()

num = int(input('Digite um número inteiro:'))

imprimir(num)