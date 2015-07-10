import math
visited = set()
repunits = set()

for x in xrange(2, 10**6):
    orig = 1
    while True:
        if orig > 10 ** 12:
            break
        if orig in visited and not orig in repunits:
            repunits.add(orig)
        elif x + 1 != orig and orig not in visited:
            visited.add(orig)
            
        orig = orig * x + 1
