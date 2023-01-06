#ETAPA RESPONSÁVEL POR DESCOMPACTAR A PASTA BAIXADA NA ETAPA 1 E VERIFICAR/VALIDAR SE OS CERTIFICADOS ESTÃO NA PLANILHA
import configparser
import shutil  #Mover arquivos para diretórios
from zipfile import ZipFile  #Write and read ZIP files
from datetime import datetime
from funcoes import *
from pysimpleGUI import coletarNome
import os  #Functions to access, modify, and perform OS-related tasks such as access and modifying directories

data = datetime.today().strftime('%d-%m-%Y')

#CONFIG
config = configparser.ConfigParser()
config.read('python_config.ini')

#DECLARANDO CAMINHOS
downloads = os.path.expanduser("~") + config['CAMINHOS']['downloads'] #expanduser pega o caminho home do Pc como string
sharepoint = os.path.expanduser("~") + config['CAMINHOS']['sharepoint']
planilha = sharepoint + config['CAMINHOS']['planilha']


#VERIFICA SE A PASTA JÁ EXISTE. CASO SIM, ELA É ZERADA
if os.path.isdir(sharepoint + '\Assinados'):
    shutil.rmtree(sharepoint + '\Assinados') #Exclui a pasta com conteudo
    os.mkdir(sharepoint + '\Assinados')      #Cria uma pasta vazia

if os.path.isdir(sharepoint + '\Conferir'):
    shutil.rmtree(sharepoint + '\Conferir')  #Exclui a pasta com conteudo
    os.mkdir(sharepoint + '\Conferir')       #Cria uma pasta vazia


#LOCALIZAR ARQUIVOS ZIPS BAIXADOS:
i = 0
for diretorio, sub, arquivo in os.walk(downloads): #A primeira execução do 'for' percorre a raiz do caminho, os próximos são em subpastas
    if i == 0:                                     #Atribui à uma lista, os items na raiz da pasta 'Download'
        itemsRaiz = arquivo
    else:                                          #Não permite verificar subpastas do caminho
        break
    i += 1


#EXTRAIR ARQUIVOS ZIPS BAIXADOS:
for item in itemsRaiz:
    if ".zip" in item:
        #Se o primeiro zip não foi descompactado:
        if os.path.isdir(os.path.expanduser("~") + '\Downloads\\' + data) == False:
            z = ZipFile(downloads + '\\' + item, 'r') #Nome arquivo ZIP, abrir no modo (leitura ou escrita)
            z.extractall(downloads + '\\' + data)     #If the folder passed does not exist, this method will create one
            z.close()
       

#SALVAR OS NOMES DOS PDFS NA VARIAVEL(LISTA) 'ITEMSPDF':
certificados = downloads + '\\' + data + '\Certificados' 
i = 0
for diretorio, sub, arquivo in os.walk(certificados):
    if i == 0:
        itemsPDF = arquivo
    else:
        break
    i += 1


#MUDEI
#VERIFICAR ARQUIVOS EM 'ITEMSPDF'
i = 0
for item in itemsPDF:
    aprovado = True
    print('--------------------------------------------------------------------------------------------------------------------------')
    print(item)
    
    if i < (len(itemsPDF)-1): #Se não for o ultimo arquivo:
        if itemsPDF[i + 1][len(item) - 5] != '0' or item == itemsPDF[i + 1]: #Remover arquivos duplicados OU se o próximo arquivo tem final diferente de 'R0' 
            os.remove(certificados + '\\' + item) #Deleta o item atual da pasta
            aprovado = False
        
    if aprovado == True: #Se o arquivo não foi deletado, verificar se os dados do arquivo batem com a planilha
        retorno = buscarPlanilha(planilha, coletarInfosPDF(certificados + '\\' + item), item)
        
        if retorno[0] == False: #Se não for validado, ele NÃO é salvo
            os.remove(certificados + '\\' + item)
        
        else: 
            #Se for validado, mover para Conferir:
            shutil.move(certificados + '\\' + item, sharepoint + '\Conferir')
            #Renomear PDF:
            data = datetime.today().strftime('%d-%m-%Y')
            novoNome = "CC_" + retorno[1] + "_" + datetime.today().strftime('%Y') + "_" + datetime.today().strftime('%m') + ".pdf"
            os.replace(sharepoint + '\Conferir\\' + item, sharepoint + '\Conferir\\' + novoNome)  
    i += 1