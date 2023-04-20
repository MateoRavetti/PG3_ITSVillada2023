while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("Error: Ingrese un numero.")
    finally:
        respuesta = input("¿Desea seguir esperando? (S/N): ")
        if respuesta.upper() != "S":
            break
