def quantDigitos(num):
  return len(str(num))

num = int(input("Digite um número inteiro:"))

print(f"O número {num} tem {quantDigitos(num)} dígitos.")