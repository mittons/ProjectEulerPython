def modeach(a,b):
	c = []
	for i in xrange(len(a)):
		c.append(a[i]^b[i])
	print c
	return c

def alert(rf):
	guy = [71,3,13,0,7,16]
	print "{}".format(modeach(guy,rf+rf[:2]))
	print "{}".format(modeach(guy,rf[1:]+rf))
	print "{}".format(modeach(guy,rf[2]+rf+rf[0]))
