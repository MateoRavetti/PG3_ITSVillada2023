def palindromo(palabra):
    return palabra == palabra[::-1]
print(palindromo("neuquen"))
print(palindromo("muchachos"))