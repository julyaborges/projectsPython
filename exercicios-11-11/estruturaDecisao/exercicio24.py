import sys
import math

print(f'-- CALCULE --')

num1 = int(input('Insira o 1° número: '))
operador = input('Qual operação você deseja realizar: (+, -, / ou *)')
num2 = int(input('Insira o 2° número: '))

resultado = 0

if operador == '+':
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')
elif operador == '-':
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')
elif operador == '/':
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}')
elif operador == '*':
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado}')
else:
    print(f'Operador inválido')
    sys.exit()

if resultado % 2 == 0:
    print(f'O resultado é par')
else:
    print(f'O resultado é ímpar')

if resultado < 0:
    print(f'O resultado é negativo')
else:
    print(f'O resultado é positivo')

if resultado == math.floor(resultado):
    print(f'O resultado é inteiro')
else:
    print(f'O resultado é decimal')