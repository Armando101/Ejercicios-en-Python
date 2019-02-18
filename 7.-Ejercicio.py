"""
Realizar un menú que contenga las siguientes:
1. Saludar
2. Decir Algo
3. Despedirse
Cuando se selecciones despedir, se tiene que
imprimir
una
despedida
y
terminar
el
programa.
"""
import os

while True:
	print("")
	print("Ingresa tu opcion ")
	print("1) Saludar ")
	print("2) Decir Algo ")
	print("3) Despedirse ")

	op = int(input())
	os.system("clear")

	if op == 1:
		print("Hola como estas? Esto es un saludo")
	elif op == 2:
		print("Estoy diciendo algo")
	elif op == 3:
		break
	else:
		print("Opcion invalida, vuelve a intentarlo")

print("GoodBye")