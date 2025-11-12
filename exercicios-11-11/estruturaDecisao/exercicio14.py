print(f'-- CALCULE SUA MÉDIA --')
 
nota1 = float(input('Insira a 1° nota:'))
nota2 = float(input('Insira a 2° nota:'))

media = (nota1 + nota2) / 2

conceito = ''

print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'Média: {media}')

if media <= 4.0:
    print(f'Conceito: E')
    print(f'REPROVADO')
elif media > 4.0 and media < 6.0:
    print(f'Conceito: D')
    print(f'REPROVADO')
elif media >= 6.0 and media < 7.5:
    print(f'Conceito: C')
    print(f'APROVADO')
elif media >= 7.5 and media < 9.0:
    print(f'Conceito: B')
    print(f'APROVADO')
else:
    print(f'Conceito: A')
    print(f'APROVADO')