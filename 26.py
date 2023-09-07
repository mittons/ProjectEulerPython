maxCycle = 1
maxCycleDenominator = 1
for i in xrange(2,1000):
    fractionDigits = []
    formerNumerators = []
    currNumerator = 10
    while currNumerator not in formerNumerators:
        formerNumerators.append(currNumerator)
        if i > currNumerator:
            currNumerator *= 10
            fractionDigits.append(0)
        else:
            fractionDigits.append(int(currNumerator/i))
            currNumerator %= i
            if currNumerator == 0:
                formerNumerators.append(0)
                break
            currNumerator *= 10
    if currNumerator != 0:
        currCycleLength = len(formerNumerators)-formerNumerators.index(currNumerator) 
        if maxCycle < currCycleLength:
            maxCycle = currCycleLength
            maxCycleDenominator = i
            print "{} has a cycle of length {}".format(i,len(formerNumerators)-formerNumerators.index(currNumerator))
            print "Fraction digits are {}".format(fractionDigits)
            print "The cycle is {}".format(fractionDigits[formerNumerators.index(currNumerator):])
            print "The first recurring numerator is {}".format(currNumerator)
            print "" 

print "The longest cycle is of length {} and belongs to the inverse of {}".format(maxCycle, maxCycleDenominator)
