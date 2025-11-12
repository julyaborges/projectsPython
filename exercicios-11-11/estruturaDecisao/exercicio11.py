print('-- Organizações Tabajara --')
print('-- Descubra seu aumento! --')

salarioAtual = float(input('Insira o valor do seu salário atual:'))

porcentagem = ''
valorAumento = 0

if salarioAtual <= 280.00:
    valorAumento = salarioAtual * 0.20
    salarioAjuste = salarioAtual + valorAumento
    porcentagem = '20%'
elif salarioAtual > 280.00 and salarioAtual <= 700.00:
    valorAumento = salarioAtual * 0.15
    salarioAjuste = salarioAtual + valorAumento
    porcentagem = '15%'
elif salarioAtual > 700.00 and salarioAtual <= 1500.00:
    valorAumento = salarioAtual * 0.10
    salarioAjuste = salarioAtual + valorAumento
    porcentagem = '10%'
else:
    valorAumento = salarioAtual * 0.05
    salarioAjuste = salarioAtual + valorAumento
    porcentagem = '5%'
    
print(f'Salário atual: R${round(salarioAtual, 2)}')
print(f'Percentual de aumento: {porcentagem}')
print(f'Valor do aumento: R${round(valorAumento, 2)}')
print(F'Salário após aumento: {round(salarioAjuste, 2)}')