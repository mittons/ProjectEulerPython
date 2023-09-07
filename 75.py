from collections import deque

#Generate next 3 new primitive pythagorean triples uniquely from a single primitive pythagorean triples
def createNext3((c,b,a)):
	rt = [(2*a-2*b+3*c, 2*a-b+2*c, a-2*b+2*c)]
	rt.append((-2*a+2*b+3*c, -2*a+b+2*c, -a+2*b+2*c))
	rt.append((2*a+2*b+3*c, 2*a+b+2*c, a+2*b+2*c))
	return rt

triples = deque([])

triples.append((5,4,3))

#The largest perimeter allowed
maxP = 1500000

pCount = [0]*(maxP+1)

p=0

#Find the perimeter of all primitive pythagorean triples, generate the perimeters of the non primitive ones from the primitive ones
while len(triples) > 0:
	t = triples.popleft()
	perimeter = sum(t)
	while(perimeter <= maxP):
		#primitve perimeter
		pCount[perimeter] += 1
		
		#Non primitive perimeters
		multPerimeter = perimeter*2
		while (multPerimeter) <= (maxP):
			pCount[multPerimeter] += 1
			multPerimeter += perimeter

		next3 = createNext3(t)
		
		t = next3[0]
		perimeter = sum(t)
		
		if sum(next3[1])<=maxP:
			triples.append(next3[1])
		if sum(next3[2])<=maxP:
			triples.append(next3[2])


print pCount.count(1)

