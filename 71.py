def factorizeUpTo(n):
	factorLists = [[] for i in xrange(n)]
	for i in xrange(2,n):
		if len(factorLists[i]) == 0:
			k = i
			while k<n:
				factorLists[k].append(i)
				k += i
	return factorLists

def containSameFactor(factorL1, factorL2):
	for factor in factorL1:
		if factor in factorL2:
			return True
	return False

def prob71(n):
	factorLists = factorizeUpTo(n)
	target = 3.0/7.0
	closest = 1.0/4.0
	clNum = 1
	for antiDenominator in xrange(n-3):
		denominator = n-1-antiDenominator
		if denominator == 7:
			continue
		numerator = int(denominator*target)
		while float(numerator)/denominator > closest:
			if not containSameFactor(factorLists[numerator],factorLists[denominator]):
				clNum = numerator
				closest = float(numerator)/denominator
				print "new best value: numerator={}, denominator={}, fraction={}".format(numerator, denominator, float(numerator)/denominator)
				break
			else:
				if numerator == 1:
					break
				else:
					numerator -= 1
		
	print clNum	

prob71(1000001)
