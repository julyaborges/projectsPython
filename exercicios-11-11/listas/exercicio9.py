numeros = []
somaQuadrados = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

for num in numeros:
    somaQuadrados += num ** 2

print(f"A soma dos quadrados é: {somaQuadrados}")
