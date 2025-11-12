inteiro1 = int(input("Insira o 1° número inteiro:"))
inteiro2 = int(input("Insira o 2° número inteiro:"))
real = float(input("Insira um número real:"))

calculo1 = (inteiro1 * 2) * (inteiro2 / 2)
calculo2 = (inteiro1 * 3) + real
calculo3 = real ** 3

print(f'O produto do dobro do primeiro com metade do segundo é: {calculo1}')
print(f'A soma do triplo do primeiro com o terceiro: {calculo2}')
print(f'O terceiro elevado ao cubo: {calculo3}')