import sys
import math

num = int(input('Insira um número menor que 1000:'))

if num >= 1000:
    print(f'Número inválido!')
    sys.exit()

centenas = math.floor(num/100)

if centenas == 1:
    centenaStr = 'centena'
else:
    centenaStr = 'centenas'

dezenas = math.floor((num - (centenas * 100)) / 10)
dezenaStr = ''

if dezenas == 1:
    dezenaStr = 'dezena'
else:
   dezenaStr = 'dezenas'

unidades = (num - (centenas * 100 )) - (dezenas * 10)
unidadeStr = ''

if unidades == 1:
    unidadeStr = 'unidade'
else:
   unidadeStr = 'unidades'

if dezenas == 0 and centenas == 0:
    print(f'{num}: {unidades} {unidadeStr}')
elif unidades == 0 and centenas == 0:
    print(f'{num}: {dezenas} {dezenaStr}')
elif dezenas == 0 and unidades == 0:
    print(f'{num}: {centenas} {centenaStr}')
elif unidades == 0 and dezenas >= 1 and centenas >= 1:
    print(f'{num}: {centenas} {centenaStr} e {dezenas} {dezenaStr}')
elif unidades >=1 and dezenas == 0 and centenas >= 1:
    print(f'{num}: {centenas} {centenaStr} e {unidades} {unidadeStr}')
elif dezenas >= 1 and centenas == 0:
    print(f'{num}: {dezenas} {dezenaStr} e {unidades} {unidadeStr}')
else:
    print(f'{num}: {centenas} {centenaStr}, {dezenas} {dezenaStr} e {unidades} {unidadeStr}')