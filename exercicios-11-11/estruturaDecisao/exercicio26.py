print(f'--   POSTO DE COMBUSTÍVEL    --')
print(f'-- A - Álcool | G - Gasolina --')

tipoCombustivel = input('Tipo de combustível? A/G: ')
litros = int(input('Quantidade de litros: '))

valor = 0

if tipoCombustivel == 'A' or tipoCombustivel == 'a':
    if litros <= 20:
        valor = round((litros * 1.90) -  ((litros * 1.90) * (1.90 * 0.03)), 2)
    else:
        valor = round((litros * 1.90) -  ((litros * 1.90) * (1.90 * 0.05)), 2)
elif tipoCombustivel == 'G' or tipoCombustivel == 'g':
    if litros <= 20:
        valor = round((litros * 2.50) -  ((litros * 2.50) * (2.50 * 0.04)), 2)
    else:
        valor = round((litros * 2.50) -  ((litros * 2.50) * (2.50 * 0.06)), 2)
else:
    print(f'Tipo de combustível inválido.')
    exit()

print(f'Total a ser pago: R${valor}')