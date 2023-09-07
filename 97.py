from math import log

#reikna 2^2^i
def twosPowerMod10(i):
	twos = 2
	for i in xrange(i):
		twos = (twos*twos)%pow(10,10)
	return twos
p = 7830457
a = 28433
b = 2

m = pow(10,10)
num = 1

while p != 0:
	nexti = int(log(p))
	num *= twosPowerMod10(nexti)
	num %= m
	p -= 2**nexti

print (num*a+1)%m
