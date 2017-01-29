# -*- coding: utf-8 -*-
print "factorrial de N"
i = 1
total = 1
contador = 1
factorial = int(raw_input("cual es el factorial: "))

for i in range (1, factorial):
	total = i * factorial
	factorial = total
	
print "el total es", total