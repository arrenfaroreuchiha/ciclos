#
#clave = 1224
#clave2 = 2412


print "hola eduardo"
numero = int(raw_input("clave:"))
repetir = 1
while repetir != 0:
	while numero != 1224:
		numero = int(raw_input("clave:"))

	if numero == 1224:
		print "---------------"
		print "hola eduardo bienvenido"
		numero2 = int(raw_input("eduardo marque la clave:"))
		while numero2 != 2412:
			print "----------------"
			numero2 = int(raw_input("Eduardo la clave por favor:"))

	if numero2 == 2412:
		print "-----------------"
		print "su numero de tarjeta es 12242414 adios"
	repetir = int(raw_input("desea repetir este proceso? si es si marque 1 si es no marque 0"))

