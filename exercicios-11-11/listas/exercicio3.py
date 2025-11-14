notas = []

for i in range (4):
    nota = float(input(f'Insira a {i+1}° nota: '))
    notas.append(nota)

total = 0

for i in range(4):
    total += notas[i]
    
media = total / 4

print(f'Média: {round(media, 2)}')