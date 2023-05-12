"""System module."""

import math

def is_prime(num):
    if num == 1 or num == 0: # Estos primeros numeros no son primos
        return False
    elif num == 2: # El primer numero primo
        return True
    elif num > 2:
        for i in range(2, int(1 + math.sqrt(num))):
            if num % i == 0: # si num es divisible por i, devuelve False
                return False
        return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()