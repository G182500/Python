import shutil  #Mover arquivos para diretórios
from zipfile import ZipFile  #Write and read ZIP files
from datetime import datetime
from validarPDF import *
from pysimpleGUI import coletarNome
import os  #Functions to access, modify, and perform OS-related tasks such as access and modifying directories

caminho1 = os.path.expanduser("~") + '\Downloads' #expanduser pega o caminho home do Pc como string
data = datetime.today().strftime('%d-%m-%Y')
nome = coletarNome()
#-------------------------------------------------------------------------------------------------------------------------------------------#
#Verifica se a pasta já existe. Caso sim, ela é excluida para ser substituida
if os.path.isdir(caminho1 + '\\' + data):
    shutil.rmtree(caminho1 + '\\' + data)
#-------------------------------------------------------------------------------------------------------------------------------------------#
#A primeira execução do 'for' percorre a raiz do caminho, os próximos são em subpastas
i = 0
for diretorio, sub, arquivo in os.walk(caminho1): #Listar elementos da pasta informada pelo 'caminho'
    if i == 0:                                    #Atribui à uma lista, os items na raiz da pasta 'Download'
        itemsRaiz = arquivo
    else:                                         #Não permite verificar subpastas do caminho
        break
    i += 1

for item in itemsRaiz: #Extrair arquivos ZIPS baixados
    if ".zip" in item:
        z = ZipFile(caminho1 + '\\' + item, 'r') #Nome arquivo ZIP, abrir no modo (leitura ou escrita)
        z.extractall(caminho1 + '\\' + data) #If the folder passed does not exist, this method will create one
        z.close()
#-------------------------------------------------------------------------------------------------------------------------------------------#
#Atribuir os nomes dos PDFs na variavel 'itemsPDF'
certificados = caminho1 + '\\' + data + '\Certificados' 
i = 0
for diretorio, sub, arquivo in os.walk(certificados):
    if i == 0:
        itemsPDF = arquivo
    else:
        break
    i += 1
#-------------------------------------------------------------------------------------------------------------------------------------------#
#Verificar arquivos em 'itemsPDF'
planilha = caminho1 + '\\FOR-XXX_Gerenciamento_de_vidrarias_volumétricas.xlsx'
os.mkdir(caminho1 + '/' + data + '/' + 'NaoAprovados')  #Cria a pasta para salvar os PDF's
os.mkdir(caminho1 + '/' + data + '/' + 'Assinados')

i = 0
for item in itemsPDF:
    aprovado = True
    print('--------------------------------------------------------------------------------------------------------------------------')
    print(item)
    if i < (len(itemsPDF)-1): #Se não for o ultimo arquivo:
        if itemsPDF[i + 1][len(item) - 5] != '0': #Verificar se o próximo arquivo tem final diferente de 'R0'
            os.remove(certificados + '\\' + item) #Deleta o item atual da pasta
            aprovado = False
        elif item == itemsPDF[i + 1]: #Remover arquivos duplicados
            os.remove(certificados + '\\' + item)
            aprovado = False
        
    if aprovado == True: #Se o arquivo não foi deletado, verificar se os dados do arquivo batem com a planilha
        if buscarPlanilha(planilha, coletarInfosPDF(certificados + '\\' + item)) == False: 
            print("Os dados do PDF '" + item + "' NÃO bateram com a planilha! Arquivo salvo na pasta 'NaoAprovados'")
            #os.remove(certificados + '\\' + item)
            shutil.move(certificados + '\\' + item, caminho1 + '/' + data + '/' + 'NaoAprovados')
        else:
            assinarPDF(nome, item, data) #Internamente chama a função "addWatermark"
    i += 1
#-------------------------------------------------------------------------------------------------------------------------------------------#

'''
arquivo = 'D:\LV01061-32987-22-R1.pdf' #Nome do arquivo com o caminho
planilha = 'D:\FOR-XXX_Gerenciamento_de_vidrarias_volumétricas.xlsx'
ok = buscarPlanilha(planilha, coletarInfosPDF(arquivo))

#Renomear
os.rename("diretorio/origem/nome-do-arquivo", "diretorio/destino/novo-nome-arquivo")
shutil.move("diretorio/origem/nome-do-arquivo", "diretorio/lugar-para-onde-sera-movida/novo-nome-do-arquivo")
'''