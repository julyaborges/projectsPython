import sys

print(f'-- FORME UM TRIÂNGULO ;) --')

lado1 = float(input('Insira o 1° lado:'))
lado2 = float(input('Insira o 2° lado:'))
lado3 = float(input('Insira o 3° lado:'))

if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado3 + lado2 > lado1:
    print(f'É um triângulo!')
else:
    print(f'Não é um triângulo!')
    sys.exit()

if lado1 == lado2 and lado2 == lado3:
    print(f'Tipo: Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print(f'Tipo: Isóceles')
else:
    print(f'Tipo: Escaleno')

     