continuar = 's'

while continuar == 's':
    nomeAtleta = input('Nome do atleta:')

    if nomeAtleta == '':
        continuar = 'n'
        print(f'Fim do programa!')
    else:
        salto1 = float(input('Primeiro salto:'))
        salto2 = float(input('Segundo salto:'))
        salto3 = float(input('Terceiro salto:'))
        salto4 = float(input('Quarto salto:'))
        salto5 = float(input('Quinto salto:'))

        media = (salto1 + salto2 + salto3 + salto4 + salto5) / 5

        print(f'Resultado final:')
        print(f'Atleta: {nomeAtleta}')
        print(f'Saltos: {salto1} - {salto2} - {salto3} - {salto4} - {salto5}')
        print(f'Média dos saltos: {media}m')