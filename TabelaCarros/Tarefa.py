# Tarefa em grupo de 3 pessoas.
# Nomes dentro do arquivo. Apenas um aluno submete o arquivo.

# Crie uma classe Linha. Ela deve estar dentro de um arquivo chamado
# Linha.py.
# Crie um construtor para Linha. O construtor cria um atributo
# chamado "dados". "Dados" deve ser inicializado com uma lista vazia.
#
# Crie um método (função da classe) append dentro de Linha que recebe um valor.
# Se o valor não for uma lista,
# com este valor deve ser feito um append no final de dados.
# Se o valor for uma lista,
# esta lista deve ser incorpordada na lista "dados".
#
# Crie um método que converte uma linha para string. Deve imprimir
# todos os elementos da linha seguido do número de elementos da linha
# entre parenteses. (veja o exemplo abaixo).
#
# Crie uma instância (objeto) do tipo linha.
#
# Crie uma função que mostra o comprimento de uma linha.
#
#
#  Abaixo veja o uso da classe Linha.


from Linha import Linha

aux = Linha()
# o parâmetro é uma lista
aux.append([1, 2, 3, 4, 3])
# o parâmetro não é uma lista
aux.append(2)

print(aux)

# Saída:
#  [1, 2, 3, 4, 3, 2](6)

# Crie agora uma classe Tabela dentro de um arquivo Tabela.py
# No construtor da classe Tabela deve ser criado uma variável
# chamada "cabecalho" do tipo Linha e uma variável "dados" inicializada
# com uma lista vazia.
#
# Crie um método (função da classe) na classe Tabela chamado
# add_cabecalho. O valor passado para este método deve ser
# atribuída à variável cabeçalho, através do método  "append(valor)"
# já implementado na classe linha.
#
#  Crie uma função que adiciona uma linha de dados na tabela. A linha
#  deve ser passada como parâmetro.
#  Se o comprimento da linha não for compatível com o tamanho do cabeçalho,
#  deve ser impresso uma mensagem de erro (tamanho da linha incompatível).
#
#  Faça uma função que imprime uma tabela conforme mostrado abaixo

from Tabela import Tabela

tab = Tabela()
tab.add_cabecalho(["Placa", "Ano", "Marca", "Modelo"])
carro = Linha()
carro.append(["ZBB1B11", 1998, "Ford", "Ka"])
tab.addLinha(carro)
carro = Linha()
carro.append(["BBB1B22", 2010, "Ford", "Fusion"])
tab.addLinha(carro)
carro = Linha()
carro.append(["DBB1B33", 2020, "Fiat", "Uno"])
tab.addLinha(carro)
carro = Linha()
carro.append(["CBB1B00", 2015, "Volks", "Gol"])
tab.addLinha(carro)

print(tab)

carro = Linha()
carro.append(["CBB1B00", 2015, "Volks", "Gol", "Teste"])
tab.addLinha(carro)

#exit(0)

# saída do código acima:
# ['Placa', 'Ano', 'Marca', 'Modelo'](4)
# ---------------------------------------
# ['ZBB1B11', 1998, 'Ford', 'Ka'](4)
# ['BBB1B22', 2010, 'Ford', 'Fusion'](4)
# ['DBB1B33', 2020, 'Fiat', 'Uno'](4)
# ['CBB1B00', 2015, 'Volks', 'Gol'](4)
#
# Tamanhos incompatíveis
#
# Finalmente você deve implementar uma função
#     def ordena_por(self, valor):
# que recebe o valor presente em cabeçalho e faz a ordenação
# pela coluna correspondente.
#
# Número de linhas gastas na função: 10 (5+5)
# 5 linhas em ordena_por(self, valor):
# 5 linhas na classe Linha.
# #


tab.ordena_por("Ano")
print(tab)

'''
#print(tab)

#  Saída:
#  ['Placa', 'Ano', 'Marca', 'Modelo'](4)
# ---------------------------------------
# ['ZBB1B11', 1998, 'Ford', 'Ka'](4)
# ['BBB1B22', 2010, 'Ford', 'Fusion'](4)
# ['CBB1B00', 2015, 'Volks', 'Gol'](4)
# ['DBB1B33', 2020, 'Fiat', 'Uno'](4)
#
#
tab.ordena_por("Modelo")
print(tab)

# Saída:
# ['Placa', 'Ano', 'Marca', 'Modelo'](4)
# ---------------------------------------
# ['BBB1B22', 2010, 'Ford', 'Fusion'](4)
# ['CBB1B00', 2015, 'Volks', 'Gol'](4)
# ['ZBB1B11', 1998, 'Ford', 'Ka'](4)
# ['DBB1B33', 2020, 'Fiat', 'Uno'](4)
#

tab.ordena_por("Placa")
print(tab)

# Saída:
# ['Placa', 'Ano', 'Marca', 'Modelo'](4)
# ---------------------------------------
# ['BBB1B22', 2010, 'Ford', 'Fusion'](4)
# ['CBB1B00', 2015, 'Volks', 'Gol'](4)
# ['DBB1B33', 2020, 'Fiat', 'Uno'](4)
# ['ZBB1B11', 1998, 'Ford', 'Ka'](4)
#

'''