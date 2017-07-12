from ciclo12 import mein
repetir = 1
while repetir != 0:
	mein()
	print "Si desea repetir marque 1 si no marque 0."
	repetir = int(raw_input("Deseas repetir el proceso:"))
	while repetir > 1:
		repetir = int(raw_input("Marque como se le indica arriba."))