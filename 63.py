from math import log10
maxPower = 1000

count = 0

num = 1
while maxPower > 1:
	for i in xrange(1,maxPower):
		n = int(log10(num**i))
		if i == n+1:
			print num, i, num**i
			count += 1
		elif i < n+1:
#			print num, i, num**i, maxPower
			maxPower -= 1
			break
#		else:
#			print num, i
	num += 1

print count
