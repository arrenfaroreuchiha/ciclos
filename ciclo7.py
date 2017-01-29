# -*- coding: utf-8 -*-
print "suma de numeros pares"
i = 1
par = 0
numero = int(raw_input("cantidad de numeros:"))

for i in range (numero):
	numero2 = int(raw_input("numero:"))
	contador = numero2
	contador = numero2 % 2
	if contador == 0:
		par = par + numero2
		print "suma de numeros pares:", par 
	else:
		print "el numero es impar:", numero2
		

