
matrixFile = open("in_83/matrix83.txt", 'r')

matrix = []
for line in matrixFile:
	a = line.split(',')
	b = []
	for item in a:
		b.append(int(item))
	matrix.append(b)

pathSum = [[0]*80 for i in xrange(80)]

bfsList = []
dude = (matrix[0][0], 0, 0)

while (dude[1] < 79 or dude[2] < 79):
	path = dude[0]
	x = dude[1]
	y = dude[2]
	if ((pathSum[x][y] != 0) and (pathSum[x][y] < path)):
		dude = bfsList.pop(0)		
		continue
#	print "x: {}, y: {}".format(x,y)
	pathSum[x][y] = path
	if x != 0:
		bfsList.append((path+matrix[x-1][y], x-1, y))
	if x != 79:
		bfsList.append((path+matrix[x+1][y], x+1, y))
	if y != 0:
		bfsList.append((path+matrix[x][y-1], x, y-1))
	if y != 79:
		bfsList.append((path+matrix[x][y+1], x, y+1))
	bfsList.sort()
	dude = bfsList.pop(0)
#	print bfsList

print "x: {}, y: {}, pathsum = {}".format(dude[1],dude[2],dude[0])
