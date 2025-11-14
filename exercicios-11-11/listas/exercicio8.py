idades = []
alturas = []

for i in range (5):
    print(f'Bem-vinda Pessoa {i+1}! Insira seus dados: ')
    idade = int(input(f'Insira a sua idade: '))
    idades.append(idade)
    altura = float(input(f'Insira a sua altura: '))
    alturas.append(altura)

for i in range(4, -1, -1):
    print(f'Pessoa {i+1}: idade: {idades[i-1]} altura: {alturas[i-1]} ')