#Criar um programa que desafia o usuário a adivinhar um número gerado aleatoriamente pelo computador.
#O programa deve gerar um número entre 1 e 100. [FEITO]
#O usuário terá um número limitado de tentativas para adivinhar o número (por exemplo, 10 tentativas). []
#A cada tentativa, o programa deve informar se o número escolhido pelo usuário é maior ou menor que o número gerado. []
#Quando o usuário acerta o número ou esgota as tentativas, o programa termina e exibe uma mensagem. []
import random

numAleatorio = random.randint(1,100)
i = 0

while i < 10:
    chute = int(input(f"{i+1}º Tentativa - Chute um número inteiro aleatório entre 1 e 100: "))
    if chute == numAleatorio:
        print(f"Parabéns, você acertou, o número realmente era: {numAleatorio}!")
        break
    elif chute > numAleatorio:
        print("Errou! Seu número é MAIOR do que o número sorteado!")
        i += 1
    elif chute < numAleatorio:
        print("Errou! Seu número é MENOR do que o número sorteado!")
        i += 1

if i == 10:
    print("Você esgotou suas tentativas.")
print("O jogo acabou.")