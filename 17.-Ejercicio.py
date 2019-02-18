"""
Se debe diseñar una clase CuentaBancaria que va a tener los métodos
mostrarInformación, depósito y retiro, como atributos, cada objeto
va a tener un saldo y un nombre. El método mostrar información va a
imprimir el nombre de la cuenta y el saldo, el método depósito va a
agregar una cantidad al saldo de la cuenta y va a mostrar
información. El método retiro va a retirar dinero de la cuenta, pero
antes tendrá que comprobar que se cuente con el dinero suficiente,
terminando el retiro va a mostrar información. Cada vez que se cree
un objeto, va a mostrar información de la cuenta. Se debe crear dos
objetos y llamar sus métodos para probarlos.
"""

# Definimos la clase

class CuentaBancaria:
	def __init__(self, nombre, saldo):
		self.nombre = nombre
		self.saldo = saldo

	def mostrarInformacion(self):
		print("Nombre: " + self.nombre + "\nSaldo: "+ str(self.saldo)+"\n"*2)

	def deposito(self, cantidad):
		self.saldo += cantidad

	def retiro(self, cantidad):
		if self.saldo < cantidad:
			print("No puedes retirar esa cantidad")
		else:
			self.saldo -= cantidad


# Procedemos a crear algunos objetos

Persona1 = CuentaBancaria("Armando", 1500)
Persona2 = CuentaBancaria("Juan", 500)


Persona1.mostrarInformacion()
Persona1.deposito(500)
Persona1.mostrarInformacion()

Persona2.mostrarInformacion()
Persona2.retiro(1000)
Persona2.mostrarInformacion()
