# -*- coding: utf-8 -*-
print "calcular el exponentede N"
i = 0
potencia = 0
base = int(raw_input("cual es la base:"))
exponente = int(raw_input("cual es el exponente:"))

for i in range (1, exponente):
	if potencia == 0:
		potencia = base * base
	else:
		nuevapotencia = potencia * base
		potencia = nuevapotencia

print "la potencia es %d" % potencia

