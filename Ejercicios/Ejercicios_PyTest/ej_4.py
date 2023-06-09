import math

def calculate_statistics(numbers):
    n = len(numbers)

   
    mean = sum(numbers) / n

   
    sum_of_squared_diff = sum((x - mean) ** 2 for x in numbers)

    
    std_deviation = math.sqrt(sum_of_squared_diff / n)

    return mean, std_deviation
numbers = [2, 4, 6, 8, 10]
mean, std_deviation = calculate_statistics(numbers)
print("Media:", mean)
print("Desviación estándar:", std_deviation)

