print "precios-promedio-iva-subtotal-total de un producto"
i = 1
condicional = 0
condicional1 = 0
condicional2 = 0
condicional3 = 0
a = 1
b = 2
c = 3

def entra():
	print "harina pan = $2500-1"
	print "aceite = $3000-2"
	print "bolsa de leche = $2300-3"
	global producto 
	producto = 4
	global cantidad
	cantidad = int(raw_input("cuantos productos:"))

def algoritmo():
	for i in range (cantidad):
		while producto > 3:
			print "por favor marque el producto con su respectivo numero(1,2,3)"
			producto = int(raw_input("cual producto:"))
			
		if producto == 1:
			cantidad1 = int(raw_input("cantidad:"))
			condicional = 2500 * cantidad1
			
		elif producto == 2:
			cantidad2 = int(raw_input("cantidad:"))
			condicional1 = 3000 * cantidad2
			
		elif producto == 3:
			cantidad3 = int(raw_input("cantidad"))
			condicional2 = 2300 * cantidad3
		

def salida():
	subtotal = condicional + condicional2 + condicional3
	print "el subtotal es:", subtotal

	iva = subtotal * 16 / 100
	print "el iva es: %d" % iva

	total = subtotal + iva
	print "el total es: %d" % total

def main():
	entrada()
	algoritmo()
	salida()
