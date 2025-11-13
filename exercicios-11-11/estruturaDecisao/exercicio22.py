import math

num = float(input('Insira um número inteiro ou decimal: '))

if num == math.floor(num):
    print(f'Número inteiro')
else:
    print(f'Número decimal')