triangle = []

f = open('triangle67.txt','r')
for line in f:
	triangle.append((map(lambda s: int(s),line[:-1].split(' '))))

print triangle
triangleSums = [triangle[0]]

print triangleSums


for i in xrange(len(triangle)-1):
	triS=[]
	triS.append(triangleSums[i][0]+triangle[i+1][0])
	for j in xrange(len(triangle[i+1])-2):
		if (triangleSums[i][j] > triangleSums[i][j+1]):
			triS.append(triangleSums[i][j]+triangle[i+1][j+1])
		else:
			triS.append(triangleSums[i][j+1]+triangle[i+1][j+1])
	last = len(triangle[i])
	triS.append(triangleSums[i][last-1]+triangle[i+1][last])
	triangleSums.append(triS)

print max(triangleSums[len(triangleSums)-1])

