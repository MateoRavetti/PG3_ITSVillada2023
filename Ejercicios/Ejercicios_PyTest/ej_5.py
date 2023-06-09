def search_matrix(matrix, target):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Inicializar los índices para la búsqueda
    row = 0
    col = cols - 1

    # Realizar la búsqueda desde la esquina superior derecha
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target = 9

if search_matrix(matrix, target):
    print("El número", target, "está presente en la matriz.")
else:
    print("El número", target, "no está presente en la matriz.")
