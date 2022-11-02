from Coordenada import Coordenada
import random

class Rota:
    def __init__(self, r = None):
        if r != None:
            self.rota = r
        else:
            self.rota = []

    def __str__(self):
        saida = str(self.rota[0])
        i = 0
        for coordenada in self.rota:
            if i != 0:
                saida += "->" + str(coordenada)
            i += 1
        saida += "->" + str(self.rota[0])
        return saida

    def addCoord(self, c):
        if c != Coordenada:
            self.rota.append(c)
        else:
            self.rota.append(c.coordenada)

    def comprimento(self):
        dist_euclidianas = []
        tamanho_rotas = len(self.rota)
        for i in range(tamanho_rotas):
            if i <= (tamanho_rotas - 2):
                dist_euclidianas.append(self.rota[i].distancia(self.rota[i+1]))
            elif i == (tamanho_rotas - 1):
                dist_euclidianas.append(self.rota[i].distancia(self.rota[0]))
        return sum(dist_euclidianas)

    def copy(self):
        copia = Rota()
        for coord in self.rota:
            copia.rota.append(coord)
        return copia
    
    def shuffle(self):
        self.rota = tuple(random.sample(self.rota, len(self.rota)))
        
    def reduzir(self):
        newrota = Rota() #newrota.rota = []
        i = 0
        for coord in self.rota:
            if i == 0: #Adiciona o ponto de inicio em newrota
                newrota.rota.append(coord)
                #print("posicao inicial é " + str(coord))
            elif i != (len(self.rota)-1): #Adiciona outras coordenadas de acordo com as distancias (menos as duas ultimas) #2 ->1
                menordist = 99999999999999999.0
                posicaoexiste = False
                for j in range(len(self.rota)): #'J' assume todas as posições que não foram adicionadas
                    if newrota.rota[i-1].menor(self.rota[j]):
                    #Acima, pula a comparação de newrota[ultima] e j[i-1] (são os mesmos) e coordenadas menores que a atual (já foram)
                        dist = newrota.rota[i-1].distancia(self.rota[j]) #Compara a posição mais recente de newrota com j
                        #print("Distancia entre " + str(newrota.rota[i-1]) + str(self.rota[j]))
                        if dist < menordist:
                            menordist = dist
                            #print("Menor distancia: "+ str(menordist))
                            if posicaoexiste == False:
                                newrota.rota.append(self.rota[j])
                                posicaoexiste = True
                            else:
                                newrota.rota[i] = self.rota[j]
            else:
                for ultima in self.rota:
                        if ultima not in newrota.rota:
                            newrota.rota.append(ultima)
            i += 1
        self.rota = []
        self.rota = newrota.rota
