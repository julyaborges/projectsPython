import random

jogar_novamente = 's'

while jogar_novamente == 's':

    print("Bem-vindo(a) ao Jogo da Adivinhação!")

    num_aleatorio = random.randint(1, 50)

    jogadas = 0

    num_escolhido = 0

    print("Tente adivinhar o número entre 1 e 50.")

    while jogadas == 0 or num_escolhido != num_aleatorio:

        escolhido = int(input("Seu palpite? "))
        num_escolhido = escolhido

        jogadas += 1

        if num_aleatorio == num_escolhido:
            print(f"Parabéns! Você acertu em {jogadas} tentativas!")
        elif num_escolhido > num_aleatorio:
            print("Muito alto! Tente um número menor.")
        else:
            print("Muito baixo! Tente um número maior.")

    jogar_novamente = input("Quer jogar novamente?(s/n): ")

    if jogar_novamente == 'n':
        print("Obrigada por jogar!")