from math import sqrt


def lerNumeroDeLados():
    while True:
        try:
            lados = float(input('Digite o número de lados do polígono: '))
            return lados
        except:
            print('Quantidade inválido. Tente novamente.')


def lerMedidaLadoEmCentimetros():
    while True:
        try:
            medida = float(input('Digite a medida do lado em centímetros: '))
            return medida
        except:
            print('Medida inválida. Tente novamente.')


def perimetroTriangulo(lado):
    return lado*3


def areaTrianguloEquilatero(lado):
    p = (3*lado)/2
    return sqrt(p*((p-lado)**3))


def areaPentagonoRegular(lado):
    return areaTrianguloEquilatero(lado) * 5


def areaQuadrado(lado):
    return lado*lado


def identificaPoligono(nLados, medidaCadaLado):
    if (nLados == 3):
        print('TRIÂNGULO')
        print('Perímetro = %.2f' % (perimetroTriangulo(medidaCadaLado)))
    elif(nLados == 4):
        print('QUADRADO')
        print('Área = %.2f' % (areaQuadrado(medidaCadaLado)))
    elif(nLados == 5):
        print('PENTÁGONO')
        print('Área = %.2f' % (areaPentagonoRegular(medidaCadaLado)))


def main():
    nLados = lerNumeroDeLados()
    medidaCadaLado = lerMedidaLadoEmCentimetros()
    identificaPoligono(nLados, medidaCadaLado)


if __name__ == "__main__":
    main()
