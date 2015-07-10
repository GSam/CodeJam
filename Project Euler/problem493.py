import math
cache = [math.factorial(10)/(math.factorial(x) * math.factorial(10-x)) for x in xrange(11)]
total = 0
m = 0
coef = math.factorial(70)/(math.factorial(20) * math.factorial(50))


for a in xrange(11):
    colora = 0 if a == 0 else 1
    for b in xrange(11):
        colorb = colora if b == 0 else colora+1
        for c in xrange(11):
            colorc = colorb if c == 0 else colorb+1
            for d in xrange(11):
                colord = colorc if d == 0 else colorc+1
                for e in xrange(11):
                    colore = colord if e == 0 else colord+1
                    for f in xrange(11):
                        colorf = colore if f == 0 else colore+1
                        for g in xrange(11):
                            colorg = colorf if g == 0 else colorf+1
                            if (a+b+c+d+e+f+g) != 20:
                                continue
                            total += colorg * (cache[a] * cache[b] * cache[c] * cache[d] * cache[e] * cache[f] * cache[g]*1.0)/coef
                            m += (cache[a] * cache[b] * cache[c] * cache[d] * cache[e] * cache[f] * cache[g]*1.0)/coef
