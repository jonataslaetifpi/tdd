'''2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''

def isPositivo(n):
    return n >= 0

def somaPositivos(lista):
    s = 0
    for n in lista:
        if (isPositivo(n)): s += n
    return s

def quantidadeNegativos(lista):
    q = 0
    for n in lista:
        if (n < 0): q += 1
    return q


def main():
    numeros = [-1, 2, 3, -4, -5, 6, 7, 8, 9, 10]
    print('Quantidade de números negativos: %d' %(quantidadeNegativos(numeros)))
    print('Soma dos números positivos: %d' %(somaPositivos(numeros)))


if __name__ == "__main__":
    main()
