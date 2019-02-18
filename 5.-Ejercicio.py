"""
Programa que capture dos números ingresados
por el usuario y en base a esos números cree
un número complejo que va a imprimir en
consola. Considerar que las entradas pueden
ser números decimales.
"""

a = float(input("Dame la parte real "))
b = float(input("Dame la parte imaginaria "))

print("El numero complejo es: " + str(a) + "+"+str(b)+"i")