f1 = 1
f2 = 2
b = False
c = pow(10,999)
d = 4

while(True):
	if b==False:
		f1 += f2
		if (f1/c) > 0:
			print d
			break
	else:
		f2 += f1
		if (f2/c) > 0:
			print d
			break
	b ^= True
	d += 1
