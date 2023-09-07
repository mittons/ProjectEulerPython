triangle = [[75]]
triangle.append([95,64])
triangle.append([17,47,82])
triangle.append([18,35,87,10])
triangle.append([20,4,82,47,65])
triangle.append([19,1,23,75,3,34])
triangle.append([88,2,77,73,7,63,67])
triangle.append([99,65,4,28,6,16,70,92])
triangle.append([41,41,26,56,83,40,80,70,33])
triangle.append([41,48,72,33,47,32,37,16,94,29])
triangle.append([53,71,44,65,25,43,91,52,97,51,14])
triangle.append([70,11,33,28,77,73,17,78,39,68,17,57])
triangle.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
triangle.append([63,66,4,68,89,53,67,30,73,16,69,87,40,31])
triangle.append([4,62,98,27,23,9,70,98,73,93,38,53,60,4,23])

triangleSums = [[75]]
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

