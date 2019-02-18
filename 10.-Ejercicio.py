"""
Escribir un programa que pida al usuario una
cadena de texto e imprima la misma cadena de
texto, pero antes de cada vocal, agregue una
f.
Ejemplo:
“Mi nombre es Ana”
“Mfi nfombrfe fes fAnfa”
"""

cadena = input("Ingrese su cadena ")
cadenaA=[]
for x in cadena:
	if x in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
		cadenaA.append('f')
		cadenaA.append(x)
	else:
		cadenaA.append(x)

cadenaA = "".join(cadenaA)
print(cadenaA)