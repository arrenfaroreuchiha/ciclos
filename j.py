cantidad = int(raw_input("cantidad:"))
vector = []
for i in range(cantidad):
	numero = int(raw_input("numero:"))
	vector.append(numero)

for i in vector:
	if i == 1:
		print "numero mayor a uno:", i
	if i == 0:
		print "numero menor a uno:", i
print vector
