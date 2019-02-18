"""
Realizar un programa que imprima la serie de
fibonacci hasta el elemento n que especifique
el usuario.
"""

num = int(input("Ingrese un numero "))

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(num)