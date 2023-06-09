import re

def validate_password(password):
    if len(password) < 8:
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True
print(validate_password("Abcdefg1"))  # True
print(validate_password("password"))  # False (no contiene una letra mayúscula)
print(validate_password("12345678"))  # False (no contiene una letra minúscula)
print(validate_password("Abcdefg!"))  # False (contiene un carácter especial)
