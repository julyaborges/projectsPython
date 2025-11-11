import math

print(f'-- Bem-vindo á Loja de Tintas! --')

metrosQuadrados = float(input('Insira o tamanho da área em metros quadrados:'))

quantidade = math.ceil(metrosQuadrados / 6)

quantLata = math.ceil(quantidade / 18)
precoLata = round(quantLata * 80, 2)

quantGalao = math.ceil(quantidade / 3.6)
precoGalao = round(quantGalao * 25, 2)

quantDois = 0

while(quantDois < )