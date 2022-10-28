from Coordenada import Coordenada

class Rota:
    def __init__(self):
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
        self.rota.append(c)

    #def comprimento(self):
