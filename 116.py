def factorial(n):
	fn = 1
	for i in xrange(2,n+1):
		fn *= i
	return fn

def C(n,k):
	return float(factorial(n))/(factorial(n-k)*factorial(k))

facs = [factorial(i) for i in xrange(51)]

blackTiles = 50


tileArrangements = 0
for tileSize in xrange(2,5):
	for i in xrange(1,(blackTiles/tileSize)+1):
		blk = blackTiles - tileSize*i
		assert blk >= 0
		tileArrangements += (facs[blk+i]/(facs[i]*facs[blk]))

print tileArrangements
