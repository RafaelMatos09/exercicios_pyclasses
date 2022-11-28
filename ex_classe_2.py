"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""


class Quadrado():
    def __init__(self, tamanho_do_lado):
        self.__tamanho_do_lado = tamanho_do_lado

    def muda_valor_do_lado(self, n_lado):
        self.__tamanho_do_lado = n_lado

    def retorna_valor_do_lado(self):
        print(f'Valor do lado é {self.__tamanho_do_lado}')

    def calcular_area(self):
        calc = self.__tamanho_do_lado ** 2
        print(f'Area do quadrado é {calc}')


b1 = Quadrado(2)
b1.muda_valor_do_lado(4)
b1.retorna_valor_do_lado()
b1.calcular_area()
