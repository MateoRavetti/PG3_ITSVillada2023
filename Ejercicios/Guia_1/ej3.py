ancho = int(input("Ancho: "))
alto = int(input("Alto: "))
caracter = input("Caracter: ")

for i in range(alto):
    for j in range(ancho):
        print(caracter, end=" ")
    print()