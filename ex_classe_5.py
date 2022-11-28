"""
Classe Conta Corrente: Crie uma classe para implementar 
uma conta corrente. A classe deve possuir os seguintes 
atributos: número da conta, nome do correntista e saldo. Os métodos 
são os seguintes: alterarNome, depósito e saque; No 
construtor, saldo é opcional, com valor 
default zero e os demais atributos são obrigatórios.

"""


class ContaCorrente:

    contador = 999

    def __init__(self, nome, saldo=0):
        self.__numero = ContaCorrente.contador + 1
        self.__nome = nome
        self.__saldo = saldo

    def altera_nome(self, novo_nome):
        self.__nome = novo_nome
        print(f'O nome da conta agora é {self.__nome}')

    def deposito(self, valor_deposito):
        self.__saldo += valor_deposito
        print(
            f'Você fez o deposito no valor de R${valor_deposito} reais seu saldo agora é de R${self.__saldo} reais.')

    def saque(self, valor_saque):
        self.__saldo -= valor_saque
        print(
            f'Saque efetuado no valor de R${valor_saque} reais saldo de R${self.__saldo} reais.')


cc1 = ContaCorrente('Rafael')
cc1.altera_nome('Rodolfo')
cc1.deposito(50.00)
cc1.saque(30.00)
cc1.deposito(300.00)
