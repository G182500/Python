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
