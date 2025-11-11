import sys

print(f'-- Calcule o excesso da pesca --')

peso = float(input('Qual foi o peso da pesca?'))

if peso > 50:
    excesso = peso - 50
else:
    print(f'O peso da pesca está dentro do limite')
    sys.exit()

multa = excesso * 4.0

print(f'{excesso} kgs acima do limite - Valor da multa: R$ {multa} ')