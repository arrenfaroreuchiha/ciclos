# -*- coding: utf-8 -*-
print "precios-promedio-iva-subtotal-total de un producto"
i = 1
condicional = 0
condicional1 = 0
condicional2 = 0
condicional3 = 0
a = 1
b = 2
c = 3

print "harina pan = $2500-1"
print "aceite = $3000-2"
print "bolsa de leche = $2300-3"
producto = 4
cantidad = int(raw_input("cuantos productos:"))


for i in range (cantidad):
	while producto > 3:
		print "-------------------------------"
		print "por favor marque el producto con su respectivo numero(1,2,3)"
		producto = int(raw_input("cual producto:"))
		
		
	if producto == 1:
		cantidad1 = int(raw_input("cantidad:"))
		condicional = 2500 * cantidad1
		producto = 4
		#print condicional
		
	elif producto == 2:
		cantidad2 = int(raw_input("cantidad:"))
		condicional1 = 3000 * cantidad2
		producto = 4
		#print condicional1
		
	elif producto == 3:
		cantidad3 = int(raw_input("cantidad"))
		condicional2 = 2300 * cantidad3
		producto = 4
		#print condicional2

print "--------------------------------"
subtotal = condicional + condicional2 + condicional1
print "el subtotal es:", subtotal

iva = subtotal * 16 / 100
print "el iva es: %d" % iva

total = subtotal + iva
print "el total es: %d" % total






		
		

