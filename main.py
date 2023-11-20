from termcolor import cprint

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

convidado1 = Convidado(0)  ####### COLOCANDO DINHEIRO


################################### Listas

filmes = []
series = []
diretores = []
generos = []
alugueis = []

################################### Pré-Cadastro
DRAMA = Genero('DRAMA', 'CONSISTE EM SEQUENCIAS EMOCIONANTES.')

ACAO = Genero('AÇÃO', 'CONSISTE EM SEQUENCIAS DE ADRENALINA.')

COMEDIA = Genero('COMEDIA', 'CONSISTE EM SEQUENCIAS DE HUMOR')
#####
COPPOLA = Diretor('FRANCIS FORD COPPOLA', 84, 'AMERICANO')

WINDING = Diretor('NICOLAS WINDING REFN', 53, 'DINAMARQUÊS')

RIDLEY = Diretor('RIDLEY SCOTT', 85, 'BRITÂNICO')
#####
GODFATHER = Filme('O PODEROSO CHEFÃO', 1972, DRAMA, 24.99, COPPOLA, 175)

DRIVE = Filme('DRIVE', 2011, ACAO, 22.99, WINDING, 100)

BLADERUNNER = Filme('BLADE RUNNER', 1982, DRAMA, 23.99, RIDLEY, 117)
#####
THEOFFICE = Serie('THE OFFICE', 2005, COMEDIA, 30.99, 9, 25, 20)

BREAKINGBAD = Serie('BREAKING BAD', 2008, DRAMA, 24.99, 5, 50 , 13)

SEVERANCE = Serie('SEVERANCE', 2022, DRAMA, 24.99, 1, 50, 9)
####
generos.append(DRAMA)
generos.append(ACAO)
generos.append(COMEDIA)
diretores.append(COPPOLA)
diretores.append(WINDING)
diretores.append(RIDLEY)
filmes.append(GODFATHER)
filmes.append(DRIVE)
filmes.append(BLADERUNNER)
series.append(THEOFFICE)
series.append(BREAKINGBAD)
series.append(SEVERANCE)
############################################### Menu

print('''
⣶⡄⠀⣶⠀⢰⣶⣶⡆⠠⣶⣶⣶⡆⢰⣶⣶⣦⠀⣶⠀⠀⠀⣶⡆⠐⣶⠀⣰⡖
⣿⣷⡀⣿⠀⣸⣇⣀⡀⠀⠀⣿⠀⠀⢸⣇⣀⡀⠀⣿⠀⠀⠀⣿⡇⠀⠹⣷⡿⠁
⣿⡿⣷⣿⠀⣿⡟⠛⠁⠀⠀⣿⠀⠀⢸⡏⠉⠁⠀⣿⠀⠀⠀⣿⡇⠀⢠⣿⣇⠀
⣿⡇⢻⣿⠀⣿⣷⣶⡆⠀⠀⠿⠀⠀⠸⠇⠀⠀⠀⣿⣶⣶⠀⣿⡇⢀⣿⠋⢿⡆
⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
''')
print('')
print('==========NETFLIX=========')
print('')
print('        Bem Vindo!')

msg_continuar = 'Tecle ENTER para continuar.'

login = 'n'
while login != '3':
  print('')
  print('==========================')
  print('===========MENU===========')
  print('==========================')
  print('1) Entrar como Operador')
  print('2) Entrar como Convidado')
  print('--------------------------')
  print('3) Finalizar Programa')
  print('==========================')
  print('')
  login = input('O que deseja fazer? (1/2/3) ')

#################################################### Modo Operador

############################################## Login operador

  if login == '1':
    print('')
    print('===================')
    print('=======LOGIN=======')
    print('===================')
    op_user = input('Digite o usuario: ')
    op_senha = input('Digite a senha: ')
    print('===================')
    print('')
    

    if op_user == 'operador01' and op_senha == 'senha123':
      print('Login efetuado com sucesso!')
      print('Seja bem vindo operador!')

############################################## Menu

      quest = 'n'
      while quest != '5':

        print('')
        print('======================')
        print('=======OPERADOR=======')
        print('======================')
        print('1) Cadastrar Filme')
        print('2) Cadastrar Série')
        print('----------------------')
        print('3) Cadastrar Diretor')
        print('4) Cadastrar Genêro')
        print('----------------------')
        print('5) Sair')
        print('======================')
        print('')

        mensagem = '***obs: Já existem alguns genêros, diretores, filmes e séries pré-cadastrados. Porém se você deseja adicionar mais algum, basta cadastra-lo no modo operador.'
        cprint('\033[1m\033[3m' + mensagem, 'white', 'on_grey')
        
        print('')
        quest = input('O que deseja fazer? ')
        print('')

###################################################### Cadastro
############################################## Cadastrar Filme

        if quest == '1':
          print('========================')
          print('  FILMES JÁ CADASTRADOS ')
          print('========================')
          for i in filmes:
            print(f'- {i.getTitulo()}')
          print('========================')
          print('')

          print('- Cadastrando novo filme.')
          try:
            titulo1 = input('Titulo: ').upper()
            ano1 = int(input('Ano: '))
            diretor1 = ''
            preco1 = float(input('Preço: $ '))
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
              filme1 = Filme(titulo1, ano1, genero_associado1, preco1, diretor1,
                             duracao1)
  
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
                filme1 = Filme(titulo1, ano1, genero_associado1, preco1,
                               diretor_associado, duracao1)
                filmes.append(filme1)
                print('')
                print('O filme foi cadastrado com sucesso!')
                cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
                input('')
              else:
                print('Diretor não encontrado.')
                print('Filme NÃO cadastrado.')
                cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
                input('')
            else:
              print('Genêro não encontrado.')
              print('Filme NÃO cadastrado.')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')

          except ValueError:
            print('')
            print('Você digitou algo errado.')
            input('Tecle ENTER para voltar e tentar novamente.')

############################################## Cadastrar Serie

        elif quest == '2':
          print('========================')
          print('  SÉRIES JÁ CADASTRADAS ')
          print('========================')
          for s in series:
            print(f'- {s.getTitulo()}')
          print('========================')
          print('')

          print('- Cadastrando nova série.')
          try:
            titulo2 = input('Titulo: ').upper()
            ano2 = int(input('Ano: '))
            preco2 = float(input('Preço: $ '))
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
              serie1 = Serie(titulo2, ano2, genero_associado, preco2, temporadas,
                             duracaoEps, qntEps)
              series.append(serie1)
              print('')
              print('A série foi cadastrada com sucesso!')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
            else:
              print("Genêro não encontrado.")
              print('Série NÃO cadastrada.')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')

          except ValueError:
            print('')
            print('Você digitou algo errado.')
            input('Tecle ENTER para voltar e tentar novamente.')

############################################## Cadastrar Diretor

        elif quest == '3':
          print('========================')
          print('DIRETORES JÁ CADASTRADOS')
          print('========================')
          for d in diretores:
            print(f'- {d.getNome()}')
          print('========================')
          print('')
          try:
            nome = input('Nome do diretor: ').upper()
            idade = int(input('Idade: '))
            nacionalidade = input('Nacionalidade: ').upper()
            diretor1 = Diretor(nome, idade, nacionalidade)
            diretores.append(diretor1)
            print('')
            print('O Diretor foi cadastrado com sucesso!')
            cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
            input('')
          except ValueError:
            print('')
            print('Você digitou algo errado.')
            input('Tecle ENTER para voltar e tentar novamente.')

############################################## Cadastrar Genero

        elif quest == '4':
          print('========================')
          print(' GENÊROS JÁ CADASTRADOS')
          print('========================')
          for g in generos:
            print(f'- {g.getName()}')
          print('========================')
          print('')
          name = input('Genêro: ').upper()
          info = input('Informações do genêro: ').upper()
          genero1 = Genero(name, info)
          generos.append(genero1)
          print('')
          print('O Genêro foi cadastrado com sucesso!')
          cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
          input('')

############################################## Sair do modo operador

        elif quest == '5':
          print('')
          print('Saiu do modo operador.')
          print('')

############################################## Erro Comando Inválido

        else:
          print('')
          print('Comando Inválido! digite de 1 a 5 para a opção desejada.')
          cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
          input('')

############################################## Login incorreto

    else:
      print('')
      print('Login incorreto!')
      print('')
      dica_operador = '***obs: O usuário correto é "operador01" e a senha é "senha123"'
      cprint('\033[1m\033[3m' + dica_operador, 'white', 'on_grey')
      print('')
      cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
      input('')

######################################################################
######################################################################
######################################################################
############################################ Modo Convidado

  elif login == '2':
    print('')
    convidado_user = input('Digite o usuário: ')
    convidado_senha = input('Digite sua senha: ')
    print('')

    print('Logado com sucesso.')
    print(f'Bem vindo {convidado_user}!')

    quest2 = 'n'
    while quest2 != '7':
      print('')
      print('======================')
      print('=======CONVIDADO======')
      print('======================')
      print('1) Pesquisar Filme')
      print('2) Pesquisar Série')
      print('----------------------')
      print('3) Pesquisar Diretor')
      print('4) Pesquisar Genêro')
      print('----------------------')
      print('5) Ver Carteira')
      print('6) Ver Aluguéis')
      print('----------------------')
      print('7) Sair do modo usuário')
      print('======================')

      print('')
      mensagem = '***obs: Já existem alguns, genêros, diretores, filmes e séries pré-cadastrados. Porém se você deseja adicionar mais algum, basta cadastra-lo.'
      cprint('\033[1m\033[3m' + mensagem, 'white', 'on_grey')
      print('')
      
      quest2 = input('O que deseja fazer? ')

################################################## Pesquisa
############################################## Pesquisar Filme

      if quest2 == '1':
        print('========================')
        print('      LISTA FILMES      ')
        print('========================')
        for i in filmes:
          print(f'- {i.getTitulo()}')
        print('========================')

        escolhe_filme = input(
            'Qual filme deseja saber informações? (digite o titulo) ').upper()
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
          print(f'Genero: {filme_escolhido.genero.getName()}')
          print(f'Diretor: {filme_escolhido.diretor.getNome()}')
          print(
              f'Duração total: {filme_escolhido.calculaDuracaoTotal()} Minutos'
          )
          print(f'Preço aluguel do filme: $ {filme_escolhido.getPreco():.2f}')
          print('')
          
          ################### Alugar série
          aluguel = input('Deseja alugar o filme? (s/n) ')
          if aluguel == 's':
            if (filme_escolhido.getPreco()) <= (convidado1.getCreditos()):
              alugueis.append(filme_escolhido)
              print('')
              print('Filme alugado com sucesso!')
              print(f'Valor atual em sua carteira: $ {convidado1.calculaCreditos(filme_escolhido):.2f}')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
            else:
              print('')
              print('Você não tem créditos suficientes para alugar esse filme!')
              print('Para colocar mais créditos, acesse a opção 5) Ver Carteira.')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
          ###########################
        
        else:
          print("Filme não encontrado.")
          cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
          input('')

############################################## Pesquisar Serie

      elif quest2 == '2':
        print('========================')
        print('      LISTA SÉRIES      ')
        print('========================')
        for s in series:
          print(f'- {s.getTitulo()}')
        print('========================')

        escolhe_serie = input(
            'Qual série você deseja saber informações? ').upper()
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
          print(f'Genero: {serie_escolhida.genero.getName()}')
          print(
              f'Duração total: {serie_escolhida.calculaDuracaoTotal()} Minutos'
          )
          print(f'Preço aluguel da série: $ {serie_escolhida.getPreco():.2f}')
          print('')
          
          ################ Alugar Série
          aluguel2 = input('Deseja alugar a série? (s/n) ')
          if aluguel2 == 's':
            if (serie_escolhida.getPreco()) <= (convidado1.getCreditos()):
              alugueis.append(serie_escolhida)
              print('')
              print('Série alugada com sucesso!')
              print(f'Valor atual em sua carteira: $ {convidado1.calculaCreditos(serie_escolhida):.2f}')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
            else:
              print('')
              print('Você não tem créditos suficientes para alugar essa série!')
              print('Para colocar mais créditos, acesse a opção 5) Ver Carteira.')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
          #########################
        
        else:
          print("Série não encontrada.")
          cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
          input('')

############################################## Pesquisar Diretor

      elif quest2 == '3':
        print('========================')
        print('        DIRETORES       ')
        print('========================')
        for d in diretores:
          print(f'- {d.getNome()}')
        print('========================')

        escolhe_diretor = input(
            'Digite o nome do diretor que deseja saber detalhes: ').upper()
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
          
          ######## Projetos do diretor #######
          projetos_diretor = [
              projeto.getTitulo() for projeto in filmes
              if isinstance(projeto, Filme)
              and projeto.getDiretor() == diretor_escolhido
          ]
          if projetos_diretor:
            print('=======================')
            print('       PROJETOS ')
            print('=======================')
            for projeto in projetos_diretor:
              print(f'- {projeto}')
            print('=======================')
            cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
            input('')
          else:
            print('Nenhum projeto associado a este diretor encontrado.')
            cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
            input('')
          ################################
        
        else:
          print("Diretor não encontrado.")
          cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
          input('')

############################################## Pesquisar Genero

      elif quest2 == '4':
        print('======================')
        print('        GENÊROS  ')
        print('======================')
        for g in generos:
          print(f'- {g.getName()}')
        print('======================')

        escolhe_genero = input(
            'Digite o nome do genêro que deseja saber detalhes: ').upper()
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
          
          ###### Projetos do genêro ########
          projetos_genero = [
              projeto.getTitulo()
              for projeto in filmes if projeto.getGenero() == genero_escolhido
          ] + [
              projeto.getTitulo()
              for projeto in series if projeto.getGenero() == genero_escolhido
          ]
          if projetos_genero:
            print('=======================')
            print('        PROJETOS       ')
            print('=======================')
            for projeto in projetos_genero:
              print(f'- {projeto}')
            print('=======================')
            cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
            input('')
          else:
            print('Nenhum projeto associado a este gênero encontrado.')
            cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
            input('')
          ###################################
        
        else:
          print("Genero não encontrado.")
          cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
          input('')

############################################## Ver Carteira

      elif quest2 == '5':
        print(f'Valor atual em sua carteira: $ {convidado1.getCreditos():.2f}')
        print('')
        add_money = input('Deseja adicionar mais dinheiro? (s/n) ')
        if add_money == 's':
          print('')
          try:
            money = float(input('Quanto dinheiro deseja adicionar? $ '))
            print('')
            verifica_senha = input('***Digite a senha do login para aprovar a transação: ')
            if verifica_senha == convidado_senha:
              convidado1.maisCreditos(money)
              print('')
              print('-----------------------------------------')
              print(f'Você adicionou $ {money:.2f} na sua carteira!')
              print(f'O valor atual em sua carteira é de $ {convidado1.getCreditos():.2f}')
              print('')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
            else:
              print('')
              print('Senha incorreta!')
              print('')
              cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
              input('')
          except ValueError:
            print('')
            print('Você digitou algo errado.')
            print('É importante notar que você deve escrever valores decimais com PONTO e não VIRGULA.')
            print('')
            input('Tecle ENTER para voltar e tentar novamente.')
  
############################################## Alugueis

      elif quest2 == '6':
        print('========================')
        print('        ALUGUÉIS        ')
        print('========================')
        for a in alugueis:
          print(f'- {a.getTitulo()}')
        print('========================')
        cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
        input('')

############################################## Fim programa

      elif quest2 == '7':
        print('Saiu do modo convidado!')
        print('')

############################################## Erro Comando Inválido

      else:
        print('')
        print('Comando Inválido! digite de 1 a 7 para a opção desejada.')
        cprint('\033[1m\033[3m' + msg_continuar, 'white', 'on_grey')
        input('')

############################################## Fim programa total

  elif login == '3':
    print('')
    print('''
⣶⡄⠀⣶⠀⢰⣶⣶⡆⠠⣶⣶⣶⡆⢰⣶⣶⣦⠀⣶⠀⠀⠀⣶⡆⠐⣶⠀⣰⡖
⣿⣷⡀⣿⠀⣸⣇⣀⡀⠀⠀⣿⠀⠀⢸⣇⣀⡀⠀⣿⠀⠀⠀⣿⡇⠀⠹⣷⡿⠁
⣿⡿⣷⣿⠀⣿⡟⠛⠁⠀⠀⣿⠀⠀⢸⡏⠉⠁⠀⣿⠀⠀⠀⣿⡇⠀⢠⣿⣇⠀
⣿⡇⢻⣿⠀⣿⣷⣶⡆⠀⠀⠿⠀⠀⠸⠇⠀⠀⠀⣿⣶⣶⠀⣿⡇⢀⣿⠋⢿⡆
⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
    ''')
    print('')
    print('Obrigado por utilizar.')
    print('Programa Encerrado!')
