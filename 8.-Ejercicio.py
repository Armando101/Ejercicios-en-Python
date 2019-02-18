"""
Hacer un programa que pida al usuario un
nombre y una contraseña. Después de esto el
programa le pedirá al usuario de nuevo su
contraseña, si la contraseña es la correcta,
imprimirá “Bienvenido ‘Nombre de Usuario’”
donde ‘Nombre de Usuario’ es el nombre que se
ingresó, si la contraseña no es la correcta,
imprimirá “INCORRECTO”.
"""

import os

print("Bienvenido")
nombre = input("Dame un nombre de usuario ")
password = input("Dame tu password ")

os.system("clear")

while True:
	os.system("clear")
	nom = input("Coloque su nombre de usuario ")
	passw = input("Coloque su password ")

	if nom == nombre and password == passw:
		print("Usted ha ingresado correctamente")
		break
	else:
		print("Nombre de usuario o password incorrecto")
		print("Desea intentarlo de nuevo")
		print("1) Si")
		print("2) No")
		op = input()
		if op == "2":
			break