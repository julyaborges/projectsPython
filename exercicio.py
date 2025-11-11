import time

print('Iniciando o programa...');
time.sleep(3);

print('Bem vindo(a)! :)');

nome = input("Digite o seu nome: ");
idade = int(input("Digite a sua idade: "));

print("Olá ",nome," :)");
print("Vamos contar os números até a sua idade: ;)");
time.sleep(2);

for i in range (idade+1):
    time.sleep(0.5);
    print(i, " anos");

print("Agora digite uma mensagem:");
mensagem = input();

print("Você deseja deixar a mensagem como?");
print("1 - DEIXAR A MENSAGEM ASSIM");
print("2 - deixar assim");
print("3 - mudar a mensagem");
print("4 - repetir a mensagem");
escolha = int(input());

if escolha == 1:
    print(mensagem.upper());
elif escolha == 2:
    print(mensagem.lower());
elif escolha == 3:
    mudarMensagem = input("Insira a nova mensagem:");
    print("Essa é a nova mensagem: ",mudarMensagem);
elif escolha == 4:
    print(mensagem*5);
else:
    print("Número inválido");
    
print("Fim do Programa :)");