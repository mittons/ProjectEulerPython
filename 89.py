f = open('in_89/roman89.txt','r')
from collections import deque

#Roman digits
rd = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
rn = ['I','V','X','L','C','D','M']
rs = [1,10,100]
rl = {1:[5,10],10:[50,100],100:[500,1000]}
def getVal(rs):
	prev = 0
	val = 0
	sub = False
	for i in rs:
		curr = rd[i]
		if prev == 0:
			prev = curr
			continue
		if curr>prev:
#			print curr,prev
			val = val+curr-prev
			prev = 0
		else:
#			print prev
			val += prev
			prev = curr
	if prev != 0:
#		print prev
		val += prev
	return val



assert getVal("I") == 1
assert getVal("IV") == 4
assert getVal("IX") == 9
assert getVal("MDCVI") == 1606
assert getVal("MCCCCCCVI") == 1606
assert getVal("MMXII") == 2012


def getShortestRomanL(num):
	Q = deque([])
	currN = 0
	currL = 0
	currR = 1000
	currO = []
	while(True):
		if currN < num:
#			print "A",currN,currO
			if 1000+currN < num:
				Q.append((1000+currN,currL+1,1000,[1000]+currO))
			else:
				for i in xrange(len(rn)):
					if rd[rn[i]] > currR:
						if i != 0:
							Q.append((rd[rn[i-1]]+currN,currL+1,rd[rn[i-1]],currO+[rd[rn[i-1]]]))
						break
					if rd[rn[i]]+currN == num:
						print currO+[rd[rn[i]]]
						return currL+1
					if rd[rn[i]]+currN > num:
#						print "xx",rd[rn[i]]+currN
						Q.append((rd[rn[i]]+currN,currL+1,rd[rn[i]],currO+[rd[rn[i]]]))
						if i != 0:
							Q.append((rd[rn[i-1]]+currN,currL+1,rd[rn[i-1]],currO+[rd[rn[i-1]]]))
#						print Q
						break
		elif currN > num:
#			print "B",currN
			for i in [1,10,100]:
				if currR in rl[i]:
#					print currR, currO
					if currN-i == num:
						print currO[:-1]+[i]+[currO[-1]]
						return currL+1
					elif currN-i < num:
						Q.append((currN-i,currL+1,currR,currO[:-1]+[i]+[currO[-1]]))
						break
		n = Q.popleft()
		currN = n[0]
		currL = n[1]
		currR = n[2]
		currO = n[3]

s = 0
for line in f:
	if '\n' in line:
		s += len(line[:-1])-getShortestRomanL(getVal(line[:-1]))
	else:
		s += len(line)-getShortestRomanL(getVal(line))

print s
