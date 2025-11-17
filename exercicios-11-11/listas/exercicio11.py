vetor1 = []
vetor2 = []
vetor3 = []
vetorFinal = []

for i in range(10):
    n1 = int(input('Insira um valor inteiro para o Vetor 1: '))
    n2 = int(input('Insira um valor inteiro para o Vetor 2: '))
    n3 = int(input('Insira um valor inteiro para o Vetor 3: '))

    vetor1.append(n1)
    vetor2.append(n2)
    vetor3.append(n3)

    vetorFinal.append(n1)
    vetorFinal.append(n2)
    vetorFinal.append(n3)

print(f'\nVetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Vetor 3: {vetor3}')
print(f'Vetor Intercalado: {vetorFinal}')
