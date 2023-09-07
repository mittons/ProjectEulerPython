properDivisors = [[1] for i in xrange(10001)]

for i in xrange(2,10001):
	for j in xrange(i+1,10001):
		if j % i == 0:
			properDivisors[j].append(i)

amicableCandidates = []

for i in xrange(10001):
	amicableCandidates.append(sum(properDivisors[i]))

amicableSum = 0

for i in xrange(2,10001):
	if amicableCandidates[i] != i and amicableCandidates[i] < 10001:
		if amicableCandidates[amicableCandidates[i]] == i:
			amicableSum += i

print amicableSum
