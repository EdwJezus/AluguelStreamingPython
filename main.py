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

####################################Classe usuário

class Convidado():
  def __init__(self, creditos):
    self.creditos = creditos
  def calculaCreditos(self, projeto):
    self.creditos = self.creditos - projeto.preco
    return self.creditos
  def maisCreditos(self, dinheiro):
    self.creditos = self.creditos + dinheiro
    return self.creditos
  def getCreditos(self):
    return self.creditos

convidado1 = Convidado(0)####### COLOCANDO DINHEIRO

################################### Listas

filmes = []
series = []
diretores = []
generos = []
alugueis = []

################################### Menu

print('')
print('========NETFLIX=======')
print('')
print('      Bem Vindo!')

quest = 'n'
while quest != '11': 

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
  print('----------------------')
  print('9) Ver Carteira')
  print('10) Ver Alugueis')
  print('----------------------')
  print('11) Sair')
  print('======================')
  print('')
  quest = input('O que deseja fazer? ')
  print('')

###################################################### Cadastro
############ Cadastrar Filme

  if quest == '1':
    titulo1 = input('Titulo: ').upper()
    ano1 = int(input('Ano: '))
    diretor1 = ''
    preco1 = int(input('Preço: $ '))
    duracao1 = int(input('Duracao em minutos: '))

    print('')
    print('===========')
    print('  GENÊROS  ')
    print('===========')
    for g in generos:
      print(f'- {g.getName()}')
    print('===========')

    genero_nome1 = input('Genêro: ').upper()

    genero_associado1 = None
    for genero in generos:
      if genero.getName() == genero_nome1:
        genero_associado1 = genero
        break
    
    if genero_associado1:
      filme1 = Filme(titulo1, ano1, genero_associado1, preco1, diretor1, duracao1)

      print('============')
      print(' DIRETORES')
      print('============')
      for d in diretores:
        print(f'- {d.getNome()}')
      print('============')
  
      diretor_nome = input('Diretor: ').upper()
  
      diretor_associado = None
      for diretor in diretores:
          if diretor.getNome() == diretor_nome:
              diretor_associado = diretor
              break
  
      if diretor_associado:
          filme1 = Filme(titulo1, ano1, genero_associado1, preco1, diretor_associado, duracao1)
          filmes.append(filme1)
          print('O filme cadastrado com sucesso!')
      else:
          print('Diretor não encontrado.')
          print('Filme NÃO cadastrado.')
    else:
      print('Genêro não encontrado.')
      print('Filme NÃO cadastrado.')

############ Cadastrar Serie

  elif quest == '2':
    titulo2 = input('Titulo: ').upper()
    ano2 = int(input('Ano: '))
    preco2 = int(input('Preço: $ '))
    temporadas = int(input('Quantidade de Temporadas: '))
    qntEps = int(input('Quantidade de episodios por temporada: '))
    duracaoEps = int(input('Duracao dos episodios em minutos: '))

    print('')
    print('===========')
    print('  GENÊROS  ')
    print('===========')
    for g in generos:
      print(f'- {g.getName()}')
    print('===========')
    genero_nome = input('Genêro: ').upper()
    print('')

    genero_associado = None
    for genero in generos:
        if genero.getName() == genero_nome:
            genero_associado = genero
            break

    if genero_associado:
        serie1 = Serie(titulo2, ano2, genero_associado, preco2, temporadas, duracaoEps, qntEps)
        series.append(serie1)
        print('A série foi cadastrada com sucesso!')
    else:
        print("Genêro não encontrado.")
        print('Série NÃO cadastrada.')

############ Cadastrar Diretor

  elif quest == '3':
    nome = input('Nome do diretor: ').upper()
    idade = int(input('Idade: '))
    nacionalidade = input('Nacionalidade: ').upper()
    diretor1 = Diretor(nome, idade, nacionalidade)
    diretores.append(diretor1)
    print('O Diretor foi cadastrado com sucesso!')

############ Cadastrar Genero

  elif quest == '4':
    name = input('Genêro: ').upper()
    info = input('Informações do genêro: ').upper()
    genero1 = Genero(name, info)
    generos.append(genero1)
    print('O Genêro foi cadastrado com sucesso!')

################################################## Pesquisa
############ Pesquisar Filme

  elif quest == '5':
    print('============')
    print('LISTA FILMES')
    print('============')
    for i in filmes:
      print(f'- {i.getTitulo()}')
    print('============')

    escolhe_filme = input('Qual filme deseja saber informações? (digite o titulo) ').upper()
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
      print(f'***Genero: {filme_escolhido.getGenero()}')
      print(f'Genero: {filme_escolhido.genero.getName()}')
      print(f'***Diretor: {filme_escolhido.getDiretor()}')
      print(f'Diretor: {filme_escolhido.diretor.getNome()}')
      print(f'Duração total: {filme_escolhido.calculaDuracaoTotal()} Minutos')
      print(f'Preço aluguel do filme: $ {filme_escolhido.getPreco()}')
      print('')
      ###################Aluguel
      aluguel = input('Deseja alugar o filme? (s/n) ')
      if aluguel == 's':
        if (filme_escolhido.getPreco()) <= (convidado1.getCreditos()):
          alugueis.append(filme_escolhido)
          print('')
          print('Filme alugado com sucesso!')
          print(f'Valor atual em sua carteira: $ {convidado1.calculaCreditos(filme_escolhido)}')
        else:
          print('')
          print('Você não tem créditos suficientes para alugar esse filme!')
      else:
        print('')
      ###########################
    else:
      print("Filme não encontrado.")

############ Pesquisar Serie

  elif quest == '6':
    print('============')
    print('LISTA SÉRIES')
    print('============')
    for s in series:
      print(f'- {s.getTitulo()}')
    print('============')

    escolhe_serie = input('Qual série você deseja saber informações? ').upper()
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
      print(f'**Genero: {serie_escolhida.getGenero()}')
      print(f'Genero: {serie_escolhida.genero.getName()}')
      print(f'Duração total: {serie_escolhida.calculaDuracaoTotal()} Minutos')
      print(f'Preço aluguel da série: $ {serie_escolhida.getPreco()}')
      print('')
      ###################Aluguel
      aluguel2 = input('Deseja alugar a série? (s/n) ')
      if aluguel2 == 's':
        alugueis.append(serie_escolhida)
        print('')
        print('Série alugada com sucesso!')
        print(f'Valor atual em sua carteira: $ {convidado1.calculaCreditos(serie_escolhida)}')
      else:
        print('')
      ###########################
    else:
      print("Série não encontrada.")

############ Pesquisar Diretor

  elif quest == '7':
    print('============')
    print('  DIRETORES ')
    print('============')
    for d in diretores:
      print(f'- {d.getNome()}')
    print('============')

    escolhe_diretor = input('Digite o nome do diretor que deseja saber detalhes: ').upper()
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
      ######### Projetos do diretor #######################
      
      projetos_diretor = [projeto.getTitulo() for projeto in filmes if isinstance(projeto, Filme) and projeto.getDiretor() == diretor_escolhido]
      if projetos_diretor:
          for projeto in projetos_diretor:
              print('============')
              print('  PROJETOS ')
              print('============')
              print(f'- {projeto}')
              print('============')
      else:
          print('Nenhum projeto associado a este diretor encontrado.')
        
      ###############################################
    else:
      print("Diretor não encontrado.")

############ Pesquisar Genero

  elif quest == '8':
    print('===========')
    print('  GENÊROS  ')
    print('===========')
    for g in generos:
      print(f'- {g.getName()}')
    print('===========')

    escolhe_genero = input('Digite o nome do genêro que deseja saber detalhes: ').upper()
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
      ###### Projetos do genêro ############################

      projetos_genero = [projeto.getTitulo() for projeto in filmes if projeto.getGenero() == genero_escolhido] + [projeto.getTitulo() for projeto in series if projeto.getGenero() == genero_escolhido]
      if projetos_genero:
          print('============')
          print('  PROJETOS ')
          print('============')
          for projeto in projetos_genero:
              print(f'- {projeto}')
          print('============')
      else:
          print('Nenhum projeto associado a este gênero encontrado.')
  
    ######################################################
    else:
      print("Genero não encontrado.")

############ Ver Carteira

  elif quest == '9':
    print(f'Valor atual em sua carteira: $ {convidado1.getCreditos()}')
    print('')
    add_money = input('Deseja adicionar mais dinheiro? (s/n) ')
    if add_money == 's':
      print('')
      money = float(input('Quanto dinheiro deseja adicionar? $ '))
      print('')
      input('***Digite a senha para aprovar a transação: ')
      convidado1.maisCreditos(money)
      print('')
      print('-----------------------------------------')
      print(f'Você adicionou $ {money} na sua carteira!')
      print(f'O valor atual em sua carteira é de $ {convidado1.getCreditos()}')

############ Alugueis

  elif quest == '10':
    print('============')
    print('==ALUGUÉIS==')
    print('============')
    for a in alugueis:
      print(f'- {a.getTitulo()}')
    print('============')

############ Fim programa
  
  elif quest == '11':
    print('Programa Encerrado!')

############ Ajuda para erros

  else:
    print('')
    print('Comando Inválido! digite de 1 a 11 para a opção desejada.')
