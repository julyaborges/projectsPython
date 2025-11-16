import sys

print(f'-- FRUTEIRA --')

morango = float(input('Morango Kg: '))
precoMorango = 0

maca = float(input('Maçã Kg: ')) 
precoMaca = 0

if morango <= 5:
    precoMorango = morango * 2.50
else:
    precoMorango = morango * 2.20    

if maca <= 5:
    precoMaca = maca * 1.80
else:
    precoMaca = maca * 1.50  

totalPreco = precoMaca + precoMorango

if morango + maca > 8 or totalPreco > 25.0:
    totalPreco = totalPreco - (totalPreco * 0.10)
    print(f'Você recebeu 10% de desconto - Total: R${totalPreco}')
else:
    print(f'Total: R${totalPreco}')