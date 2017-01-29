
vector= []
cantidad = int(raw_input("cantidad:"))

for i in range(cantidad):
	numero = int(raw_input("numero:"))
	vector.insert(i, numero)
	vector.sort()

print vector
print "-------------------------"

c = 0
for i in vector:
	c += 1
	print "la pocicion es:%d el valo es:%d" % (c, i)
	

