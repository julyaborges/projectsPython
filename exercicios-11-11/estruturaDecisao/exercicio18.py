from datetime import datetime

data = input('Insira uma data no formato: dia/mês/ano:')

try:
    dataValida = datetime.strptime(data, "%d/%m/%Y")
    print(f'Data válida!')
except ValueError: 
    print(f'Data inválida')