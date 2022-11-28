"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a 
idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self, idade_prevista):
        self.__idade += idade_prevista
        print(f'Você agora tem {self.__idade} anos.')
        print(f'Envelheceu {idade_prevista} anos.')

    def engordar(self, peso_engordar):
        self.__peso += peso_engordar
        print(f'Você agora tem {self.__peso} kilos.')
        print(f'Engordou {peso_engordar} kilos.')

    def emagrecer(self, peso_emagrecer):
        self.__peso -= peso_emagrecer
        print(f'Você agora tem {self.__peso} kilos.')
        print(f'Emagreceu {peso_emagrecer} kilos.')

    def crescer(self, idade_prevista):
        if self.__idade < 21:
            self.__altura += 0.05 * idade_prevista
            print(f'Sua altura agora é {self.__altura}m.')
            print(f'Você cresceu {0.05 * idade_prevista}m.')


p1 = Pessoa('Rafael', 15, 80, 1.60)
p1.crescer(5)
p1.envelhecer(10)
p1.engordar(15)
p1.emagrecer(5)
