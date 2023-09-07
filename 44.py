isPen = [0]*30000000
pen = []
p = 1
n = 1
while p < 30000000:
    isPen[p] = 1
    pen.append(p)
    n += 3
    p += n
D = 100000000
Pj = 0
Pk = 0

b = 0
c = 0

pmax = pen[-1]

for n in xrange(1,len(pen)):
    for j in xrange(len(pen)-n):
        p1 = pen[j]
        p2 = pen[j+n]
        if p2+p1 > pmax:
            break
        if p2-p1 > D:
            break
        if isPen[p2+p1] and isPen[p2-p1]:
            if p2-p1 < D:
                Pj = j
                Pk = j+n
                D = p2-p1

print D


