import PySimpleGUI as sg

def coletarNome():    
    #sg.theme_previewer()
    sg.theme('Dark2')
   
    #Cada item da matriz representa uma linha da coluna
    layout = [
        [sg.Image(r'synvia.png', key = '-LOGO-')], #.gif or .png only
        [sg.Text('Digite o seu nome:')],
        [sg.Input(key = '-NOME-')],
        [sg.Button('Confirmar'), sg.Button('Cancelar')]]
    
    #Segue um exemplo com mais de uma coluna
    #coluna1 = [[]]
    #coluna2 = [[]]
    #layout = [[sg.Column(coluna1),
    #            sg.VSeparator(),
    #            sg.Column(coluna2)
    #]]    
  
    window = sg.Window('Bem-vindo!').Layout(layout)
    #Também podemos definir o tamanho, acrescentando o parametro: margins = (100, 50)
  
    #A graphical user interface needs to run inside a infinite loop and wait for the user do something: 
    while True:
        event, values = window.read() #É necessário SEMPRE ter o método '.read()' dentro do loop 
        #print(event, values)
      
        if event in (None, 'Cancelar'):  #Se o evento for o click do botão 'Cancelar' ou 'X' (fechar a janela)
            window.close()
            break
      
        #Os inputs da interface são em forma de dicionário: cada item tem como key correspondente aquela 
        #declarada no layout (linha 8 por exemplo)
        if event == 'Confirmar':  #Se o evento for o click do botão 'Confirmar'
            nome = values['-NOME-']
            window.close()
            return nome
#---------------------------------------------------------------------------------------------------------------------#