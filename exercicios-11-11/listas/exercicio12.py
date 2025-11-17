idades = []
alturas = []
alturaSoma = 0

for i in range (30):
    print(f'Bem-vinda Pessoa {i+1}! Insira seus dados: ')
    idade = int(input(f'Insira a sua idade: '))
    idades.append(idade)
    altura = float(input(f'Insira a sua altura: '))
    alturas.append(altura)
    alturaSoma += altura

alturaMedia = alturaSoma / 30

alturasInferiores = 0

for i in range (30):
    if idades[i] > 13 and alturas[i] < alturaMedia:
        alturasInferiores += 1

print(f'Total de alunos maiores de 13 anos com altura abaixo da média: {alturasInferiores}')