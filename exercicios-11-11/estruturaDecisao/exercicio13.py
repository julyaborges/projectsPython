num_semana = int(input("Insira um número de 1 a 7: "))

match num_semana:
    case 1:
        print("1 - Domingo")
    case 2:
        print("2 - Segunda-feira")
    case 3:
        print("3 - Terça-feira")
    case 4:
        print("4 - Quarta-feira")
    case 5:
        print("5 - Quinta-feira")
    case 6:
        print("6 - Sexta-feira")
    case 7:
        print("7 - Sábado")
    case _:
        print("Valor inválido")
