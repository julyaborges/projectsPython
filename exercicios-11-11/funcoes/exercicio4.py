def positivo_negativo(n):
    if n < 0:
        return 'N'
    else:
        return 'P'
    
print(f'{positivo_negativo(5)}')
print(f'{positivo_negativo(0)}')
print(f'{positivo_negativo(-5)}')
