print(f'-- FOLHA DE PAGAMENTO --')

horas = int(input('Horas trabalhadas:'))
valorHora = float(input('Valor da hora:'))

salarioBruto = horas * valorHora

descontoIr = 0

porcentagem = ''

if salarioBruto <= 900.00:
    descontoIr = 0
    porcentagem = '0%'
elif salarioBruto <= 1500.00:
    descontoIr = 0.05
    porcentagem = '5%'
elif salarioBruto <= 2500.00:
    descontoIr = 0.10
    porcentagem = '10%'
else:
    descontoIr = 0.20
    porcentagem = '20%'

valorIr = round(salarioBruto * descontoIr, 2)

descontoInss = round(salarioBruto * 0.10, 2)

fgts = round(salarioBruto * 0.11, 2)

salarioLiquido = salarioBruto - descontoInss - valorIr

print('-- FOLHA - NOVEMBRO/2025 --')

print(f'Salário Bruto (R${valorHora} * {horas}): R${salarioBruto}')
print(f'(-) IR ({porcentagem}): R${valorIr}')
print(f'(-) INSS (10%): R${descontoInss}')
print(f'FGTS (11%): R${fgts}')
print(f'Total de descontos: R${valorIr + descontoInss}')
print(f'Salário Líquido: R${salarioLiquido}')
