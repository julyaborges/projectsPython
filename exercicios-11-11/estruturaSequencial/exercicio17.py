import math

print(f'-- Bem-vindo á Loja de Tintas! --')

metrosQuadrados = float(input('Insira o tamanho da área em metros quadrados:'))
litros = metrosQuadrados / 6
print(f'Quantidade de litros necessários: {round(litros, 2)}L')

quantidadeLata = math.ceil(litros / 18)
precoTotalLata = round(quantidadeLata * 80, 2)
print(f'Preço total (apenas latas): R${precoTotalLata}')

quantidadeGalao = math.ceil(litros / 3.6)
precoTotalGalao = round(quantidadeGalao * 25, 2)
print(f'Preço total (apenas galões): R${precoTotalGalao}')

# Opção 3 - Misturar latas e galões

# Deixa 10% de folga 
litrosTotais = litros * 1.10

# Máximo de latas, só a parte inteira
latas = litrosTotais // 18   

# Calcula o restante
litrosRestantes =  litrosTotais - (latas * 18)

# Quantidade de galões necessários
galoes = math.ceil(litrosRestantes / 3.6)

# Preço total
precoTotal = round((latas * 80) + (galoes * 25), 2)

print(f'Preço total (latas e galões): R${precoTotal}')