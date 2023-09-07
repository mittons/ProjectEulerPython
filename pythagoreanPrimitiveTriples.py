#Something i decided to keep, this creates primitive pythagorean triples quite nicely

from collections import deque

def createNext3((c,b,a)):
	rt = [(2*a-2*b+3*c, 2*a-b+2*c, a-2*b+2*c)]
	rt.append((-2*a+2*b+3*c, -2*a+b+2*c, -a+2*b+2*c))
	rt.append((2*a+2*b+3*c, 2*a+b+2*c, a+2*b+2*c))
	return rt

triples = deque([])

triples.append((5,4,3))

minC = 5
maxC = 38000000#pow(10,7)#pow(10,11)+1
q = 5

D = {}

while len(triples) > 0:
	t = triples.popleft()
	while(t[0]<maxC):
		D.setdefault(t[0], []).append(t[0])
		next3 = createNext3(t)
		t = next3[0]
		if next3[1][0]<maxC:
			triples.append(next3[1])
		if next3[2][0]<maxC:
			triples.append(next3[2])
#	print len(triples)


s = 0
while(q<maxC):				
	if q in D:
		if len(D[q]) == 52:
			print q
			s+=q
		for p in D[q]:
			D.setdefault(p+q, []).append(p)
		del D[q]
	q += 1

print s	
