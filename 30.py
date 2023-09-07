def topLevelOfRecursion():
	s = -1 #Since apparently 1 doesnt count as a sum of itself in the pow of 5
	for i in xrange(1,10):
		s += highToLowOrderDynamic(i, pow(i,5), 1)
	return s

def highToLowOrderDynamic(number, summ, depth):
	r = 0
	if (number == summ):
		r = number
		print number
	if ((depth < 6) and (number < 35430)):
		for i in xrange(10):
			r += highToLowOrderDynamic(number*10+i, summ+pow(i,5), depth+1)
	return r

print topLevelOfRecursion()
