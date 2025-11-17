print(f'-- Caixa Eletrônico --')

valor = int(input('Insira o valor para saque (mínimo R$10 e máximo R$600): '))

if valor < 10 or valor > 600:
    print('Valor inválido! O saque deve ser entre R$10 e R$600.')
else:
    print(f'Valor solicitado: R${valor}')

    notas100 = valor // 100
    valor = valor - (notas100 * 100)

    notas50 = valor // 50
    valor = valor - (notas50 * 50)

    notas10 = valor // 10
    valor = valor - (notas10 * 10)

    notas5 = valor // 5
    valor = valor - (notas5 * 5)

    notas1 = valor 

    print('\n-- Quantidade de notas fornecidas --')
    print(f'Notas de 100: {notas100}')
    print(f'Notas de 50: {notas50}')
    print(f'Notas de 10: {notas10}')
    print(f'Notas de 5: {notas5}')
    print(f'Notas de 1: {notas1}')
