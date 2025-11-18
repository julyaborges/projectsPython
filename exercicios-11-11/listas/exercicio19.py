import math

votos = [0, 0, 0, 0, 0, 0]
totalVotos = 0
continuar = 's'

print(f'-- ENQUETE --')
print(F'Qual o melhor Sistema Operacional para uso em servidores?')
print(f'1- Windows Server')
print(f'2- Unix')
print(f'3- Linux')
print(f'4- Netware')
print(f'5- Mac OS')
print(f'6- Outro')

while continuar == 's':
    voto = int(input('Resposta: '))
    if voto == 0:
        continuar = 'n'
        print('Votação encerrada!')
    elif voto == 1:
        votos[0] += 1
        totalVotos += 1
    elif voto == 2:
        votos[1] += 1
        totalVotos += 1
    elif voto == 3:
        votos[2] += 1
        totalVotos += 1
    elif voto == 4:
        votos[3] += 1
        totalVotos += 1
    elif voto == 5:
        votos[4] += 1
        totalVotos += 1
    elif voto == 6:
        votos[5] += 1
        totalVotos += 1
    else:
        print(f'Número inválido! Responda novamente.')

percentual1 = math.ceil((votos[0] / totalVotos) * 100)
percentual2 = math.ceil((votos[1] / totalVotos) * 100)
percentual3 = math.ceil((votos[2] / totalVotos) * 100)
percentual4 = math.ceil((votos[3] / totalVotos) * 100)
percentual5 = math.ceil((votos[4] / totalVotos) * 100)
percentual6 = math.ceil((votos[5] / totalVotos) * 100)

print(f'Sistema Operacional - Votos - %')
print(f'-------------------------------------')
print(f'Windows Server - {votos[0]} - {percentual1}%')
print(f'Unix - {votos[1]} - {percentual2}%')
print(f'Linux - {votos[2]} - {percentual3}%')
print(f'Netware - {votos[3]} - {percentual4}%')
print(f'Mac OS - {votos[4]} - {percentual5}%')
print(f'Outro - {votos[5]} - {percentual6}%')
print(f'-------------------------------------')
print(f'Total {totalVotos}')

if percentual1 > percentual2 and percentual1 > percentual3 and percentual1 > percentual4 and percentual1 > percentual5 and percentual1 > percentual6:
    print(f'O Sistema Operacional mais votado foi o Windows Server, com {votos[0]} votos, correspondendo a {percentual1}% dos votos.')
elif percentual2 > percentual1 and percentual2 > percentual3 and percentual2 > percentual4 and percentual2 > percentual5 and percentual2 > percentual6:
    print(f'O Sistema Operacional mais votado foi o Unix, com {votos[1]} votos, correspondendo a {percentual2}% dos votos.')
elif percentual3 > percentual1 and percentual3 > percentual2 and percentual3 > percentual4 and percentual3 > percentual5 and percentual3 > percentual6:
    print(f'O Sistema Operacional mais votado foi o Linux, com {votos[2]} votos, correspondendo a {percentual3}% dos votos.')
elif percentual4 > percentual1 and percentual4 > percentual2 and percentual4 > percentual3 and percentual4 > percentual5 and percentual4 > percentual6:
    print(f'O Sistema Operacional mais votado foi o Netware, com {votos[3]} votos, correspondendo a {percentual4}% dos votos.')
elif percentual5 > percentual1 and percentual5 > percentual2 and percentual5 > percentual3 and percentual5 > percentual4 and percentual5 > percentual6:
    print(f'O Sistema Operacional mais votado foi o Mac OS, com {votos[4]} votos, correspondendo a {percentual5}% dos votos.')
else:
    print(f'Outros sistemas operacionais foram considerados melhores, com {votos[5]} votos, correspondendo a {percentual6}% dos votos.')