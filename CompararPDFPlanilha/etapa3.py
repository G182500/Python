#ETAPA RESPONSÁVEL POR ASSINAR/COLOCAR MARCA D'AGUA NOS PDF'S VALIDADOS (ETAPA 2) E SALVA-LOS NO BD

from pysimpleGUI import coletarNome
from funcoes import *
import os
from datetime import datetime
import shutil  #Mover arquivos para diretórios

nome = coletarNome()
data = datetime.today().strftime('%d-%m-%Y')
sharepoint = os.path.expanduser("~") + config['CAMINHOS']['conferir']

i = 0
for diretorio, sub, arquivo in os.walk(sharepoint): #Listar elementos da pasta informada pelo caminho
    if i == 0:                                      #Atribui à uma lista, os items na raiz da pasta 'sharepoint'
        itemsRaiz = arquivo
    else:                                           #Não permitir verificar subpastas do caminho
        break
    i += 1

for item in itemsRaiz:
    shutil.move(sharepoint + "\\" + item, os.path.expanduser("~") + config['CAMINHOS']['assinados'])  #Move pdf de pasta
    assinarPDF(nome, item, data) #Chama internamente as funções 'watermark()' e 'salvarBanco()'