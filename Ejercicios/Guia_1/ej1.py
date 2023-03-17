def busqueda_valor(lista, valor):
    try:
        indice = lista.index(valor)
        return indice
    except ValueError:
        return "---------."
mi_lista = [91, 199, 999, 455]
valor_buscado = 455

print(busqueda_valor(mi_lista, valor_buscado))