from usefulStuff import *

panDigitals = []
thePanDigital = [1,2,3,4,5,6,7,8,9]
for i in xrange(2,5):
	normDigCount = 9/i
	offsCount = 9%normDigCount
	multRange = range(1, i+1-offsCount)
	offsMultRange = range(1+i-offsCount, i+1)
	x = 1
	xList = [1]
	while len(xList)<normDigCount:
		x+=1
		xList = intToList(x)
	if len(offsMultRange)>0:
		while len(intToList(x*offsMultRange[0]))<normDigCount+1:
			x+=1
		xList = intToList(x)
	while len(xList)==normDigCount:
		pD = []
		pCp = []
		for j in multRange:
			pD += intToList(j*x)	
			pCp += intToList(j*x)
		for j in offsMultRange:
			pD += intToList(j*x)
			pCp += intToList(j*x)
		pD.sort()
		if pD == thePanDigital:
			panDigitals.append(pCp)
		x+=1
		xList = intToList(x)

panDigitals.sort()
print panDigitals
