from math import floor, sqrt


def lerNumero():
    while True:
        try:
            numero = int(input('Digite o número inteiro: '))
            return numero
        except:
            print('Número inválido. Tente novamente.')


def quantidadeDivisores(num):
    r = int(floor(sqrt(num))) + 1
    c = 2
    i = 2
    while(i < r):
        if (num % i == 0):
            c += (1 if (num/i == i) else 2)
        i += 1
    return c


def main():
    n = lerNumero()
    print('O número %d possui %d divisores inteiros positivos.' %
          (n, quantidadeDivisores(n)))


if __name__ == "__main__":
    main()
