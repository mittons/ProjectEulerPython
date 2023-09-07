D = {}

q = 2
consec = 0
while consec != 4:
	if q not in D:
		D.setdefault(q+q,[]).append(q)
		consec = 0
	else:
		for p in D[q]:
			D.setdefault(p+q, []).append(p)
		if len(D[q])==4:
			consec += 1
		else:
			consec = 0
			del D[q]
	q += 1

q-= 1
for i in xrange(4):
	print "q:{}, D[q]:{}".format(q-i,D[q-i])

