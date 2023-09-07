def createSpiral(n):
	spi = [[0]*n for i in xrange(n)]
	num = 1
	x = y = (n-1)/2
	spi[x][y] = num
	for i in xrange(1,((n-1)/2)+1):
		x += 1
		num += 1
		spi[x][y] = num
		for k in xrange((2*i)-1):
			y -= 1
			num += 1
			spi[x][y] = num
		for k in xrange(2*i):
			x -= 1
			num += 1
			spi[x][y] = num
		for k in xrange(2*i):
			y += 1
			num += 1
			spi[x][y] = num
		for k in xrange(2*i):
			x += 1
			num += 1
			spi[x][y] = num

	return spi

def diagonalSpiralSum(n):
	spi = createSpiral(n)
	sum = 1
	for i in xrange((n-1)/2):
		sum += spi[i][i]
		sum += spi[i][n-1-i]
		sum += spi[n-1-i][i]
		sum += spi[n-1-i][n-1-i]
	print sum

diagonalSpiralSum(1001)


