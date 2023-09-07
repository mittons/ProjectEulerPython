"""
1 1 1 1
1 1 2
1 3
2 2
4

1 1 1
1 2
3

1 1
2

1
"""
from collections import defaultdict

pValues = defaultdict(list)#lambda: defaultdict(int))
"""
for n in xrange(1,100):
    pValues[n][k]
    m = 0  
    for i in xrange(1, (n/2)+1):
        99 1
        98 2
        98 1 1
        97 3
        97 2 1
        97 1 1 1
        96 4
        96 3 1
        96 2 1 1
        96 1 1 1 1
        96 5
        96 2 2
        95 5 

"""
def p_helper(k, n, debug = None):
    pVals = pValues
    if n in pVals:
        if k in pVals[n]:
            if debug != None:
                print debug
            return pVals[n][k]
    
    if k > n:
        return 0
    elif k == n:
        pValues[n][k] = 1
        return 1
    else:
        print "that {} {}:".format(n, k)
        #Section a
        pValues[n][k] = p_helper(k+1, n) + p_helper(k, n-k, "this {} {}".format(k, n-k))
        return pValues[n][k]

i = 1
while i < 251:
#for i in xrange(1, 10):
    last = 1
    lis = [0]*(i+1)
    lis[i] = last
    for j in xrange(1,i):
        #Section a
#        print "XXthatXX {} {}:".format(i, i-j)
        k = i-j
        if i-k >= k:
            last += pValues[i-k][k]
        else:
            last += 0
        lis[i-j] = last

    pValues[i] = lis

    print pValues[i][1]
    if pValues[i][1] % pow(10,6) == 0:
        break
    else:
        i += 1
    print i

#print i
#print pValues[i][1]
#print i
print pValues
#Let p(n) represent the number of different ways un which n coins can be seoarated into piles. For example, five coins can be separated into piles in exactly seven different ways so p(5)=7.

#def p(n):
#    return 1 +  sum(map(lambda k: p_helper(k, n-k), xrange(1,((n/2)+1))))

#i = 3
#while p(i) % pow(10,6) != 0:
   # print p(i)
  #  i += 1
 #   print i
#print i
