
isBouncy = [0]*10000000


#bounceFactor: 0 if undefined, 1 if bouncy, 2 if inc, 3 if decr
def generateBouncy(n, bounceFactor, d):
    if d == 0:
        return
    else:
        if bounceFactor == 0:
            piv = n % 10
            for i in xrange(0,piv):
                 generateBouncy(n*10+i, 3, d-1)
            generateBouncy(n*10+piv, 0, d-1)
            for i in xrange(piv+1, 10):
                 generateBouncy(n*10+i, 2, d-1)
        
        elif bounceFactor == 1:
            for i in xrange(10):
                x = n*10+i
                isBouncy[x] = 1
                generateBouncy(x, 1, d-1)

        elif bounceFactor == 2:
            piv = n % 10
            for i in xrange(0,piv):
                x = n*10+i
                isBouncy[x] = 1
                generateBouncy(x, 1, d-1)

            for i in xrange(piv,10):
                generateBouncy(n*10+i, 2, d-1)

        elif bounceFactor == 3:
            piv = n % 10
            for i in xrange(0,piv+1):
                generateBouncy(n*10+i, 3, d-1)

            for i in xrange(piv+1,10):
                x = n*10+i
                isBouncy[x] = 1
                generateBouncy(x, 1, d-1)

for i in xrange(1,10):
    generateBouncy(i, 0, 6) 

print isBouncy[10**6:10**6+50]

bouncy = 0.0
for i in xrange(1, 10**7):
    if isBouncy[i] == 1:
        bouncy += 1
        if bouncy/i >= 0.99:
            print i
            break
