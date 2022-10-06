class Linha:

    def __init__(self):   #construtor
        self.dados = []   #cria um atributo 'dados' e atribui uma lista vazia 

    def append(self, valor):
        if type(valor) == list:
            self.dados.extend(valor)

        else:
            self.dados.append(valor)

    def __str__(self, exibir_tamanho = True):
        if exibir_tamanho:
            tamanho = len(self.dados)
            s = str(self.dados)
            return s + " (" + str(tamanho) + ")"
        
        else:
            s = str(self.dados)
            return s
'''
l1 = Linha ()
l1.append([1, 2, 3])
l1.append([4, 5, 6])
l1.append(10)
print(l1.dados)
print(l1) #str foi reescrito, então print(l1) não retorna 'Objeto Lista', mas sim a string do return 
'''