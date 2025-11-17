def valor_pagamento(valorPrestacao, numDias):
    valor = valorPrestacao + (valorPrestacao * 0.03) + (0.001 * numDias)
    return valor

continuar = 's'
quantPrestacao = 0
somaPrestacoes = 0

while continuar == 's':

    valorPrestacao = float(input('Insira o valor da prestação:'))

    if valorPrestacao == 0:
        print(F'Programa encerrado!')
        continuar = 'n'
    else:
        numDias = int(input('Insira o número de dias em atraso:'))
        valorPago = valor_pagamento(valorPrestacao, numDias)
        print(f'Valor a ser pago: R${valorPago}')
        quantPrestacao += 1
        somaPrestacoes += valorPago

print(f'Relatório do dia:')
print(f'Quantidade de prestações pagas: {quantPrestacao}')
print(f'Valor total de prestações pagas: {round(valorPago, 2)}')