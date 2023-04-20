try:
    with open("prueba.txt", "w") as archivo:
        frase = input('Ingrese una frase: ')
        archivo.write(frase)
except TypeError:
    print("Error: se intentó escribir un valor que no es un string en el archivo.")