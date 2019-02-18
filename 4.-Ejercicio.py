"""
Programa que permite determinar si en una
cadena de texto se encuentra determinado
carácter. Tanto la cadena como el carácter
deben ser ingresados por el usuario.
Pd: No se puede usar in
"""

cadena = input("Ingrese un cadena ")
caracter = input("Ingrese el caracter a buscar ")

def buscarCaracter(car, caracter, i, cont):
	if i == len(cadena):
		if car == caracter:
			cont = cont +1
		return cont
	else:
		if car == caracter:
			cont = cont+1
		return buscarCaracter(car, cadena[i], i+1, cont)

numero = buscarCaracter(caracter, cadena[0], 0, 0)
print(numero)