print(f'-- INVESTIGAÇÃO --')
print(f'Responda apenas: s/n')

pontos = 0

telefoneVitima = input("Telefonou para a vítima?")

if telefoneVitima == 's' or telefoneVitima == 'S':
    pontos+= 1

localCrime = input("Esteve no local do crime?")

if localCrime == 's' or localCrime == 'S':
    pontos+= 1

moraPerto = input("Mora perto da vítima?")

if moraPerto == 's' or moraPerto == 'S':
    pontos+= 1

deviaVitima = input("Devia para a vítima?")

if deviaVitima == 's' or deviaVitima == 'S':
    pontos+= 1

trabalhoVitima = input("Já trabalhou com a vítima?")

if trabalhoVitima == 's' or trabalhoVitima == 'S':
    pontos+= 1

if pontos == 2:
    print('Suspeita')
elif pontos == 3 or pontos == 4:
    print('Cúmplice')
elif pontos == 5:
    print('Assassino')
else:
    print('Inocente')