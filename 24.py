from collections import deque

def howManyDistinctSumsMake(n):
	#We can get a_0 = 1 sums using the number 99 as the largest number in the sum
	#We can get a_1 = 1 + a_0 sums using the number 98 as the largest number in the sum
	#When a_0 stands for n, then a_max stands for 1 and max is n-1
	bfslist = deque([])
	count = 0
	for i in xrange(1,(n/2)+1):
		bfslist.append((i,i))
	while len(bfslist) != 0:
		dude = bfslist.popleft()
		if dude[0] > n:
			continue
		if dude[0] == n:
			count += 1
			continue
		for i in xrange(dude[1],n-dude[0]+1):
			bfslist.append((i+dude[0],i))
	print count
		
	
howManyDistinctSumsMake(100)

