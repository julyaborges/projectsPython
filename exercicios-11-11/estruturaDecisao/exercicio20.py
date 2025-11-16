nota1 = float(input('Digite a 1° nota:'))
nota2 = float(input('Digite a 2° nota:'))
nota3 = float(input('Digite a 3° nota:'))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção')
else: 
    print('Reprovado')
