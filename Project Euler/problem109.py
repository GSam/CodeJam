distinct = set()

base = [str(x) for x in xrange(1,21)]

for hit1 in [None, 'B', 'DB'] + ['S' + str(x) for x in base] + ['D' + str(x) for x in base] + ['T' + str(x) for x in base]:
    for hit2 in [None, 'B', 'DB'] + ['S' + str(x) for x in base] + ['D' + str(x) for x in base] + ['T' + str(x) for x in base]:
        for hit3 in [None, 'DB'] + ['D' + str(x) for x in base]:
            group = []
            if hit1:
                group.append(hit1)
            if hit2:
                group.append(hit2)
            if hit3:
                group.append(hit3)
                

            # must have a group
            if len(group) < 1:
                continue

            # must have an ending double
            if not group[-1].startswith('D'):
                continue
            
            # sort the first 'two' elements
            group[:-1] = list(sorted(group[:-1]))

            distinct.add(tuple(group))

# length of distinct should be 42336
print len(distinct)

count = 0
# not the most efficient way, but hey, we only have 40,000 things to iterate
for x in distinct:
    tot = 0
    for y in x:
        mult = 1
        if y[0] == 'D':
            mult = 2
        elif y[0] == 'T':
            mult = 3
            
        if y[-1] == 'B':
            tot += mult * 25
        else:
            tot += mult * int(y[1:])
    if tot < 100:
        count += 1

print 'Count:', count
            
