norm = [0,31,59,90,120,151,181,212,243,273,304,334]
leap = [0,31,60,91,121,152,182,213,244,274,305,335]
sun = 5
normFirst = [n%7 for n in norm]
leapFirst = [l%7 for l in leap]

count = 0
for i in xrange(1,101):
	if (i % 4 != 0):
		for j in normFirst:
			if j == sun:
				count += 1
		sun -= 1
		sun %= 7
	else:
		for j in leapFirst:
			if j == sun:
				count += 1
		sun -= 2
		sun %= 7
print count
