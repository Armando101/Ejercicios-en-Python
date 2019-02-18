"""
Realizar un programa en el que se le pida al
usuario dos números del 1 al 9, num1 y num2.
Después va a imprimir todos los números
naturales del 1 al 100, sin embargo, cuando
un número sea múltiplo de num1 o num2 o
contenga
alguno
de
estos
números,va
a
imprimir ‘clap’.
"""

num1 = int(input("Ingrese un numero del uno al nueve "))
num2 = int(input("Ingrese otro numero del uno al nueve "))

for x in range(100):
	if x%num1 == 0 or x%num2 == 0:
		print("clap")
	else:
		print(x)