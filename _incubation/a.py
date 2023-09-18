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

prizeStringCount = 0 

onTimes = 30
#how many single A's there can be
for i in xrange(((onTimes+1)/(1+1))+1):
	onTime = onTimes-i
	#How many single AA's there can be given the current count of single A's (single AAs obviously cant be next to a single A)
	for j in xrange(((onTime+1-i)/(2+1))+1):
		onT = onTime-(j*2)
		#The number of possible places you can pick for each A or AA(this is equal to the number of spaces between two consecutive O's (or the number of pairs of Os that are next to each other), plus the places at ends, if they are occupied by O's you can put A's further in the end). This is multipled by the number of places you can put the L (you can swap out any O, or no O for L)
		prizeStringCount += (P(onT+1,i+j)/(facs[i]*facs[j]))*(onT+1)

print prizeStringCount
