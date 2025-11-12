print(f'-- Cálculo Salarial --')

valorHora = float(input('Quanto você ganha por hora?'))
horasTrabalhadas = int(input('Quantas horas você trabalhou nesse mês?'))

salarioBruto = valorHora * horasTrabalhadas
salarioLiquido = salarioBruto - (salarioBruto * 0.11) - (salarioBruto * 0.08) - (salarioBruto * 0.05)

print(f'Salário bruto: R${salarioBruto}')
print(f'INSS: R${salarioBruto * 0.08}')
print(f'Sindicato: R${salarioBruto * 0.05}')
print(f'Salário Líquido: R${salarioLiquido}')
