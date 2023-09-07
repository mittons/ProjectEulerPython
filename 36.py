from math import log,log10


def logHouse(number, base):
	if base == 10:
		return log10(number)
	else:
		return log(number, base)

#def ifBinPalindrome(n):
def isBasePalindrome(n,base):
	length = int(logHouse(n,base))
	for i in xrange(int((length+1)/2)):
		if ((n/pow(base,i))%base) != ((n/pow(base,length-i))%base):
			return False
	return True

def prob36(n):
	s = 0
	for i in xrange(1,n+1):
		if (isBasePalindrome(i,10) and isBasePalindrome(i,2)):
			s += i
	print s

prob36(pow(10,6)-1)
