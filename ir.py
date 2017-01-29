# -*- coding: utf-8 -*-
print "repaso de def"
contador = 0
vector = []
matriz = []

def entra():
	cantidad = int(raw_input("cuantos numeros:"))
	return procesa(cantidad)

def procesa(cantidad):
	repetir = 1
	while repetir != 0:
		contador = 0
		if cantidad == 2:
			for i in range(0, 2):
				matriz.append([])
				for j in range(0 , 2):
					numero = int(raw_input("cual es el numero:"))
					contador = contador + numero
					matriz[i].append(numero)
			print "esta es su matris de dos por dos en fila", matriz
			print "---------------------------------------"
			print "esta es la matriz en orden"
			print "la suma es:", contador
			for i in range(0, 2):
				print matriz[i]		
					
		elif cantidad == 3:
			contador = 0
			for i in range(0, 3):
				matriz.append([])
				for j in range(0, 3):
					contador = contador + numero
					numero = int(raw_input("cual es el numero:"))
					matriz[i].append(numero)
			print "esta es su matris de tres por tres en fila", matriz
			print ("-----------------------------------------")
			print "esta es la matriz en su orden"
			print "esta es la suma", contador
			for i in range(0, 3):
				print matriz[i]

		else:
			for i in range(cantidad):
				numero = int(raw_input("cual es el numero:"))
				vector.insert(i, numero)
			print "este es su vector:", vector

	repetir = int(raw_input("¿desea repetir este proceso? si es si marque 1 si es no marque 2:"))
	return repetir
	
def mein():
	entra()
