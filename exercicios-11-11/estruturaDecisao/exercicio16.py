import sys

print(f'--  EQUAÇÃO DE SEGUNDO GRAU   --')
print(f'-- Fórmula: a x2 + bx + c = 0 --')

a = int(input('Insira o valor de A:'))

if a == 0:
    print(f'Não é uma equação de segundo grau!')
    sys.exit()

b = int(input('Insira o valor de B:'))
c = int(input('Insira o valor de C:'))

delta = (b * b) - ((4*a)*c)

if delta < 0:
    print(f'A equação não possui raízes reais!')
    sys.exit()

x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)

print(f'Valor de Δ (delta): {delta}')

if delta == 0:
    print(f'A equação possui apenas uma raiz real: {x1}')
else:
    print(f'A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}')