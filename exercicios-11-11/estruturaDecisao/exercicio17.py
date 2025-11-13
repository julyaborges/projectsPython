import calendar

ano = int(input('Digite aqui um ano:'))

print(f'O ano é bissexto? {calendar.isleap(ano)}')