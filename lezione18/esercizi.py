#ESERCIZIO 1
'''
import math

def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError as error:
        print(f"Il valore inserito è negativo: {number}")
        return -1


number = 16
print(safe_sqrt(number))
'''
#ESERCIZIO 2
'''
import string
import collections as ct
special_chars = string.punctuation
def validate_password(password):
    if len(password) >= 20:
        pass
    else:
        raise ValueError("La password deve avere almeno 20 caratteri")
    
    if sum([1 if c.isupper() else 0 for c in password]) >= 3:
        pass
    else:
        raise ValueError("La password deve contenere almeno 3 caratteri maiuscoli") 
    
    if sum([v for k,v in ct.Counter(password).items() if k in special_chars]) >= 3:
        print("Password corretta")
    else: 
        raise ValueError("La password deve contenere almeno tre caratteri speciali")
    
password = "PasswordGiustaNonMeRompe&%&"
print(validate_password(password))
'''
#ESERCIZIO 3



        


