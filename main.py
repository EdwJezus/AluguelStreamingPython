class Projeto():
  def __init__(self, titulo, ano, umGenero, preco):
    self.titulo = titulo
    self.ano = ano
    self.genero = umGenero
    self.preco = preco
  def calculaDuracaoTotal(self):
    pass
  def setTitulo(self, titulo):
    self.titulo = titulo
  def setAno(self, ano):
    self.ano = ano
  def setGenero(self, novoGenero):
    self.genero = novoGenero
  def setPreco(self, preco):
    self.creditos = preco
  def getTitulo(self):
    return self.titulo
  def getAno(self):
    return self.ano
  def getGenero(self):
    return self.genero
  def getPreco(self):
    return self.preco

class Filme(Projeto):
  def __init__(self, titulo, ano, umGenero, preco, umDiretor, duracao):
    super().__init__(titulo, ano, umGenero, preco)
    self.diretor = umDiretor
    self.duracao = duracao
  def calculaDuracaoTotal(self):
    return self.duracao
  def setDiretor(self, novoDiretor):
    self.diretor = novoDiretor
  def getDiretor(self):
    return self.diretor

class Serie(Projeto):
  def __init__(self, titulo, ano, umGenero, preco, temporadas, duracaoEps, qntEps):
    super().__init__(titulo, ano, umGenero, preco)
    self.temporadas = temporadas
    self.duracaoEps = duracaoEps
    self.qntEps = qntEps
  def calculaDuracaoTotal(self):
    return (self.temporadas * self.duracaoEps * self.qntEps)
    
################################ Classes de associação

class Diretor():
  def __init__(self, nome, idade, nacionalidade):
    self.nome = nome
    self.idade = idade
    self.nacionalidade = nacionalidade
  def setNome(self, nome):
    self.nome = nome
  def setIdade(self, idade):
    self.idade = idade
  def setNacionalidade(self, nacionalidade):
    self.nacionalidade = nacionalidade
  def getNome(self):
    return self.nome
  def getIdade(self):
    return self.idade
  def getNacionalidade(self):
    return self.nacionalidade

class Genero():
  def __init__(self, name, info):
    self.name = name
    self.info = info
  def setName(self, name):
    self.name = name
  def setInfo(self, info):
    self.info = info
  def getName(self):
    return self.name
  def getInfo(self):
    return self.info

################################### Menu

print('')
print('======================')
print('=========MENU=========')
print('======================')
print('1) Cadastrar Filme')
print('2) Cadastrar Série')
print('3) Cadastrar Diretor')
print('4) Cadastrar Genêro')
print('----------------------')
print('5) Pesquisar Filme')
print('6) Pesquisar Série')
print('7) Pesquisar Diretor')
print('8) Pesquisar Genêro')
print('9) Sair')
print('======================')

filmes = []
series = []
diretores = []
generos = []
alugueis = []

quest = 'n'
while quest != '9': 

  print('')
  quest = input('O que deseja fazer? ')
  print('')

######################################################Cadastro
############Cadastrar Filme
  
  if quest == '1':
    titulo1 = input('Titulo: ')
    ano1 = int(input('Ano: '))
    genero1 = input('Genero: ')
    preco1 = int(input('Preço: '))
    diretor1 = input('Diretor: ')
    duracao1 = int(input('Duracao em minutos: '))
    filme1 = Filme(titulo1, ano1, genero1, preco1, diretor1, duracao1)
    filmes.append(filme1)
    print('O filme foi cadastrado com sucesso!')

############Cadastrar Serie
  
  elif quest == '2':
    titulo2 = input('Titulo: ')
    ano2 = int(input('Ano: '))
    genero2 = input('Genero: ')
    preco2 = int(input('Preço: '))
    temporadas = int(input('Quantidade de Temporadas: '))
    qntEps = int(input('Quantidade de episodios por temporada: '))
    duracaoEps = int(input('Duracao dos episodios em minutos: '))
    serie1 = Serie(titulo2, ano2, genero2, preco2, temporadas, duracaoEps, qntEps)
    series.append(serie1)
    print('A série foi cadastrada com sucesso!')

############Cadastrar Diretor

  elif quest == '3':
    nome = input('Nome do diretor: ')
    idade = int(input('Idade: '))
    nacionalidade = input('Nacionalidade: ')
    diretor1 = Diretor(nome, idade, nacionalidade)
    diretores.append(diretor1)
    print('O Diretor foi cadastrado com sucesso!')

############Cadastrar Genero

  elif quest == '4':
    name = input('Genêro: ')
    info = input('Informações do genêro: ')
    genero1 = Genero(name, info)
    generos.append(genero1)
    print('O filme foi cadastrado com sucesso!')

##################################################Pesquisa
############Pesquisar Filme
  
  elif quest == '5':
    print('============')
    print('LISTA FILMES')
    print('============')
    for i in filmes:
      print(f'- {i.getTitulo()}')
    print('============')
    
    escolhe_filme = input('Qual filme deseja saber informações? (digite o titulo) ')
    print('')
    filme_escolhido = None
    for filme in filmes:
      if filme.getTitulo() == escolhe_filme:
        filme_escolhido = filme
        break
    if filme_escolhido:
      print('')
      print(f'Titulo: {filme_escolhido.getTitulo()}')
      print(f'Ano: {filme_escolhido.getAno()}')
      print(f'Genero: {filme_escolhido.getGenero()}')
      print(f'Diretor: {filme_escolhido.getDiretor()}')
      print(f'Duração total: {filme_escolhido.calculaDuracaoTotal()} Minutos')
      print(f'Preço aluguel do filme: $ {filme_escolhido.getPreco()}')
      print('')
      ###################Aluguel
      aluguel = input('Deseja alugar o filme? ')
      if aluguel == 'sim':
        alugueis.append(filme_escolhido)
        print('')
        print('Filme alugado com sucesso!')
        print(f'Valor atual em sua carteira: $ {convidado1.calculaCreditos(filme_escolhido)}')
      else:
        print('')
      ###########################
    else:
      print("Filme não encontrado.")

############Pesquisar Serie

  elif quest == '6':
    print('============')
    print('LISTA SÉRIES')
    print('============')
    for s in series:
      print(f'- {s.getTitulo()}')
    print('============')
    
    escolhe_serie = input('Qual série você deseja saber informações? ')
    print('')
    serie_escolhida = None
    for serie in series:
      if serie.getTitulo() == escolhe_serie:
        serie_escolhida = serie
        break
    if serie_escolhida:
      print('')
      print(f'Titulo: {serie_escolhida.getTitulo()}')
      print(f'Ano: {serie_escolhida.getAno()}')
      print(f'Genero: {serie_escolhida.getGenero()}')
      print(f'Duração total: {serie_escolhida.calculaDuracaoTotal()} Minutos')
      print(f'Preço aluguel da série: $ {serie_escolhida.getPreco()}')
      print('')
      ###################Aluguel
      aluguel2 = input('Deseja alugar a série? ')
      if aluguel2 == 'sim':
        alugueis.append(serie_escolhida)
        print('')
        print('Série alugada com sucesso!')
        print(f'Valor atual em sua carteira: $ {convidado1.calculaCreditos(serie_escolhida)}')
      else:
        print('')
      ###########################
    else:
      print("Série não encontrada.")

############Pesquisar Diretor

  elif quest == '7':
    print('============')
    print('=DIRETORES=')
    print('============')
    for d in diretores:
      print(f'- {d.getNome()}')
    print('===========')
    
    escolhe_diretor = input('Digite o nome do diretor que deseja saber detalhes: ')
    diretor_escolhido = None
    for diretor in diretores:
      if diretor.getNome() == escolhe_diretor:
        diretor_escolhido = diretor
        break
    if diretor_escolhido:
      print('')
      print(f'Nome: {diretor_escolhido.getNome()}')
      print(f'Idade: {diretor_escolhido.getIdade()}')
      print(f'Nacionalidade: {diretor_escolhido.getNacionalidade()}')
      print('')
    else:
      print("Diretor não encontrado.")
    
############Pesquisar Genero

  elif quest == '8':
    print('=======')
    print('GENÊROS')
    print('=======')
    for g in generos:
      print(f'- {g.getName()}')
    print('===========')
    
    escolhe_genero = input('Digite o nome do genêro que deseja saber detalhes: ')
    genero_escolhido = None
    for genero in generos:
      if genero.getName() == escolhe_genero:
        genero_escolhido = genero
        break
    if genero_escolhido:
      print('')
      print(f'Nome: {genero_escolhido.getName()}')
      print(f'Informações: {genero_escolhido.getInfo()}')
      print('')
    else:
      print("Genero não encontrado.")

######Fim programa
  elif quest == '9':
    print('Programa Encerrado!')
