def numero_step(numero):
    numero_string = str(numero)
    for i in range(len(numero_string) - 1):
        diferencia = abs(int(numero_string[i]) - int(numero_string[i+1]))
        if diferencia != 1:
            return False
    return True
print(numero_step(123234))
print(numero_step(943733837))