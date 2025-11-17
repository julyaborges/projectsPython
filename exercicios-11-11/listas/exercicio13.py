temperaturas = []
mesesAno = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
somaTemp = 0

for i in range(len(mesesAno)):
    print(f'Insira a temperatura média do mês {i+1} - {mesesAno[i]}:')
    temp = int(input(''))
    temperaturas.append(temp)
    somaTemp += temp

mediaTemp = somaTemp / 12
print(f'Meses que a temperatura ficou acima da média anual:')

for i in range(len(mesesAno)):
    if temperaturas[i] > mediaTemp:
        print(f'Mês {i+1} - {mesesAno[i]} - Temperatura {temperaturas[i]}°C')