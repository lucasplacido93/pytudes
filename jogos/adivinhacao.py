print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")
print("Você digitou ", chute_str)
chute = int (chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou! O Seu chute foi maior do que o número secreto.")
    elif(chute < numero_secreto):
        print("Você errou! O Seu chute foi menor do que o número secreto.")
print("Fim do jogo")