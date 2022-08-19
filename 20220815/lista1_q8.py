def lerNumero():
    while True:
        try:
            numero = float(input('Digite o número: '))
            desejaContinuar = lerCaractere().upper()
            if (desejaContinuar != 'N'):
                lerNumero()
            return numero
        except:
            print('Número inválido. Tente novamente.')


def lerCaractere():
    while True:
        try:
            caractere = input('Desejar continuar [S - sim; N - não]: ').upper()
            if (caractere != 'S' and caractere != 'N'):
                print('Caractere inválido. Tente novamente.')
                lerCaractere()
            return caractere
        except:
            print('Caractere inválido. Tente novamente.')


def main():
    numero = lerNumero()
    print("O cubo do número %.2f é: %.2f" % (numero,  numero**3))


if __name__ == "__main__":
    main()
