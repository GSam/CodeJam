import math

last = 0
last2 = 1
count = 0
while(True):
    prev = last2
    last2 = last2 + last
    last = prev
    last2 %= 10 ** 9
    count += 1
    
    val = prev
    val2 = prev % 10 ** 9
    if val < 100000000:
        continue
    temp = count * 0.20898764024997873 - 0.3494850021680094
    val = int( pow( 10, temp - int( temp ) + 9 - 1 ) )

    set1 = set()
    set2 = set()
    while val >= 1:
        set1.add(val % 10)
        val /= 10
    while val2 >= 1:
        set2.add(val2 % 10)
        val2 /= 10
    if len(set1) == 9 and len(set2) == 9 and 0 not in set1 and 0 not in set2:
        print prev, count
        break
