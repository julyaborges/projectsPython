print("-- Cálculo de tempo de download --")

tamanho = float(input("Tamanho do arquivo (em MB): "))
velocidade = float(input("Velocidade da internet (em Mbps): "))

tamanhoMegabits = tamanho * 8

tempoSegundos = tamanhoMegabits / velocidade

tempoMinutos = tempoSegundos / 60

print(f"Tempo aproximado de download: {round(tempoMinutos, 2)} minutos")
