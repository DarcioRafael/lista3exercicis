# exercicio = int(input(' digite qual exercicio a execukltar: 1 ou 2 '))

# if exercicio == 1:

#     nome = input(' digite o seu nome ')
#     sobrenome = input(' digite o sobrenome ')
#     idade = input(' digite a idade ')

#     listaA = [ nome, sobrenome, idade]
#     print(listaA[0], listaA[1],', idade', listaA[2], 'anos')

# elif exercicio == 2:

#     mes =int(input(' digite um més de 1 a 12 '))
#     mes=mes-1
#     listaA= [ 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro ']
#     print (' o més é :',listaA[mes])
# else:
#     print(' digito invalido')

# class Usuario1 ():
#     def _init_(self, nome, sobrenome, idade ):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade

# usuario = Usuario1(input(' digite o mome: '), input(' digite o sobre nome: '), int(input(' digite a idade: ')))

# print(' O USUARIO:' ,usuario.nome, usuario.sobrenome, usuario.idade )

# class Vendedor:
#     def __init__ ( self, nome, nome2):
#         self.nome = nome
#         self.nome2 = nome2

        
#     def informacaoSaida(self):
#         print(f' ola meu nome do Sr ',self.nome, self.nome2,)

#     def informacaoSaida1(self):
#         print(f' ola meu nome do Sra ',self.nome, self.nome2,)


# vendedor1 = Vendedor(input('nome 1 '), input(' sobrenome 1 '))
# vendedor2 = Vendedor(input('nome 2 '), input(' sobrenome 2 '))



# vendedor1.informacaoSaida()
# vendedor2.informacaoSaida1()

# class Pessoa :
#     def __init__ (self, nome, sobrenome, idade, cidade ):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
#         self.cidade = cidade
    
#     def saida(self):
#         print(f' Meu nome é: ' ,self.nome, self.sobrenome, 'Tenho ' ,self.idade,'anos e moro em/no' ,self.cidade )
    
# pessoa1 = Pessoa(input(' qual seu nome? '), input(' qual seu sobre nome '), input(' qual sua idade? '),input(' onde vc mora? '))
# pessoa2 = Pessoa(input(' qual seu nome? '), input(' qual seu sobre nome '), input(' qual sua idade? '),input(' onde vc mora? '))
# pessoa3 = Pessoa(input(' qual seu nome? '), input(' qual seu sobre nome '), input(' qual sua idade? '),input(' onde vc mora? '))

# pessoa1.saida()
# pessoa2.saida()
# pessoa3.saida()

# exercicio 1
#criar uma classe carro, atribultos marca ano, cor

# class Carro:
#     def __init__(self, marca, modelo, ano, cor, ):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.cor = cor
        
#     def caracter_veiculo(self):
#         print(f' Veiculo,' ,self.marca, self.modelo, 'ano', self.ano, ',  cor', self.cor, 'foi roubado !!! ')
# carro1 = Carro(input(' Qual a marca? '), input(' Qual o modelo? '), input(' Qual o ano? '), input(' Qual a cor? '))
# carro1.caracter_veiculo()

# #EXERCICO 2

# class Pessoa:
#     def __init__(self, nome, sobre_nome, cpf, cidade, estado):
#         self.nome = nome
#         self.sobre_nome = sobre_nome
#         self.cpf = cpf
#         self. cidade = cidade
#         self.estado = estado
#     def aluno(self):
#         print(f' O aluno(a)', self.nome, self.sobre_nome, ', cpf ', self.cpf, 'da cidade de ', self.cidade, '-', self.estado,', foi aprovado no exame do ENEM ')

# aluno1 = Pessoa(input(' Nome do Aluno: '), input('Sobre Nome: '), input (' cpf: '), input(' Cidade: '), input(' Estado: ') )
# aluno1.aluno()

# exercicio 3


# class contaBancaria:

#        def _init_(self, nome, conta, saldo):
#            self.nome = nome
#            self.conta = conta
#            self.saldo = float(saldo)

#        def deposito(self):
#            self.saldo = 1000 + self.saldo


#        def bancaria(self):
#            print(f'\nnome do usuário {self.nome}')
#            print(f'conta bancária {self.conta}')
#            print(f'saldo em conta {self.saldo}')



# conta_1 = contaBancaria(input('Nome do titular da conta: '), input('numero conta corrente: '), input('valor deposito: '))
# conta_1.deposito()
# conta_1.bancaria()


    
               

