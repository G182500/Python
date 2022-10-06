from Tabela import Tabela

class TabelaBD(Tabela):         #extends em Python (herança)
    def __init__(self, nome_arquivo = None):
        super().__init__(nome_arquivo)
        
    def conta(self, coluna):
        contagem = Tabela()
        contagem.add_cabecalho([coluna, "numero"])
        
        indice = 0
        for valor in self.cabecalho.dados:
            if valor == coluna:
                break
            indice += 1
        
        linha = 0
        for item in self.dados:
            achou = False
            contador = 0
            
            if linha == 0:
                for k in self.dados:
                    if self.dados[linha][indice] == k[indice]: 
                        contador += 1 
                contagem.dados.append([item[indice], contador])
            
            for j in contagem.dados:
                if j[0] == item[indice]:
                    achou = True
            if achou == False:
                for k in self.dados:
                    if self.dados[linha][indice] == k[indice]: 
                        contador += 1             
                contagem.dados.append([item[indice], contador])
            linha += 1
                
        return contagem

    def select(self, coluna, value):
        selected = Tabela()
        selected.cabecalho = self.cabecalho
        
        indice = 0
        for valor in self.cabecalho.dados:
            if valor == coluna:
                break
            indice += 1
        
        for item in self.dados:
            if item[indice] == value:
                selected.dados.append(item)
                
        return selected