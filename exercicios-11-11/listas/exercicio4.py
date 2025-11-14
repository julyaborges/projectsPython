vetorCarac = []
totalConsoante = 0

for i in range (10):
    letras = input(f'Insira uma letra: ')
    vetorCarac.append(letras)

for i in range (10):
    if vetorCarac[i] != 'a' and vetorCarac[i] != 'e' and vetorCarac[i] != 'i' and vetorCarac[i] != 'o' and vetorCarac[i] != 'u':
        totalConsoante += 1
        print(f'Consoante: {vetorCarac[i]}')

print(f'Total de consoantes: {totalConsoante}')