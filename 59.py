f = file('in_59/cipher59.txt','r')
l = f.readline()
l = l.split(',')
l = map(lambda x: int(x), l)
patterns = []
combos = []
for i in xrange(len(l)-2):
	pattern = l[i:i+3]
	if pattern not in patterns:
		patterns.append(pattern)
	combos.append(pattern)
for pattern in patterns:
	if combos.count(pattern) > 3:
		indexes = []
		for i in xrange(len(combos)):
			if pattern == combos[i]:
				indexes.append(i)
		print "pattern: {}, count: {}, indexes: {}".format(pattern, combos.count(pattern), indexes)

a = [0]*256
b = [0]*256
c = [0]*256
for i in xrange(len(l)/3):
	a[l[i*3-2]] += 1
	if len(l)>(i*3)-1:
		b[l[i*3-1]] += 1	
	if len(l)>i*3:
		c[l[i*3]] += 1

tuples = []
tuples2 = []
tuples3 = []
for i in xrange(len(a)):
	if a[i] > 0:
		tuples.append((a[i], i))
	if b[i] > 0:
		tuples2.append((b[i], i))
	if c[i] > 0:
		tuples3.append((c[i], i))

tuples.sort()
tuples2.sort()
tuples3.sort()

print tuples
print tuples2
print tuples3

chars = []
asciiVals = []
for i in xrange(len(l)):
	if i%3 == 0:
		chars.append(chr(l[i]^ord('g')))	
		asciiVals.append(l[i]^ord('g'))
	elif i%3 == 1:
		chars.append(chr(l[i]^ord('o')))
		asciiVals.append(l[i]^ord('o'))
	elif i%3 == 2:
		chars.append(chr(l[i]^ord('d')))
		asciiVals.append(l[i]^ord('d'))

print type("y")(chars)
print sum(asciiVals)
