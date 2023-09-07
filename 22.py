f = open("names22.txt", 'r')

nameString = ""
for line in f:
	nameString = line

names = nameString.split(',')

names = map(lambda x: x[1:-1], names)
names.sort()

chars = []
for i in xrange(1,27):
	chars.append([chr(64+i),i])
charValues = dict(chars)

values = map(lambda name: sum(map(lambda char: charValues.get(char),name)) ,names)

print sum(map(lambda i:(i+1)*values[i], xrange(len(values))))


