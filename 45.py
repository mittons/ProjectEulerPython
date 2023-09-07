t = 285
p = 165
h = 143
tn = lambda n:(n*(n+1))/2
pn = lambda n:(n*((3*n)-1))/2
hn = lambda n: n*((2*n)-1)

currt = tn(t)
currp = pn(p)
currh = 1

while(currt != currp or currt != currh):
	if currh < currp:
		h += 1
		currh = hn(h)
	elif currp < currt:
		p += 1
		currp = pn(p)
	else:
		t += 1
		currt = tn(t)

print "t:{} tn:{}, p:{} pn:{}, h:{} hn{}".format(t, currt, p, currp, h, currh)
