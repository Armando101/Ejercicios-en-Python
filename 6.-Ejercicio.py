"""
Hacer un programa que guarde los números del
1 al 100 en dos tuplas, una va a ser de
números impares y otra de números pares.
Finalmente, imprimir ambas tuplas.
"""

listaA=[]
listaB=[]

for i in range(100):
	if i%2==0:
		listaA.append(i)
	else:
		listaB.append(i)

tuplaA=tuple(listaA)
tuplaB=tuple(listaB)

print(tuplaA)
print(tuplaB)