"""
Se debe hacer una calculadora que pueda calcular el
área de un cuadrado, un círculo o un triángulo, se
debe pedir al usuario la figura para la que se quiere
calcular el área y a continuación los valores
necesarios para calcularla, ya sea el radio, la base y
la altura o un lado. Se debe definir tres funciones
que calculen el área, una para el cuadrado, otra para
el triángulo y otra para el círculo.
"""

# Definicion de funciones
import math

def areaCuadrado(b):
	print("El area del cuadrado es: ", b*b)

def areaTriangulo(b,h):
	print("El area del triangulo es: ", b*h/2)

def areaCirculo(r):
	print("El area del circulo es: ", (math.pi*r)**2)


op = input("Bienvenido\nDe que figura quiere calcular el area\n1)Cuadrado\n2)Triangulo\n3)Circulo\n")

if op == "1":
	b = int(input("Ingersa el lado del cuadrado "))
	areaCuadrado(b)

elif op == "2":
	b = int(input("Ingresa la base del triangulo "))
	h = int(input("Ingresa la altura del triangulo "))
	areaTriangulo(b,h)

elif op == "3":
	r = int(input("Ingresa el radio del circulo "))
	areaCirculo(r)

else :
	print("Ingrese una opcion valida ")
