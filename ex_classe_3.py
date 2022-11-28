"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, ladoa, ladob):
        self.__ladoa = ladoa
        self.__ladob = ladob

    def muda_valor_dos_lados(self, nladoa, nladob):
        self.__ladoa = nladoa
        self.__ladob = nladob

    def retorna_valor_dos_lados(self):
        print(f'Valor do lado A: {self.__ladoa}')
        print(f'Valor do lado B: {self.__ladob}')

    def calcular_area(self):
        a = self.__ladoa * self.__ladob
        return a

    def calcular_perimetro(self):
        perimetro = 2 * self.__ladoa + 2 * self.__ladob
        return perimetro


print('Bem vindo!')

x = float(input('Digit o valor do lado A:'))
y = float(input('Digite o valor do lado B'))

r1 = Retangulo(x, y)

print(
    f'Serão necessários {r1.calcular_area()} m quadrado(s) de piso e {r1.calcular_perimetro()}m de rodapés para suprir o local')
