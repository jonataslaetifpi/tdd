from typing import Final

media_minima: Final[float] = 6.00


def lerNota(ordemDaNota):
    while True:
        try:
            nota = float(input('Digite a '+ordemDaNota+' nota: '))
            return nota
        except:
            print('Nota inválida. Tente novamente.')


def resultado(nota1, nota2):
    m = (nota1+nota2)/2.0
    if (m >= media_minima):
        print('PARABÉNS! Você foi aprovado!')


def main():
    nota1 = lerNota('primeira')
    nota2 = lerNota('segunda')
    resultado(nota1, nota2)


if __name__ == "__main__":
    main()
