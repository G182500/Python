from Linha import Linha

class Tabela:

    def __init__(self):            #construtor
        self.cabecalho = Linha()   #cabeçalho é um objeto Linha e o construtor cria um atributo 'linha.dados = []' 
        self.dados = []

    def add_cabecalho(self, valor):
        self.cabecalho.append(valor)

    def __str__(self):
        s = self.cabecalho.__str__() + "\n---------------------------------------\n"
        for item in self.dados:
            s += item.__str__()
            s += "\n"
        return s

    def addLinha(self, car):
        if len(car.dados) == len(self.cabecalho.dados):
            self.dados.append(car)
        else:
            print("tamanho da linha incompatível")

    def ordena_por(self, v):
        
        indice = 0
        for valor in self.cabecalho.dados:
            if valor == v:
                break
            indice += 1

        def ordena(linha):
            return linha.dados[indice]
        
        self.dados.sort(key = ordena)
        


