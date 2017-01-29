# -*- coding: utf-8 -*-
print "el promedio de numeros N"
numero = int(raw_input("cantidad de numeros: "))
contador = 0
i = 1
for i in range (numero):
	numero2 = int(raw_input("cual es el numero: "))
	contador = contador + numero2

print "suma de los numeros", contador

contador = contador / numero
print "el promedio es", contador



