# -*- coding: utf-8 -*-
print "multiplos de 3"


def a():
	numero = int(raw_input("cantidad de numeros:"))
	return b(numero)

def b(numero):
	i = 1
	contador = 0
	for i in range (numero):
		numero2 = int(raw_input("numero:"))
		contador2 = numero2 % 3
		if contador2 == 0:
			print "es multiplo de 3"
			contador = contador + numero2
		
		else:
			print "no es multiplo de 3:", numero2
			
	print "la suma de los multiplos de 3 es:", contador

a()
