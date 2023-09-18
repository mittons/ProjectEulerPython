from collections import deque

matrixFile = open("in_82/matrix82.txt", 'r')

matrix = []
for line in matrixFile:
	a = line.split(',')
	b = []
	for item in a:
		b.append(int(item))
	matrix.append(b)

pathSum = [[0]*80 for i in xrange(80)]


bfsList = []
for i in xrange(len(matrix)):
	bfsList.append((matrix[i][0], i, 0))

bfsList.sort()

dude = bfsList.pop(0)

while (dude[2] < 79):
	path = dude[0]
	x = dude[1]
	y = dude[2]
	if ((pathSum[x][y] != 0) and (pathSum[x][y] < path)):
		dude = bfsList.pop(0)		
		continue
#	print "x: {}, y: {}".format(x,y)
	pathSum[x][y] = path
	if x != 79:
		bfsList.append((path+matrix[x+1][y], x+1, y))
	if y != 79:
		bfsList.append((path+matrix[x][y+1], x, y+1))
	if x != 0:
		bfsList.append((path+matrix[x-1][y], x-1, y))
	bfsList.sort()
	dude = bfsList.pop(0)
#	print bfsList


print "x: {}, y: {}, pathsum = {}".format(dude[1],dude[2],dude[0])
