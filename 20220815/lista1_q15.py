def ler(h):
    return (72.7 * h) - 58.0


def lerNumero():
    while True:
        try:
            num = int(input('Digite o valor inteiro e positivo: '))
            if (num < 0):
                print('Número inválido. Tente novamente.')
                lerNumero()
            return num
        except:
            print()


def fatorial(n, memoria):
    if (n < 2):
        return 1
    elif (n == 2):
        return 2
    elif (memoria[n] == 0):
        memoria[n] = n * fatorial(n-1, memoria)
    return memoria[n]


def somatorioAteN(n):
    s = 1
    i = 1
    memoria = [0] * (n+1)
    while(i < n):
        s += 1/((fatorial(i, memoria)))
        memoria = [0] * (i+1)
        i += 1
    return s


def main():
    n = lerNumero()
    print("S = %.2f" % (somatorioAteN(n)))


if __name__ == "__main__":
    main()
