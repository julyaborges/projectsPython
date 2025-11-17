notas = []
continuar = 's'
somaValores = 0
somaTotal = 0
totalAcimaMedia = 0
abaixoSete = 0

while continuar == 's':
    nota = float(input('Insira uma nota de 1 a 10:'))

    if nota < 0:
        continuar = 'n'
    else:
        notas.append(nota)
        somaValores += 1
        somaTotal += nota

print(f'Quantidade de valores lidos: {somaValores}')
print(f'Notas informadas: {notas}')

print(f'Notas informadas ao contrário:')
for i in notas[::-1]:
    print(i)

print(f'Soma das notas: {somaTotal}')

media = somaTotal / len(notas)
print(f'Média dos valores: {media}')

for i in range(len(notas)):
    if notas[i] > media:
        totalAcimaMedia += 1
    
    if notas[i] < 7:
        abaixoSete += 1

print(f'Quantidade de notas acima da média: {totalAcimaMedia}')

print(f'Quantidade de notas abaixo de sete: {abaixoSete}')

print(f'Uma mensagem!')