"""
Programa que permite calcular el factorial de
un número n siendo n un número natural
ingresado por el usuario.
"""

n=int(input("Ingresa el numero del cual deseas obtener el factorial "))

def factorial(n):
	if (n == 0 or n==1):
		return 1
	else:
		return factorial(n-1) * n

fac = factorial(n)
print("El factorial es: ", fac)