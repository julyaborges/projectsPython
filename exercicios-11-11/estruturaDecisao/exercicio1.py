num1 = int(input('Insira um número:'))
num2 = int(input('Insira outro número:'))

if num1 > num2:
    print(f'{num1} é maior')
elif num1 == num2:
    print(f'Os números são iguais')
else:
    print(f'{num2} é maior')