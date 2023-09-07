from usefulStuff import *
from math import sqrt
from collections import deque

def createNext3((c,b,a)):
	rt = [(2*a-2*b+3*c, 2*a-b+2*c, a-2*b+2*c)]
	rt.append((-2*a+2*b+3*c, -2*a+b+2*c, -a+2*b+2*c))
	rt.append((2*a+2*b+3*c, 2*a+b+2*c, a+2*b+2*c))
	return rt


maxC = pow(10,11)#38000000#pow(10,7)#38000000#pow(10,11)+1#38000000#pow(10,11)+1

primesBool = sieve(int((maxC/(5**3*13**2)))+2)
#print len(primesBool), int(maxC/5**3/13**2)+1
primes = []

for i in xrange(1,((len(primesBool)-2)/4)+1):
	idx = 4*i+1
	if primesBool[idx] == 1:
		primes.append(idx)
primes2 = []
for i in xrange(0,int((int(maxC/5**3/13**2)-3)/4)+1):
	idx = 4*i+3
	if primesBool[idx] == 1:
		primes2.append(idx)


print "snice"
s = 0

l = len(primes)
l2 = len(primes2)
#Use this to find the sum every number under maxC that has n as a factor and the any combination of primes of the form 4k+3
def findMore(n,lastI):
	su = 0
	for i in xrange(lastI,l2):
		c = primes2[i]*n
		if c<maxC:
#			x.append(c)
			su += c
			su += findMore(c,i)
		else:
			break
	return su


for i in xrange(l):
	q1 = primes[i]**7
	if q1<maxC:
		for j in xrange(l):
			if j!=i:
				q2 = q1*(primes[j]**3)
				if q2<maxC:
#					print q2
					s += q2
					s += findMore(q2,0)
					q2x2 = q2*2 
					while(q2x2<maxC):
#						print q2x2
						s += q2x2
						s += findMore(q2x2,0)
						q2x2 *= 2
				else:
					break	
	else:
		break

print "one down", s

for i in xrange(l):
	q1 = primes[i]**10
	if q1<maxC:
		for j in xrange(l):
			if j!=i:
				q2 = q1*(primes[j]**2)
				if q2<maxC:
					s += q2
					s += findMore(q2,0)
					q2x2 = q2*2 
					while(q2x2<maxC):
						s += q2x2
						s += findMore(q2x2,0)
						q2x2 *= 2
				else:
					break	
	else:
		break

x = []

print "two down", s

for i in xrange(l):
	q1 = primes[i]**3
	if q1<maxC:
		for j in xrange(l):
			if j!=i:
				q2 = q1*(primes[j]**2)
				if q2<maxC:
					for k in xrange(l):
						if k!=j and k!=i:
							q3 = q2*primes[k]
							if q3<maxC:
#								x.append(q3)							
								s += q3
								s += findMore(q3,0)
								q3x2 = q3*2 
								while(q3x2<maxC):
#									x.append(q3x2)
									s+=q3x2
									s += findMore(q3x2,0)
									q3x2 *= 2
							else:
								break	
				else:
					break
	else:
		break

#x.sort()
#for i in x:
#	print i
print "Svo er thetta bara buid:"
print s
