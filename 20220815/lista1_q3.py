def temperaturaDeFahrenheitParaCelsius(f):
    return ((f - 32.0)*5.0)/9.0
    
def main():
    f = float(input('Digite a temperatura em graus Fahrenheit: '))
    print('Essa temperatura equivale a '+ str(temperaturaDeFahrenheitParaCelsius(f))+' graus celsius.')

if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except:
            print('Temperatura inválida')