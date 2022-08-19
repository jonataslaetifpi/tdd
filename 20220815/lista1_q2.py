from typing import Final

pi: Final[float] = 3.14159265359


def lerRaio():
    while True:
        try:
            num = float(input('Digite o valor do raio: '))
            return num
        except:
            print('Valor inválido. Tente novamente.')


def areaCirculo(r):
    return pi * r ** 2


def perimetroCirculo(r):
    return 2*pi*r


def main():
    raio = lerRaio()
    print('Área do círculo = %.2f' % (areaCirculo(raio)))
    print('Perímetro do círculo = %.2f' % (perimetroCirculo(raio)))


if __name__ == "__main__":
    main()
