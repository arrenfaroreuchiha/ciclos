# -*- coding: utf-8 -*-
print "promedio de materias y calificacion"

def a():
	materias = int(raw_input("cuantas materias:"))
	return b(materias)

def b(materias):
	condicional = 0
	condicional1 = 0
	i = 0
	promedio = 0
	for i in range (materias):
		notas = float(raw_input("puntaje:"))
		condicional = notas + condicional
		creditos = float(raw_input("creditos:"))
		condicional1 = creditos + condicional1
		lista = [condicional, condicional1, materias]
	return c(lista)
	
def c(lista):
	condicional = lista [0]
	condicional1 = lista[1]
	materias = lista[2]	
	promedio = condicional / materias
	print "suma de notas finales:", condicional
	print "suma de creditos finales:", condicional1
	print "promedio del semestre:", promedio


def mein():
	a()
	
	

	
	
