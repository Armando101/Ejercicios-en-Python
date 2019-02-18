"""
Se debe diseñar una clase NumeroComplejo, que va a tener
como atributos parteReal y parteImaginaria, se debe definir
un método imprimir que va a imprimir el número complejo con
formato.
Se debe definir un método mágico para la suma de
dos objetos de la clase NumeroComplejo que retorne un nuevo
número complejo que sea la suma de los otros dos. A
continuación se debe crear dos números complejos y probar
sus métodos.
"""

#Definimos la clase

class NumeroComplejo:
	def __init__(self, real, img):
		self.real = real
		self.img = img

	def imprimir(self):
		print("El numero complejo es: " + str(self.real) + " +- " + str(self.img)+"\n")

	# Hacemos uso del metodo magico add
	def __add__(self, other):
		r = self.real + other.real
		i = self.img + other.img
		nuevo = NumeroComplejo(r,i)
		return nuevo


# Creamos dos objetos

complejo1 = NumeroComplejo(5,8)
complejo1.imprimir()

complejo2 = NumeroComplejo(17, 4)
complejo2.imprimir()

complejo3 = complejo1 + complejo2
complejo3.imprimir()
