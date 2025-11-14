medias = []
totalAcima = 0

for i in range (10):
    print(f'Insira as notas do aluno {i+1}:')
    nota1 = int(input('1° nota: '))
    nota2 = int(input('2° nota: '))
    nota3 = int(input('3° nota: '))
    nota4 = int(input('4° nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media)
    if media >= 7:
        totalAcima += 1

print(f'Alunos acima da média: {totalAcima}')