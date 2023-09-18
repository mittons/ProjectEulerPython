from usefulStuff import *
f = open('in_79/keylog79.txt', 'r')

keys = []


l = f.readlines()
k = map(lambda x: intToList(int(x)), l)

keys = k[0]

checkFirst = True
while (checkFirst):
	checkFirst = False
	for key in k:
		if key[1] == keys[0]:
			keys = [key[0]] + keys
			checkFirst = True
			break

print keys

check = 0
while check < len(keys)-1:
	checkDone = True
	for key in k:
		if key[0] == keys[check] and key[2] == keys[check+1]:
			keys = keys[:check+1] + [key[1]] + keys[check+1:]
			checkDone = False
			break
	if checkDone:
		#print keys
		check += 1
	
print keys

checkLast = True
while (checkLast):
	checkLast = False
	for key in k:
		if key[1] == keys[-1]:
			keys = keys + [key[2]]
			checkLast = True
			break

print keys
