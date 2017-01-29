# -*- coding: utf-8 -*-
print "menor de numeros"
numero = int(raw_input("cantidad de numeros:"))
for i in range(0, numero):
	numero1 = int(raw_input("digite el numero:"))
	if i == 0:
		menor = numero1
	if numero1 < menor:
		menor = numero1

print "el numero menor es:", menor
		


	

