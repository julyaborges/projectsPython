print('-----  Turnos  -----')
print('-- M - Matutino   --')
print('-- V - Vespertino --')
print('-- N - Noturno    --')

turno = input('Qual seu turno?')

if turno == 'M' or turno == 'm':
    print('Bom Dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa Noite!')
else:
    print('Valor Inválido!')