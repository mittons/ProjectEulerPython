def factorial(n):
	fn = 1
	for i in xrange(2,n+1):
		fn *= i
	return fn

def C(n,k):
	return factorial(n)/(factorial(n-k)*factorial(k))

def P(n,k):
	return factorial(n)/(factorial(n-k))

facs = [factorial(i) for i in xrange(51)]



#for tileSize in xrange(3,blackTiles+1):
def fillRow(blackTiles, tileSize, redTiles):
	if ((blackTiles+1-redTiles)/(tileSize+1)) == 0:
		return P(blackTiles+1,redTiles) 
	
	tileArrangements = 0
	for i in xrange(((blackTiles+1-redTiles)/(tileSize+1))+1):
		blk = blackTiles - tileSize*i
		
		tileArrangements += (fillRow(blk, tileSize+1, redTiles+i)/factorial(i))
	
	return tileArrangements

print fillRow(50,3,0)

