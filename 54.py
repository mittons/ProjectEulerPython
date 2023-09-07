def parseCard(card):
        value = card[0]
        sort = card[1]
        if not value.isdigit():
                if value == 'T':
                        value = 10
                elif value == 'J':
                        value = 11
                elif value == 'Q':
                        value = 12
                elif value == 'K':
                        value = 13
                elif value == 'A':
                        value = 14
        else:
                value = int(value)
        return {"value":value, "sort":sort}

def parseHand(hand):
        l = []
        for card in hand:
              l.append(parseCard(card))
        return l

def isFlush(hand):
        firstSort = hand[0]["sort"]
        for i in range(1, len(hand)):
                if not firstSort == hand[i]["sort"]:
                        return False
        return True

def straightHelper(values):
        for i in range(len(values) - 1):
                if values[i+1] - values[i] != 1:
                        return False
        return True
                
def isStraight(hand):
        h = map(lambda x: x["value"], hand)
        h.sort()
        if straightHelper(h[0:4]):
                if h[4] - h[3] == 1:
                        return True
                elif h[3] == 5 and h[4] == 14:
                        return True
        return False

def isRoyal(straightHand):
        h = map(lambda x: x["value"], straightHand)
        h.sort()
        return h[0] == 10

#returns how many times each distinct value in the hand appears
def distinctValueRecurrence(hand):
        h = map(lambda x: x["value"], hand)
        h.sort()
        l = []
        i = 0
        while i < 5:
                duplCount = h.count(h[i])
                l.append(duplCount)
                i += duplCount
        return l


def rankHand(hand):
        maxRank = 0
        if isStraight(hand):
                if isFlush(hand):
                        if isRoyal(hand):
                                return 9
                        else:
                                return 8
                maxRank = 4
        valueRecur = distinctValueRecurrence(hand)
        maxValRecur = max(valueRecur)
        if maxValRecur == 4:
                return 7
        if maxValRecur == 3:
                if len(valueRecur) == 2:
                        return 6
                maxRank = 3
        if isFlush(hand):
                return 5
        if maxRank != 0:
                return maxRank
        pairCount = valueRecur.count(2)
        return pairCount


#returns true if hand0 wins
def breakHighCardTie(hand0, hand1):
        h0 = map(lambda x: x["value"], hand0)
        h1 = map(lambda x: x["value"], hand1)
        h0.sort()
        h1.sort()
        for i in xrange(len(h0)):
                if h0[4-i] > h1[4-i]:
                        return True
                elif h0[4-i] < h1[4-i]:
                        return False        


#returns true if hand0 wins
def breakPairTie(hand0, hand1):
        h0 = map(lambda x: x["value"], hand0)
        h1 = map(lambda x: x["value"], hand1)
        h0.sort()
        h1.sort()
        pairVal0 = 0
        pairVal1 = 0
        for c in h0:
                if h0.count(c) == 2:
                        pairVal0 = c
        for c in h1:
                if h1.count(c) == 2:
                        pairVal1 = c
        if pairVal0 == pairVal1:
                return breakHighCardTie(hand0, hand1)
        else:
                return pairVal0 > pairVal1

def breakTie(hand0, hand1, rank):
        if (rank == 0):
                return breakHighCardTie(hand0, hand1)
        elif (rank == 1):
                return breakPairTie(hand0, hand1)
        else:
                print rank
                return True

def isFirstHandWinner(hand0, hand1):
        rank0 = rankHand(hand0)
        rank1 = rankHand(hand1)
##        print "hand0: {}, hand1: {}".format(rank0, rank1)        
        if (rank0 > rank1):
                return True
        elif (rank0 < rank1):
                return False
        else:
                return breakTie(hand0, hand1, rank0)
f = open("poker54.txt", 'r')
playerOneWinCount = 0
for line in f:
        l = line[0:-1].split(' ')
##l = ["AC", "AH", "KH", "JH", "TH", "AS", "QS", "AS", "JS", "TC"]
        p1 = l[0:5]
        p2 = l[5:10]
##print "player 1: {}, player 2: {}".format(p1, p2)
        playerOneWins = isFirstHandWinner(parseHand(p1), parseHand(p2))
        if (playerOneWins):
                playerOneWinCount += 1
print playerOneWinCount
