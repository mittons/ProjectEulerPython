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
tileSize = [2,3,4]

for i in xrange((blackTiles/tileSize[0])+1):
	blk = blackTiles - tileSize[0]*i
	for j in xrange((blk/tileSize[1])+1):
		blk2 = blk - tileSize[1]*j
		kLowerBound = 0
		for k in xrange((blk2/tileSize[2])+1):
			blk3 = blk2 - tileSize[2]*k
			tileArrangements += (facs[blk3+i+j+k]/(facs[i]*facs[j]*facs[k]*facs[blk3]))

print tileArrangements
