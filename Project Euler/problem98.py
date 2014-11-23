import itertools
import time
import math 
f = open("p098_words.txt", "r")
sortedList = {}

start = time.time()
for line in f.readline().split(","):
    word = line.strip('"')
    sword = "".join(sorted(word))
    if sword in sortedList:
        sortedList[sword].append(word)
    else:
        sortedList[sword] = [word]
        
last_dig = set(['2','3','7','8'])
largest = 0

for key in sortedList.keys():
    if len(sortedList[key]) <= 1:
        del sortedList[key]
        continue

    it = itertools.permutations('1234567890', len(key))
    for i in it:
        # key and i now form a mapping
        mapping = dict(zip(key, i))
        for c in itertools.combinations(sortedList[key], 2):
            # between every pair
            a = "".join([mapping[z] for z in c[0]])
            if a[0] == '0' or a[-1] in last_dig:
                continue
            a = int(a)
            b = "".join([mapping[z] for z in c[1]])
            if b[0] == '0' or b[-1] in last_dig:
                continue
            b = int(b)
            
            if (math.sqrt(a)) % 1 == 0 and (math.sqrt(b)) % 1 == 0:
                if a > largest:
                    largest = a
                    print mapping, key
                if b > largest:
                    largest = b
                    print mapping, key
        
print time.time() - start
