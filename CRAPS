'''CRAPS – Dois dados são lançados. Então soma-se as faces:
* Se a soma for 7 ou 11 na primeira rodada, o jogador ganha.
* Se for 2, 3 ou 12 na primeira rodada o jogador perde.
* Se a soma for 4, 5, 6, 8, 9 ou 10 na primeira rodada. Esta soma se torna o ponto do jogador.
* Para ganhar, o jogador continua jogando o dado até a soma ser igual a seu ponto. 
* O jogador perde se a soma for igual a 7.
'''

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
