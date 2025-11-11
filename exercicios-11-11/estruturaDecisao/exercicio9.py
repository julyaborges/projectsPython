lista = []

i = 0

while (i < 3):
    
    i += 1
    
    entrada = input("Digite um valor: ").strip()

    lista.append(entrada)

ordenada = sorted(lista, reverse=True)

print(f'Na ordem preenchida: {lista}')
print(f'Em ordem decrescente: {ordenada}')