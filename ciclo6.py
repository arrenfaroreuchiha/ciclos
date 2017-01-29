# -*- coding: utf-8 -*-
print "numeros impares y el promedio"
i = 1
impar = 0
numero = int(raw_input("cantidad de numeros: "))
impar2 = 0
vector = []

for i in range (numero):
	numero2 = int(raw_input("numero: "))
	contador = numero2
	contador = numero2 % 2
	if contador > 0: 
		impar = impar + numero2
	else:
		vector.append(numero2)
		print "no es numero impar:", numero2
print "--------------------------------"	
 
print "suma de numeros impares:", impar
impar2 = impar / numero
print "el promedio de los numeros impares es:", impar2
print "---------------------------------"
print vector
