count = 0
for i in xrange(1,pow(2,30)+1):
	if i^2*i^3*i == 0:
		count+=1
print count
