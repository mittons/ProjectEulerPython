f = open("words42.txt", "r")



isTri = [0]*1000
t = 1
n = 1
while t < 1000:
    isTri[t] = 1
    n += 1
    t += n

words = f.readline().split(",")
#wordValues = map(lambda word: sum(map(lambda letter: ord(letter)-64, word[1:-1])), words)
isTriWord = map(lambda word: isTri[sum(map(lambda letter: ord(letter)-64, word[1:-1]))], words)

triWordCount = sum(isTriWord)
print triWordCount
