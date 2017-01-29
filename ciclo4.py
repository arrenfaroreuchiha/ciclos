# -*- coding: utf-8 -*-
print "serie de fibonacci"

a = 1
b = 0
numero = int(raw_input("cual es el numero: "))

for i in range (0, numero):
	suma = b + a
	b = a
	a = suma
	print i

	
print "las suma es", suma