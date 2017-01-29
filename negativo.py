# -*- coding: utf-8 -*-
contador = 0

print "suma de numeros 2"
numero = int(raw_input("cantidad de numeros:"))
for i in range(numero):
	print "---------------------------"
	numero1 = int(raw_input("cual es el numero:"))
	if numero1 == 2:
		contador = contador + numero1
	
print "-----------------------"
print "la suma es:", contador