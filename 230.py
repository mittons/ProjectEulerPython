from usefulStuff import *

a =1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
b =8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

a = intToList(a)
b = intToList(b)

D = lambda n: (127+19*n)*7**n


fibo = [1,2]
while fibo[-1]<D(17):
	fibo.append(fibo[-1]+fibo[-2])
fibo.reverse()


l = len(fibo)

s = 0
for i in xrange(18):
	d = D(i)-1
	df = (d/100)+1
	dpi = d%100
	if df == 0:
		s += (10**i)*a[dpi]
	else:
		fl = 0
		while df>2:
			while fibo[fl]>df:
				fl += 1
			df %= fibo[fl]
		if (fl%2 == 0 and df == 1) or (fl%2 == 1 and df == 2):
			s += (10**i)*a[dpi]
		else: #if complement of the if or df == 0:
			s += (10**i)*b[dpi]

print s
