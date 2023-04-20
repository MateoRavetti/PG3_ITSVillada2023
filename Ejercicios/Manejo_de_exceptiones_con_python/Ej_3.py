meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    num_mes = int(input("Ingrese el número de mes (1-12): "))
    mes = meses[num_mes - 1]
    print(f"El mes correspondiente al número {num_mes} es {mes}")
except IndexError:
    print("Error: número de mes inexistente.")