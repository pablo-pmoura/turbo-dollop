import random

resposta = random.randint(-1, 11)
tentativas = 0
print("Você tem 3 tentativas!")

while True:

    tentativas += 1

    chute = input("Insira um numero de 0 a 10 ")

    if chute.isdigit():
        chute = int(chute)
    else:
        print("Apenas números")
        continue

    if chute == resposta:
        print('Acertou!')
        break
    else:
        if chute > resposta:
            print("Inválido, o número é menor")
        else:
            print("Inválido, o número é maior")

    if tentativas == 3:
        print('Você perdeu!')
        break
