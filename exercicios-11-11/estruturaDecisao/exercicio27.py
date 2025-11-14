import sys

print('------  SUPERMERCADO TABAJARA  ------')
print('- Tipo Carne - Até 5kg - Acima de 5kg -')
print('F - Filé Duplo - R$4,90 kg - R$5,80 kg')
print('A - Alcatra    - R$5,90 kg - R$6,80 kg')
print('P - Picanha    - R$6,90 kg - R$7,80 kg')

tipoCarne = input('Selecione um tipo de carne F/A/P: ')
kgCarne = float(input('Quantidade em kg: '))
totalValor = 0

if tipoCarne == 'F' or tipoCarne == 'f':
    tipoCarne = 'F - Filé Duplo'
    if kgCarne <= 5:
        totalValor = kgCarne * 4.90
    else:
        totalValor = kgCarne * 5.80
elif tipoCarne == 'A' or tipoCarne == 'a':
    tipoCarne = 'A - Alcatra'
    if kgCarne <= 5:
        totalValor = kgCarne * 5.90
    else:
        totalValor = kgCarne * 6.80
elif tipoCarne == 'P' or tipoCarne == 'p':
    tipoCarne = 'P - Picanha'
    if kgCarne <= 5:
        totalValor = kgCarne * 6.90
    else:
        totalValor = kgCarne * 7.80
else: 
    print(f'Tipo de carne inválido.')
    sys.exit()

print(f'Total: R${totalValor}')

cartaoTabajara = input('Forma de pagamento seria no Cartão Tabajara? (s/n)')
valorDesconto = 0

if cartaoTabajara == 's' or cartaoTabajara == 'S':
    valorDesconto = totalValor * 0.05
    totalValor = totalValor - valorDesconto
    tipoPagamento = 'Cartão Tabajara'
else:
    tipoPagamento = 'Cartão Débito'

print('-- CUPOM FISCAL --')
print(f'Tipo de carne: {tipoCarne}')
print(f'Quantidade: {kgCarne}kg')
print(f'Preço total: R${round(totalValor, 2)}')
print(f'Tipo pagamento: {tipoPagamento}')
print(f'Valor do desconto: R${round(valorDesconto, 2)}')
print(f'Valor a pagar: R${round(totalValor, 2)}')
