
def cardsInPrevRoom(n,C):
	if n == 1:
		return 2
	#The magic number. (This is used heavily, why not only calculate it once?)
	C0 = C-2
	#Ferry trips cost ((n-2)/C0)*C cards
	#The final trip costs ((n-2)%C0)+3 cards
	return ((n-2)/C0)*C + ((n-2)%C0)+3

R = 30
s = 0

for C in xrange(3,41):
	#We calculate this dynamically from the last room to the first room.

	#The index of the room currently being calculated
	R0 = R

	#The cards we need to be able to get into the next room with enough cards inside that room. This is 1 in the last room.
	n0 = 1
	
	while R0 > 0:
		n0 = cardsInPrevRoom(n0,C)
		R0 -= 1
		
	s+= n0

print s
