"""
Realizar un menú de una calculadora en el que las
opciones van a ser:
1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números
5. Potencia de un número
6. Raíz de un número
7. Salir
"""
import os

while True:
	print("Bienvenido a la calculadora chida")
	print("1. Sumar dos números\n2. Restar dos números\n3. Multiplicar dos números\n4. Dividir dos números\n5. Potencia de un número\n6. Raíz de un número\n7. Salir")

	op = int(input("Ingrese la operacion que desea realizar "))
	os.system('clear')
	if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
		num1=int(input("Ingrese el primer numero "))
		num2=int(input("Ingrese el segundo numero "))
		if op == 1:
			print(num1 + num2)
		elif op == 2:
			print(num1 - num2)
		elif op == 3:
			print(num1 * num2)
		elif op == 4:
			if num2 == 0:
				print("No es posible dividir entre cero")
			else:
				print(num1/num2)
		else:
			print(num1**num2)
	elif op == 6:
		num = int(input("Ingrese su numero "))
		print(num**0.5)
	elif op == 7:
		break
	else:
		print("Opcion invalida")
os.system('clear')
print("GoodBye")