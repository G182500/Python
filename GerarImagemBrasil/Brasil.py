from PIL import Image

c = open("coordenadas.txt", "r")

cores = [['AC',(255, 0, 0)], ['AL', (0, 255, 0)], ['AP', (0,0,255)], ['AM', (255, 105, 180)], ['BA', (139,0,0)], 
         ['CE', (0,191,255)], ['DF', (0,100,0)], ['ES', (150, 75, 0)], ['GO', (0, 0, 0)], ['MA', (255, 102, 51)], 
         ['MT', (220,20,60)], ['MS', (75,0,130)], ['MG', (128,0,128)], ['PA', (105,105,105)], ['PB', (47,79,79)],
         ['PR', (128,128,0)], ['PE', (210,105,30)], ['PI', (218,165,32)], ['RJ', (255,127,80)], ['RN', (0,139,139)],
         ['RS', (65,105,225)], ['RO', (0,250,154)], ['RR', (255,99,71)], ['SC', (240,230,140)], ['SP', (189,83,107)],
         ['SE', (107,142,35)], ['TO', (143,188,143)]]
#Vermelho, Verde, Azul, Pink, VermelhoEscuro, AzulClaro, VerdeEscuro, Marrom, Preto, Laranja,
#Crimson, Indigo, Roxo, Cinza, Darkslategrey, Olive, Chocolate, Goldenrod, Coral, Darkcyan,
#Royalblue, MediumSpringGreen, Tomato, Khaki, DarkKhaki, OliveDrab, DarkSeaGreen

lista_coord = [] #matriz que representará o arquivo

n_linha = 0
for linha in c:
    aux = linha.replace("\n", "")
    newlinha = aux.split(';')  #dividir o conteúdo de uma string em substrings em forma de lista
    lista_coord.append([newlinha[0], newlinha[1], newlinha[2], float(newlinha[3]), float(newlinha[4])])

    if n_linha == 0:
        maior_lat = lista_coord[n_linha][3]
        menor_lat = lista_coord[n_linha][3]
        maior_long = lista_coord[n_linha][4]
        menor_long = lista_coord[n_linha][4]
        
    else:
        if lista_coord[n_linha][3] > maior_lat:
            maior_lat = lista_coord[n_linha][3]
        
        if lista_coord[n_linha][3] < menor_lat:
            menor_lat = lista_coord[n_linha][3]
            
        if lista_coord[n_linha][4] > maior_long:
            maior_long = lista_coord[n_linha][4]
        
        if lista_coord[n_linha][4] < menor_long:
            menor_long = lista_coord[n_linha][4]

    n_linha += 1
    
c.close()

#criando uma imagem 1001x1001 em branco
brasil = Image.new('RGB',(1001, 1001),(255, 255, 255))
#matriz que cada posição é um RGB(pixel)
pixels = brasil.load()

for item1 in lista_coord: #Procurando o estado correspondente na matriz cores
    achou = False
    for item2 in cores:
        if item1[2] == item2[0]:
            achou = True
            #ajustando proporção
            latitude = ((item1[3] - menor_lat)/(maior_lat - menor_lat)) * 1000
            longitude = ((item1[4] - menor_long)/(maior_long - menor_long)) * 1000
            
            pixels[latitude, longitude] = item2[1]  #Atribuindo a cor do estado no pixel
            break   

brasil = brasil.rotate(90)
brasil.save("Brasil", format = "png")

#brasil.show() #Mostrando uma imagem