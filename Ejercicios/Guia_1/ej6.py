def vocales(palabra):
    vocales = "AEIOUaeiou"
    cantidad_vocales = 0
    for letra in palabra:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales
print(vocales("TALLERES"))