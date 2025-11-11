ano_nascimento = int(input("Insira o seu ano de nascimento: "))

idade = 2025 - ano_nascimento

if idade > 65:
    print("Você já pode se aposentar")
else:
    print("Você ainda não pode se aposentar")