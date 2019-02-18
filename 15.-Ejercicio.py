"""
Se debe simular una agenda telefónica. Cuando inicie el programa se
debe desplegar un menú con las opciones:
● Agregar contacto
● Eliminar contacto
● Mostrar contacto
● Salir
Los contactos van a ser almacenados en un diccionario en donde las
llaves son los nombres de los contactos y sus valores van a ser los
teléfonos.
Se debe diseñar funciones para las opciones de Agregar Contacto,
Eliminar Contacto y Mostrar Contacto.
"""

import os

contactos = {}

def agregar():
	nom = input("Ingresa el nombre del nuevo contacto ")
	tel = input("Ingrese el numero de su contacto ")
	contactos.setdefault(nom, tel)

def mostrar():
	def func(llave):
		return llave + ":"+ contactos.get(llave)
	lista = contactos.keys()
	for i in map(func,lista):
		print(i)

def mostrarContacto():
	con = input("Ingresa el contacto que deseas mostrar ")
	def func(con2):
		return con == con2
	lista = contactos.keys()
	for i in map(func, lista):
		if i :
			print(con + ":" + contactos.get(con))
			return 0
	print("El contacto no esta registrado\n")

def eliminar():
	con = input("Ingresa el contacto que deseas eliminar ")
	contactos.pop(con)		
	print('\n')

while True:
	op = int(input("Buenos dias\nQue accion desea realizar\n1)Agregar contaco\n2)Eliminar contacto\n3)Mostrar contacto\n4)Mostrar todos los contactos\n5)Salir\n"))

	if op == 5:
		break
	elif op == 4:
		os.system("clear")	
		mostrar()
	elif op == 3:
		os.system("clear")	
		mostrarContacto()
	elif op == 2:
		eliminar()
		os.system("clear")	
	elif op == 1:
		agregar()
		os.system("clear")	
	else:
		print("Opcion invalida")







