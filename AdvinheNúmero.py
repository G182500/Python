import random

n = random.randrange(1, 1001) #gera um número inteiro no intervalo (x, y-1)

print(n)

print("Escolhi um número entre 1 e 1000. Você consegue adivinhar qual é ?")
palpite = int(input("Digite seu primeiro palpite:"))

if palpite == n:
    print("Você é PROFISSIONAL! Acertou de primeira")

while palpite != n:
    if palpite > n:
        diferenca = palpite - n
        if diferenca > 50:
            print("Muito grande!")

    else:
        diferenca = n - palpite
        if diferenca > 50:
            print("Muito pequeno!")

    if diferenca <= 10:
        print("Passou perto!")

    elif diferenca <= 50: 
        print("Está chegando perto!")

    palpite = int(input("Digite seu novo palpite:"))

print("PARABÉNS!! Você acertou")