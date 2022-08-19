def lerNumero(iesimo):
    while True:
        try:
            numero = float(input('Digite o ' + iesimo +
                                 ' número inteiro: '))
            return numero
        except:
            print('Número inválido. Tente novamente.')


def maior(n1, n2):
    if (n1 > n2):
        return n1
    return n2


def menor(n1, n2):
    if (n1 < n2):
        return n1
    return n2


def somaTudoEntreDoisNumeros(n1, n2):
    a1 = menor(n1, n2)
    an = maior(n1, n2)
    return (a1+an)*((an-(a1)+1)/2)


def main():
    n1 = lerNumero('primeiro')
    n2 = lerNumero('segundo')
    print('A soma de todo o intervalo [%d, %d] é: %d' % (
        menor(n1, n2), maior(n1, n2), somaTudoEntreDoisNumeros(n1, n2)))


if __name__ == "__main__":
    main()
