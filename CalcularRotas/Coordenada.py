import math

class Coordenada:
        def __init__(self, *args):
            if len(args) == 0: #Nenhum argumento passado
                self.coordenada = (0, 0)

            elif len(args) == 1: #Um argumento passado...
                
                if type(args[0]) != tuple:              #Mas não é tupla
                    raise Exception("Parâmetro não é uma tupla. A tupla deve possuir dois elementos e os elementos devem ser números")
                
                elif type(args[0]) == tuple:            #E é do tipo 'Tupla'...
                    if len(args[0]) == 2:                                      #com tamanho 2...
                       
                        if type(args[0][0]) == int and type(args[0][1]) == int:                 #com tipo certo
                            self.coordenada = args[0]
                        elif type(args[0][0]) == float and type(args[0][1]) == float:               #com tipo certo
                            self.coordenada = args[0]
                        else:                                                                   #mas com tipo errado
                            raise Exception("Elemento da tupla não é int ou float")
                    
                    else:                                                      #mas tamanho errado
                        raise Exception("Numero de coordenadas inválido: " + str(len(args[0])))

            elif len(args) > 1: #Mais de um argumento passado
                raise Exception("Numero de argumentos errado: " + str(len(args)))
        
        def __str__(self):
            return str(self.coordenada)
        
        def distancia(self, c2): #euclidiana
            return math.sqrt((self.coordenada[0] - c2.coordenada[0]) ** 2 + (self.coordenada[1] - c2.coordenada[1]) ** 2) 
