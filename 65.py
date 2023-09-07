from usefulStuff import *
constants = reduce(lambda x,y: x+y, [[1,2*(i+1),1] for i in xrange(33)])

print constants

constants.reverse()

numerator = 0
denominator = 1

for k in constants:
	numerator += (k * denominator)
	temp = denominator
	denominator = numerator
	numerator = temp

numerator += 2*denominator

print "At the 100th convergent the numerator is {} and denominator is {}".format(numerator, denominator)
print "e is numerator/denominator = {}".format(float(numerator)/denominator)
print "the sum of the digits in the numerator is {}".format(sum(intToList(numerator)))
