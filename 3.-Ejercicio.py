"""
Programa que imprima en pantalla el tipo de
dato de todos los elementos contenidos en una
lista. La lista la deben crear ustedes con
diferentes tipos de datos.
"""

lista = [1, True, [1, 2, 5], False, "Hola mundo", (1, True, "Tupla")]

for x in lista:
	print(type(x))