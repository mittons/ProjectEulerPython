from usefulStuff import *
from math import sqrt


MAXPRIME = int(sqrt(pow(10,8)+1))
primesBool = sieve(MAXPRIME)
primes = sieveToPrimes(primesBool)

pow2 = [int(pow(2,i)) for i in xrange(16)]
	
squireFree = [65535]*(125000000)
theta = [[0,6,12],[2,8,14],[4,10]]
beta = 0

#for i in xrange(len(squireFree)):
#	for thet in theta[beta]:
#		squireFree[i] = (squireFree[i] & (~pow2[thet]))
#	beta = (beta+1)%3

#print "Yess"

fiboSqDiv = [0]*len(primes)
fiboSqDiv[0] = 6
fiboSqDiv[1] = 12
fiboInd = [0,1]
nextDivisorPrime = 1
def findDivisors(n,d):
	global fiboSqDiv
	global fiboInd
	global squireFree
	if len(fiboInd) == len(primes):
		return 0
	i = 0
	pr = primes[0]
	while n >= pr:
		if n%primes[i] == 0:
			if fiboSqDiv[i] == 0:
				if primes[i] != 3:
					fiboSqDiv[i] = primes[i]*d
					fiboInd.append(i)
					print "Going for {}".format(primes[i])
					divi = primes[i]*d
					divis = divi
					while divis<(pow(10,9)*2):
						squireFree[int(divis/16)] &= (~pow2[divis%16])
						divis += divi
					print "Done for {}".format(primes[i])
		i += 1
		if pr == primes[-1]:
			break
		pr = primes[i]

def isSquareFree(d):
	return (squireFree[int(d/16)] & pow2[d%16] != 0)

#	for i in fiboInd:
#		if d%fiboSqDiv[i] == 0:
#			return False
#	return True

f1 = 1
f2 = 2
c = pow(10,14)
d = 4
sqfr = 3
MAXPRIME = sqrt(pow(10,8))
f1 = 3
fA = 3.0
fB = 2.0
pwr = 0


while(True):
#	print "squareFree: {}, f: {}".format(findDivisors(f1),f1)
#	squareFree = isSquareFree(d)
#	if squareFree:
#		sqfr += 1
#		print "nr: {}, squareFree: {}, f: {}, ff:{:e}, fff:{}".format(d,squareFree,f1,f1,f1%pow(10,16))
#	else:
#		print "nr: {}, squareFree: {}, f: {}, ff: {:e}, fff:{}".format(d,squareFree,f1,f1,f1%pow(10,16))
#	if sqfr == pow(10,8):
#		print "fibo nr: {}".format(d)
#		print "nr: {}, squareFree: {}, f: {}, ff: {}".format(d,squareFree,fA,f1%pow(10,16))
#		break
#	if sqfr == 200:
#		print "{:e}".format(f1)
#		break
	if d%pow(10,6) == 0:
		print "{} millions(s)!".format(d/pow(10,6))
	if (d == 130775524): #110629224): #130772972): #130772669): #130772672
		print "NR: {}".format(d)
		print f1
		print "floating {} with power {}".format(fA,pwr)
		break
##	if (d == 130772677):
##		break
##	if (d == 260):
##		print f1
##		print "floating {} with power {}".format(fA,pwr)
##		print "integer {} with power {}".format(fX,power)
	if len(fiboInd) != len(primes):
#		findDivisors(f1,d)
		temp = f2
		f2 = f1
		f1 = (temp + f2)%pow(10,16)
		
		tempF = fB
		fB = fA
		fA = (tempF+ fB)
		if fA > 10:
			fA /= 10.0
			fB /= 10.0
			pwr += 1
		
	d += 1
