import random

gameover = False
pontos = 0

#PRIMEIRA RODADA
dado1 = random.randrange(1,7) #gera um número inteiro no intervalo (x, y-1)
dado2 = random.randrange(1,7)
print(dado1, dado2)
soma = dado1 + dado2

if soma == 7 or soma == 11:
    print("Parabéns, você VENCEU!!")
    gameover = True

elif soma == 2 or soma == 3 or soma == 12:
    print("Você PERDEU!!")
    gameover = True

else:
    pontos += soma
    print("Seus pontos: " + str(pontos))


#PROXIMAS RODADAS
while gameover == False:
    dado1 = random.randrange(1,7)
    dado2 = random.randrange(1,7)
    print(dado1, dado2)
    soma = dado1 + dado2

    if soma == pontos:
        print("Parabéns, você VENCEU!!")
        gameover = True

    elif soma == 7:
        print("Soma igual a 7, você PERDEU!!")
        gameover = True