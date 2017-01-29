# -*- coding: utf-8 -*-
lista = []
vector = []
matriz = []

class a:
	def b(self):
		cantidad = int(raw_input("cuantos numeros:"))
		return cantidad

	def c(self, cantidad):
		contador = 0
		if cantidad == 3:
			contador = 0
			for i in range(0, 3):
				matriz.append([])
				for j in range(0, 3):
					numero = int(raw_input("cual es el numero:"))
					contador = contador + numero
					matriz[i].append(numero)
					matriz.sort

			print "esta es la matriz de 2x2:", matriz
			print "este es el numero mayor de la matriz:", max(max(matriz))
			print "este es el menor de la matriz:", min(min(matriz))
			for i in range(0, 3):
				print matriz[i]

		if cantidad == 2:
			contador = 0
			for i in range(0, 2):
				lista.append([])
				for j in range(0, 2):
					numero = int(raw_input("cual es el numero:"))
					contador = contador + numero
					lista[i].append(numero)
					lista.sort
		
			print "esta es la matriz de 2x2:", lista
			print "este es el numero mayor de la matriz:", max(max(lista))
			print "este es el menor de la matriz:", min(min(lista))
			for i in range(0, 2):
				print lista[i]
		else:
			for i in range(cantidad):
				numero = int(raw_input("cual es el numero:"))
				vector.append(numero)
				vector.sort
			print "este es el vector:", vector
			print "este es el numero mayor del vector:", max(vector)
			print "este es el numero menor del vector:", min(vector)
			print "esta es la cantidad de numeros que hay en el vector:", len(vector)


		

	def d(self, cantidad):
		print "-----------------------------------------"
		suma = 0
		for i in range(cantidad):
			numero = int(raw_input("cual es el numero:"))
			suma = suma + numero
		print "esta es la suma:", suma
		repetir = int(raw_input("desea repetir este proceso de nuevo 1 o 0:"))
		return repetir


s = 1
while s != 0:
	b = a()
	z = b.b()
	y = b.c(z)
	s = b.d(z)
				
				


