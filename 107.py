from collections import deque

f = open('in_107/network107.txt','r')

lines = f.readlines()

matrix = map(lambda l: l[:-1].split(','), lines)

connected = set([])	
edges = []
allEdges = []
#vEdges = []
V = len(matrix)
for i in xrange(V):
#	adjacent = []
	for j in xrange(i+1,V):
		if matrix[i][j] != '-':
			allEdges.append((int(matrix[i][j]),i,j))
#			adjacent.append((matrix[i][j],i,j))


E = len(allEdges)

maxDist = 0
for e in allEdges:
	maxDist += int(e[0])
allEdges.sort()
#allEdges = deque(allEdges)
edges.append(allEdges.pop(0))

connected.add(edges[0][1])
connected.add(edges[0][2])

while len(connected)<V:
	i = 0
	while not((allEdges[i][1] not in connected and allEdges[i][2] in connected) or (allEdges[i][1] in connected and allEdges[i][2] not in connected)):
		i += 1
	e = allEdges.pop(i)
	edges.append(e)
	connected.add(e[1])
	connected.add(e[2])


minDist = 0
for e in edges:
	minDist += int(e[0])

print maxDist, minDist
print maxDist - minDist 

