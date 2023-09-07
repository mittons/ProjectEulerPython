
def howManyCoinCombos(n):
	combos = [[0]*8 for i in xrange(n+1)]	
	coins = [200,100,50,20,10,5,2,1]
	for i in range(len(coins)):
		if coins[i] <= n:
			combos[coins[i]][i] = 1
	for i in xrange(1,n):
		for j in range(len(coins)):
			for k in range(j,len(coins)):
				if i+coins[k] <= n:
					combos[i+coins[k]][k] += combos[i][j]
	print sum(combos[n])

howManyCoinCombos(200)
					
			
