vetorInt = []
soma = 0

for i in range (5):
    num = int(input(f'Insira um número inteiro: '))
    vetorInt.append(num)
    soma += num
    
multi = vetorInt[0] * vetorInt[1] * vetorInt[2] * vetorInt[3] * vetorInt[4]

print(f'Vetor: {vetorInt}')
print(f'Soma: {soma}')
print(f'Multiplicação: {multi}')