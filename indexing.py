fo = open("./1.txt", "r")
text = fo.read()
fo.close()
fo = open("./2.txt", "r")
text = text+fo.read()
fo.close()
fo = open("./3.txt", "r")
text = text+fo.read()
fo.close()

lines = text.splitlines()
print(len(lines)*12)
words = []
words1 = []
words2 = []
words3 = []
words4 = []
words5 = []
words6 = []
words7 = []
words8 = []
words9 = []
words10 = []
words11 = []
words12 = []
for line in lines:
    b = line.split(" ")
    words1.append(b[0])
    words2.append(b[1])
    words3.append(b[2])
    words4.append(b[3])
    words5.append(b[4])
    words6.append(b[5])
    words7.append(b[6])
    words8.append(b[7])
    words9.append(b[8])
    words10.append(b[9])
    words11.append(b[10])
    words12.append(b[11])

    for m in b:
        words.append(m)

wroddict = {}
firstdict={}

for word in words:
    k = 0
    c = words.count(word)
    wroddict[word] = c
    while k < c:
        words.remove(word)
        k = k+1
for word in words1:
    k = 0
    c = words1.count(word)
    firstdict[word] = c
    while k < c:
        words1.remove(word)
        k = k+1


sortedwords = sorted(wroddict.items(), key=lambda x: x[1], reverse=True)
sortedfirstdict = sorted(firstdict.items(), key=lambda x: x[1])

fo = open("./4.json", "w")

for word in sortedwords:
    fo.write(word[0])
    fo.write(',')


