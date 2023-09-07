import time

start = time.clock()



chains = [-1]*(pow(10,7))

digitSquares = [0]*(pow(10,7))

chains[1]=1
chains[89]=89

digitPow2 = [pow(i,2) for i in xrange(10)]


def dynamicNumbers(n, sumOfDigitSquares, depth):
	digitSquares[n] = sumOfDigitSquares
	if depth<7:
		for i in xrange(10):
			dynamicNumbers(n*10+i,sumOfDigitSquares+digitPow2[i], depth+1)

for i in xrange(1,10):
	dynamicNumbers(i, digitPow2[i], 1)

print "Cool"

chains[1] = 0
chains[0] = 0
chains[89] = 1

for i in xrange(2,len(chains)):
	if chains[i] != -1:
		continue
	curr = i
	chain = [i]
	while(digitSquares[curr] != 1 and digitSquares[curr] != 89):
		curr = digitSquares[curr]
		chain.append(curr)
	if digitSquares[curr] == 1:
		for c in chain:
			chains[c] = 0
	else:
		for c in chain:
			chains[c] = 1

print "Cool"


print sum(chains)

end = time.clock()

print "Cool"

print "Time: {}".format(end-start)

