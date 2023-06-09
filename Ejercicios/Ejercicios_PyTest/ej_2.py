def roman_to_decimal(roman_number):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    decimal_number = 0
    previous_value = 0
    
    for char in reversed(roman_number):
        value = roman_values[char]
        
        if value >= previous_value:
            decimal_number += value
        else:
            decimal_number -= value
        
        previous_value = value
    
    return decimal_number
print(roman_to_decimal("III"))  # 3
print(roman_to_decimal("IV"))  # 4
print(roman_to_decimal("IX"))  # 9
print(roman_to_decimal("LVIII"))  # 58
print(roman_to_decimal("MCMXCIV"))  # 1994
