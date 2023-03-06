import sys

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    elif n < 0:
        return "No existe el factorial de números negativos."
    elif n == 0:
        return 1

if __name__ == '__main__':
        n = int(input("Ingrese un número para hallar su factorial: "))
        print("El factorial de ",n," es: ",factorial(n))