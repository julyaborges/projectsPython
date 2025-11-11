campo = input('Digite algo: ')

# Tipo do campo
print(f'O tipo primitivo desse valor é {type(campo)}')

# Verifica se o valor do campo é um número
print(f'É um número? {campo.isnumeric()}')

# Verifica se o valor do campo é alfabético
print(f'É alfabético? {campo.isalpha()}')

# Verifica se o valor do campo está em maiúsculo
print(f'Está em maiúsculas? {campo.isupper()}')

# Verifica se o valor do campo é uma frase capitalizada
print(f'Está capitalizada? {campo.istitle()}')

# Verifica se o valor do campo é uma frase que inicia com a letra 'a'
print(f'A frase começa com a letra A? {campo.startswith('a')}')

# Verifica se o valor do campo é uma frase que termina com a letra 'o'
print(f'A frase termina com a letra O? {campo.endswith('o')}')

# Substitui o valor do campo por ou texto em específico
print(campo.replace(campo , "Python é legal"))

# Inverte maiúsculas e minúsculas
print(campo.swapcase())

# Confirma se o valor do campo é de um tipo em específico
print(f'O valor do campo é String? {isinstance(campo, str)}')