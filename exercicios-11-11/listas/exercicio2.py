vetor = []

for i in range (10):
    inteiro = int(input(f'Insira o {i+1} número do vetor: '))
    vetor.append(inteiro)

for i in range(9, -1, -1):
    print(f'Vetor invertido: {vetor[i]}')