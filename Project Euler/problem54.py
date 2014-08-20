from collections import Counter
import requests

ranking = ['high', 'pair', '2pair', '3kind', 'straight', 'flush', 'fullhouse', '4kind', 'straightflush', 'royal']
translate = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
counts = None

def comp(a,b):
    global counts
    if (counts.get(a) != counts.get(b)):
        return counts.get(a) - counts.get(b)
    return translate[a] - translate[b]

def determine(hand):
    global counts
    listH = [x[0] for x in hand]
    setH = set(listH)
    value = set([translate[x[0]] for x in hand])
    setS = set([x[1] for x in hand])
    if (len(setH.intersection(set(['T','J','Q','K','A']))) == 5 and len(setS) == 1):
        return 'royal', 14
    straight = False
    flush = False
    counts = Counter(listH)
    if (len(setS) == 1):
        flush = True
    if (max(value) - min(value) == 4 and max(counts.itervalues()) == 1):
        straight = True
    if (flush and straight):
        return 'straightflush', max(value)
    if (flush):
        return 'flush', max(value)
    if (straight):
        return 'straight', max(value)
    sortedCount = list(sorted(counts, cmp=comp, reverse=True))
    for i in range(len(sortedCount)):
        x = sortedCount[i]
        if counts[x] == 4:
            return '4kind', translate[x]
        elif counts[x] == 3:
            if counts[sortedCount[i+1]] == 2:
                return 'fullhouse', translate[x]
            return '3kind', translate[x]
        elif counts[x] == 2:
            if counts[sortedCount[i+1]] == 2:
                return '2pair', translate[x]
            return 'pair', translate[x]
        else:
            return 'high', translate[x]

def compare(hand1, hand2):
    type1 = determine(hand1)
    type2 = determine(hand2)
    print type1, type2
    if (ranking.index(type1[0]) == ranking.index(type2[0])):
        if (type1[1] == type2[1]):
            sorted1 = sorted([translate[x[0]] for x in hand1],reverse=True)
            sorted2 = sorted([translate[x[0]] for x in hand2],reverse=True)
            for i in range(5):
                if (sorted1 > sorted2):
                    return -1
                elif (sorted2 > sorted1):
                    return 1
        else:
            return type2[1] - type1[1]
    else:
        return ranking.index(type2[0]) - ranking.index(type1[0])

text = open("p054_poker.txt",'r').readlines()
count = 0
for x in text:
    a,b,c,d,e,f,g,h,i,j = x.split()
    print x.strip()
    bb = compare([a,b,c,d,e], [f,g,h,i,j])
    count += 1 if bb < 0 else 0
