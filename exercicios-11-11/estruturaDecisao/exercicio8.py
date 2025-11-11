produto1 = float(input('Qual o preço do produto 1?'))
produto2 = float(input('Qual o preço do produto 2?'))
produto3 = float(input('Qual o preço do produto 3?'))

if produto1 < produto2 and produto1 < produto3:
    print(f'Compre o produto 1, pois custa R${produto1} é mais barato!')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Compre o produto 2, pois custa R${produto2} é mais barato!')
else:
    print(f'Compre o produto 3, pois custa R${produto3} é mais barato!')