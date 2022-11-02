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
            elif i != (len(self.rota)-1): #Adiciona outras coordenadas (menos a ultima)
                menordist = 99999999999999999.0
                posicaoexiste = False
                for j in range(i, len(self.rota)): #'J' assume todas as posições em self.rota à frente de newrota.rota[ultima]
                    if self.rota[j] not in newrota.rota:#Ignora coordenadas já adicionadas em newrota
                        dist = newrota.rota[i-1].distancia(self.rota[j]) #Compara a distancia de 'newrota[ultima]' e as coordenadas à frente
                        if dist < menordist:#Coloca a coordenada com menor distancia em newrota
                            menordist = dist
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
