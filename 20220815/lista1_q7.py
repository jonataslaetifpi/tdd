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


def main():
    numero = lerNumero()
    print('%d! = %d' % (numero, fatorial(numero)))


if __name__ == "__main__":
    main()
