from usefulStuff import *

def prob40(n):
	digits = []
	l = 0
	i = 1
	while l<n:
		lis = intToList(i)
		l += len(lis)
		digits += lis
		i += 1
	
	mult = 1
	for i in [pow(10, j) for j in xrange(7)]:
		mult *= digits[i-1]
	print mult		
	

prob40(pow(10,6))
