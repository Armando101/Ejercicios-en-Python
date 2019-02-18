"""
Realizar un programa que pida al usuario
números hasta que el usuario ingrese 0,
después de esto va a realizar el promedio de
todos los números ingresados.
"""
listaA=[]
numNumeros=0
while True:
	num = float(input("Dame numeros "))
	if num == 0:
		break
	listaA.append(num)
	numNumeros += 1
suma = sum(listaA)

promedio = suma/numNumeros

print("El promedio es: ", promedio)
