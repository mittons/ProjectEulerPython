from math import log10

oddDigits = [0,9,8,7,6,5,4,3,2,1]

	
pow10 = [pow(10,i) for i in xrange(20)]
#digits stands for (nr of digits in number - 1)
def recursion(n,digits):
	if n<=1999999999: #squaredN<=1929394959697989990:
		if digits % 2 == 1:
			squaredN = pow(n,2)
			if digits == 9:
#				print n
				for i in xrange(5):
#					print "{}: {}".format(n, i)
					if int(squaredN/pow10[10+(i*2)]) % 10 != oddDigits[5+i]:
						return
				print n
				return
			if int(squaredN/pow10[digits+1]) % 10 != oddDigits[(digits+1)/2]:	
				return
		
		for j in xrange(10):
			recursion((j*pow(10,digits+1))+n,digits+1)
	

for i in xrange(1,10):
	recursion(10*i, 1)
