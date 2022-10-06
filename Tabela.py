from Linha import Linha

class Tabela:
    def add_cabecalho(self, valor):
        self.cabecalho.append(valor)
        
    def addLinha(self, car):
        if len(car.dados) == len(self.cabecalho.dados):
            self.dados.append(car)
        else:
            print("Tamanho da linha incompatível")
    
    #Simulando 2 construtores
    def __init__(self, nome_arquivo = None):   #nome_arquivo tem um default value 'None', se nenhum for passado
        
        #1 -> Se nenhum arquivo for passado, somente cria uma tabela vazia
        self.cabecalho = Linha()   #Cabeçalho é um objeto Linha e o construtor cria um atributo 'linha.dados = []' 
        self.dados = []
        
        #2 -> Se um arquivo for passado, atribui os valores desse arquivo a tabela
        if nome_arquivo != None:                       
            a = open(nome_arquivo, "r", encoding="utf8")
            numero_linhas = 0
            
            for linha in a:
                newlinha = eval(linha.replace("\n", ""))   #Remover o '\n' no fim da string
                if numero_linhas == 0:                     #'eval' converte uma string segura (ex: "['x', 4, 'a']") para lista
                    self.add_cabecalho(newlinha)
                else:
                    self.dados.append(newlinha)
                numero_linhas += 1
            a.close()

    def __str__(self):
        s = self.cabecalho.__str__() + "\n---------------------------------------\n"
        for item in self.dados:
            s += item.__str__()
            s += "\n"
        return s

    def ordena_por(self, v):
        indice = 0
        for valor in self.cabecalho.dados:
            if valor == v:
                break
            indice += 1

        '''def ordena(linha):
            return linha.dados[indice]'''
        def ordena(self):
            return self[indice]
        
        self.dados.sort(key = ordena)
        
    def writeFile(self, nome_arquivo):
        a = open(nome_arquivo, "w", encoding="utf8")
        
        a.write(self.cabecalho.__str__(False))
        
        for item in self.dados:
            a.write("\n" + str(item))
        
        a.close()