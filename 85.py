#bring (n*(n+1))*(m*(m+1)) as close to 500000 as possible
bestOffset = 500000
bestI = 0
bestJ = 0
i = 1
j = 2828
while i<=j:
	curr = i*(i+1)*j*(j+1)
	offs = abs(8000000-curr)
	if bestOffset > offs:
		bestI = i
		bestJ = j
		bestOffset = offs
	if curr<8000000:
		i+=1
	else:
		j-=1

print bestI, bestJ, bestOffset
