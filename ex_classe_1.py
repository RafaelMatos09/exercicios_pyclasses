"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

"""


class Bola:

    def __init__(self, cor, circuferencia, material):
        self.__cor = cor
        self.__circuferencia = circuferencia
        self.__material = material

    def troca_cor(self, ncor):
        self.__cor = ncor

    def mostra_cor(self):
        print(f'A cor é {self.__cor}')

    def mostra_bola(self):
        print(
            f'Cor da bola é {self.__cor} com circuferencia de {self.__circuferencia} cm e material de {self.__material}.')


b1 = Bola('amarela', 33, 'couro')
b1.troca_cor('verde')
b1.mostra_cor()
b1.troca_cor('vermelho')
b1.mostra_cor()
b1.mostra_bola()
