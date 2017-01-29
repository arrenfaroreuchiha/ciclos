# -*- coding: utf-8 -*-
print "menor y mayor de numeros N"

x = 0
contador = 0
#i = 1
lista =[]
numero = int(raw_input("cantidad de numeros:"))

for i in range (numero):
	i += 1
	numero2 = int(raw_input("numero:"))
	if numero2 > contador:
		contador = numero2
	lista.append(numero2)

print "el numero mayor es:", contador
		
for i in range(numero):
	x = i + 1
	for x in range(x, numero):
		if lista[i] > lista[x]:
			menor = lista[x]
		else:
			menor = lista[i]
	break

print "el numero menor es:", menor