numeros = []
pares = []
impares = []

for i in range (20):
    num = int(input(f'Insira um número inteiro: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Vetor de inteiros: {numeros}')
print(f'Vetor de pares: {pares}')
print(f'Vetor de ímpares: {impares}')