# -*- coding: utf-8 -*-
print "multiplos de 5"
i = 1
contador = 0
numero = int(raw_input("cantidad de numeros:"))

for i in range (numero):
	numero2 = int(raw_input("numero:"))
	contador2 = numero2 % 5
	if contador2 == 0:
		print "es multiplo de 5"
		contador = contador + numero2
		print "la suma de los multiplos de 5 es:", contador
	else:
		print "no es multiplo de 5:", numero2