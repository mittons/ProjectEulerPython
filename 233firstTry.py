from math import cos, pi, sqrt

#http://en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
#http://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity


specialK = cos(pi/4)
sqrt2 = sqrt(2)

D = {}
#print (10000**2)/2
#print (10000/sqrt2)**2
for n in xrange(7000,8001):
	n2 = n*2
	nSqr = D.setdefault(n2, (n2)**2)
	nSqrDiv2 = nSqr/2
	numStuff = 0
#	print (int((n2/sqrt2)*specialK),(n2/sqrt2)+1)
	for i in xrange(int((n2/sqrt2)*specialK),int(n2/sqrt2)):
#		print nSqrDiv2 ,i**2
		a = (nSqrDiv2 - D.setdefault(i,i**2))
#		print a
#		print sqrt(a)
		sqa = int(sqrt(a))
		if (D.setdefault(sqa, sqa**2) == a):
			print n,sqa,i
			numStuff += 1
	print numStuff
	if numStuff == 14:
		print "yay"
		break
