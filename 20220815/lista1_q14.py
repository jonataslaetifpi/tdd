def lerNumero():
    while True:
        try:
            num = int(input('Digite o valor inteiro e positivo: '))
            if (num < 0):
                print('Número inválido. Tente novamente.')
                lerNumero()
            return num
        except:
            print('Número inválido. Tente novamente.')


def f(n, memoria):
    if (n < 2):
        return 1
    elif (n == 2):
        return 2
    elif (memoria[n] == 0):
        memoria[n] = n * f(n-1, memoria)
    return memoria[n]


def fatorial(n):
    memoria = [0] * (n+1)
    return f(n, memoria)


def somatorioAteN(n):
    s = 1
    i = 1
    while(i <= n):
        s += (1/(fatorial(i)))
        i += 1
    return s


def main():
    n = lerNumero()
    print("S = %.2f" % (somatorioAteN(n)))


if __name__ == "__main__":
    main()
