def lerNumero():
    while True:
        try:
            num = int(input('Digite o valor inteiro: '))
            return num
        except:
            print('Número inválido. Tente novamente.')


def isPar(n):
    return n % 2 == 0


def mensagemParOuImpar(n):
    if (isPar(n)):
        return 'Verdadeiro, pois '+str(n)+' é par.'
    else:
        return 'Falso, pois '+str(n)+' é ímpar.'


def main():
    numero = lerNumero()
    print(mensagemParOuImpar(numero))


if __name__ == "__main__":
    main()
