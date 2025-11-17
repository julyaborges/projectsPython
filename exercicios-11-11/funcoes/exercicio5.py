def soma_imposto(taxa_imposto, custo):
    return custo + (custo * taxa_imposto)

print(f'{soma_imposto(0.05, 100)}')