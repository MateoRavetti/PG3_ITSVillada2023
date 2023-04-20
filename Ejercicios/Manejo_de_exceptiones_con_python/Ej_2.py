try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división de {num1} entre {num2} es {resultado}")
except ZeroDivisionError:
    print("Error: no esta  dividir entre cero.")