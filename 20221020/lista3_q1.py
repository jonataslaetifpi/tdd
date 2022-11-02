def volume_esfera(raio):
    pi = 3.14159265359
    if raio <= 0:
        return Exception

    return (4/3)*pi*(raio**3)

