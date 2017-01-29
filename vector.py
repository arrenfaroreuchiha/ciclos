# -*- coding: utf-8 -*-
print "un vector"
lista = []
matriz = []

def entra():
	cantidad = int(raw_input("cantida de numeros:"))
	return procesa(cantidad)

def procesa(cantidad):	
	for i in range(cantidad):
		numero = int(raw_input("cual es el numero:"))
		lista.insert(i, numero)
		

	for i in range(2):
		matriz.append([])
		for j in range(2):
			num = int(raw_input("numero:"))
			matriz[i].append(num)

	print "este es el vector:", lista
	print "esta es la matriz por fila:", matriz
	return sale(lista, matriz)

def sale(lista, matriz):
	print "esta es la matris en su orden" 
	for i in range(0, 2):
		print matriz[i]
	print  "esta es la matriz disuelta"
	for i in range(0, 2):
		for j in range(0, 2):
			print matriz[i][j]

entra()