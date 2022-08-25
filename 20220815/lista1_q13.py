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


def somatorioAteN(n):
    s = 0
    i = 1
    while(i <= n):
        s += (1/i)
        i += 1
    return s


def main():
    n = lerNumero()
    print("S = %.2f" % (somatorioAteN(n)))


if __name__ == "__main__":
    main()
