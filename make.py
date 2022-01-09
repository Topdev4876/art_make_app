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
dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}
dict6 = {}
dict7 = {}
dict8 = {}
dict9 = {}
dict10 = {}
dict11 = {}
dict12 = {}
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
for word in words1:
    k = 0
    c = words1.count(word)
    dict1[word] = c
    while k < c:
        words1.remove(word)
        k = k+1
for word in words2:
    k = 0
    c = words2.count(word)
    dict2[word] = c
    while k < c:
        words2.remove(word)
        k = k+1
for word in words3:
    k = 0
    c = words3.count(word)
    dict3[word] = c
    while k < c:
        words3.remove(word)
        k = k+1
for word in words4:
    k = 0
    c = words4.count(word)
    dict4[word] = c
    while k < c:
        words4.remove(word)
        k = k+1
for word in words5:
    k = 0
    c = words5.count(word)
    dict5[word] = c
    while k < c:
        words5.remove(word)
        k = k+1
for word in words6:
    k = 0
    c = words6.count(word)
    dict6[word] = c
    while k < c:
        words6.remove(word)
        k = k+1
for word in words7:
    k = 0
    c = words7.count(word)
    dict7[word] = c
    while k < c:
        words7.remove(word)
        k = k+1
for word in words8:
    k = 0
    c = words8.count(word)
    dict8[word] = c
    while k < c:
        words8.remove(word)
        k = k+1
for word in words9:
    k = 0
    c = words9.count(word)
    dict9[word] = c
    while k < c:
        words9.remove(word)
        k = k+1
for word in words12:
    k = 0
    c = words12.count(word)
    dict12[word] = c
    while k < c:
        words12.remove(word)
        k = k+1
for word in words10:
    k = 0
    c = words10.count(word)
    dict10[word] = c
    while k < c:
        words10.remove(word)
        k = k+1
for word in words11:
    k = 0
    c = words11.count(word)
    dict11[word] = c
    while k < c:
        words11.remove(word)
        k = k+1
a1 = []
for item in dict1:
    if dict1.get(item)!=1:
        a1.append(item)
a2 = []
for item in dict2:
    if dict2.get(item)!=1:
        a2.append(item)
a3 = []
for item in dict3:
    if dict3.get(item)!=1:
        a3.append(item)

a4 = []
for item in dict4:
    if dict4.get(item) != 1:
        a4.append(item)
a5 = []
for item in dict5:
    if dict5.get(item) != 1:
        a5.append(item)
a6 = []
for item in dict6:
    if dict6.get(item) != 1:
        a6.append(item)
a7 = []
for item in dict7:
    if dict7.get(item) != 1:
        a7.append(item)
a8 = []
for item in dict8:
    if dict8.get(item) != 1:
        a8.append(item)
a9 = []
for item in dict9:
    if dict9.get(item) != 1:
        a9.append(item)
a10 = []
for item in dict10:
    if dict10.get(item) != 1:
        a10.append(item)
a11 = []
for item in dict11:
    if dict11.get(item) != 1:
        a11.append(item)
a12 = []
for item in dict12:
    if dict12.get(item) != 1:
        a12.append(item)


sortedwords1 = sorted(dict1.items(), key=lambda x : x[1], reverse=True)
sortedwords2 = sorted(dict2.items(), key=lambda x : x[1], reverse=True)
sortedwords3 = sorted(dict3.items(), key=lambda x : x[1], reverse=True)
sortedwords4 = sorted(dict4.items(), key=lambda x : x[1], reverse=True)
sortedwords5 = sorted(dict5.items(), key=lambda x : x[1], reverse=True)
sortedwords6 = sorted(dict6.items(), key=lambda x : x[1], reverse=True)
sortedwords7 = sorted(dict7.items(), key=lambda x : x[1], reverse=True)
sortedwords8 = sorted(dict8.items(), key=lambda x : x[1], reverse=True)
sortedwords9 = sorted(dict9.items(), key=lambda x : x[1], reverse=True)
sortedwords10 = sorted(dict10.items(), key=lambda x : x[1], reverse=True)
sortedwords11 = sorted(dict11.items(), key=lambda x : x[1], reverse=True)
sortedwords12 = sorted(dict12.items(), key=lambda x : x[1], reverse=True)

print (len(a1))
print (len(a3))
print (len(a2))
print (len(a4))
print (len(a5))
print (len(a6))
print (len(a7))
print (len(a8))
print (len(a9))
print (len(a10))
print (len(a11))
print (len(a12))






# print(sortedwords1)
# print(sortedwords2)
# print(sortedwords3)
# print(sortedwords4)
# print(sortedwords5)
# print(sortedwords6)
# print(sortedwords7)
# print(sortedwords8)
# print(sortedwords9)
# print(sortedwords10)
# print(sortedwords11)
# print(sortedwords12)

# a=0
# for word1 in sortedwords1:
#     filename = "./"+word1[0]+".txt"
#     fo = open(filename, "x")
#     fo.close()
#     fo = open(filename, "w")
#     word1_sum = word1[0]+" "
#     a = a + 1
#     print(a)
#     for word2 in sortedwords2:
#         word2_sum = word1_sum+word2[0]+" "
#         for word3 in sortedwords3:
#             word3_sum = word2_sum+word3[0]+" "
#             for word4 in sortedwords4:
#                 word4_sum = word3_sum+word4[0]+" "
#                 for word5 in sortedwords5:
#                     word5_sum = word4_sum+word5[0]+" "
#                     for word6 in sortedwords6:
#                         word6_sum = word5_sum + word6[0] + " "
#                         for word7 in sortedwords7:
#                             word7_sum = word6_sum+word7[0]+" "
#                             for word8 in sortedwords8:
#                                 word8_sum = word7_sum+word8[0]+" "
#                                 for word9 in sortedwords9:
#                                     word9_sum = word8_sum+word9[0]+" "
#                                     for word10 in sortedwords10:
#                                         word10_sum = word9_sum+word10[0]+" "
#                                         for word11 in sortedwords11:
#                                             word11_sum = word10_sum+word11[0]+" "
#                                             for word12 in sortedwords12:
#                                                 word12_sum = word11_sum + word12[0] + "\n"
#                                                 fo.write(word12_sum)
#
#     fo.close()
