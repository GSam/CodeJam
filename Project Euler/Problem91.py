# Lazy brute force - Takes about 15-20 seconds

import itertools
maxX = 50
maxY = 50

def calc_lengths(pair):
    temp = []
    a,b = pair
    temp.append((a[0]**2 + a[1]**2)**0.5)
    temp.append((b[0]**2 + b[1]**2)**0.5)
    temp.append(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)
    return sorted(temp) 
    
all = []
count = 0
for x in range(maxX+1):
    for y in range(maxY+1):
        if (x == 0 and y == 0):
            continue
        all.append((x,y))

for pair in list(itertools.combinations(all,2)):
    if pair[0][0] == pair[1][0] == 0:
        continue
    if pair[0][1] == pair[1][1] and pair[0][1] == 0:
        continue
    a,b,c = calc_lengths(pair)
    if (abs((a ** 2 + b ** 2) -c ** 2) < 0.0000001):
        count += 1

print count 
