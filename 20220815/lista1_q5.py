def pesoIdealParaHomem(h):
    return (72.7 * h) - 58.0


def pesoIdealParaMulher(h):
    return (62.1 * h) - 44.7


def pesoIdeal(a, s):
    if (s == 1):
        return pesoIdealParaMulher(a)
    return pesoIdealParaHomem(a)


def lerAltura():
    while True:
        try:
            altura = float(input('Digite sua altura: '))
            return altura
        except:
            print('Altura inválida. Tente novamente.')


def lerSexo():
    while True:
        try:
            sexo = int(
                input('Digite seu sexo [1 - Feminino; 2 - Masculino]: '))
            if (sexo != 1 and sexo != 2):
                print('Sexo inválido. Tente novamente.')
                lerSexo()
            return sexo
        except:
            print('Sexo inválido. Tente novamente.')


def main():
    altura = lerAltura()
    sexo = lerSexo()
    print('Seu peso ideal é: ' + str(pesoIdeal(altura, sexo)) + ' kg.')


if __name__ == "__main__":
    main()
