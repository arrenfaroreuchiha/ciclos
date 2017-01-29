# -*- coding: utf-8 -*-
i = 1
numero = int(raw_input("numero:"))

for i in range (1):
	contador = numero % 2
	if contador == 1:
		print "el numero es primo"
	elif contador > 1:
		contador = numero % i 
	elif contador == 0:
		print "el numero no es primo"
	


	
