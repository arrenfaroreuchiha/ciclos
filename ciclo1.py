# -*- coding: utf-8 -*-
contador = 0
total = 0

while contador < 10:
	numero = int(raw_input("numero %d es:" % contador))
	total = total + numero 
	contador += 1

print "el total es", total
print contador