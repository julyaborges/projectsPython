import math

print(f'-- Bem-vindo á Loja de Tintas! --')

metrosQuadrados = float(input('Insira o tamanho da área em metros quadrados:'))

quantidadeLata = math.ceil((metrosQuadrados / 3) / 18)

precoTotal = round(quantidadeLata * 80, 2)

print(f'Quantidade de Latas: {quantidadeLata} - Preço Total R${precoTotal}')