"""
Classe TV: Faça um programa que simule um televisor criando-o 
como um objeto. O usuário deve ser capaz de informar o número 
do canal e aumentar ou diminuir o volume. Certifique-se de que 
o número do canal e o nível do volume permanecem dentro de 
faixas válidas.
"""


class Tv:
    def __init__(self, volume, canal=10):
        self.__canal = canal
        self.__volume = volume

    def trocar_canal(self, x):
        canal = [10, 20, 30, 40, 50]
        if x in canal:
            self.__canal = x
            print(f'Você está no canal {self.__canal}')
        else:
            print(f'Canal não programado.')

    def aumentar_volume(self, x):
        volume = [1, 2, 3, 4, 5]
        if x in volume:
            self.__volume = x
            print(f'O volume foi programado para {self.__volume}')
        else:
            print('Canal não programado.')

    def diminuir_volume(self, x):
        volume = [1, 2, 3, 4, 5]
        if x in volume:
            self.__volume = x
            print(f'O volume foi programado para {self.__volume}')
        else:
            print('Canal não programado.')


t = Tv(5)
t.trocar_canal(20)
t.aumentar_volume(5)
t.diminuir_volume(1)
