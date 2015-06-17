from collections import defaultdict
import itertools
import time

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
    

start = time.time()

a = primes2(100000000+1)
b = set(a)

c = [-1 for x in xrange(100000000+1)]

answer = 0
for x in a:
    x = x - 1
    orig = x
    # Principle is that x - 1 must be prime
    # For any number:
    # 1+x, 2+x/2, 3+x/3 must be prime (assuming i | x)

    # May as well do the trivial i = 2,..,7 case
    if x % 2 == 0 and x/2 + 2 not in b:
        continue

    if x % 3 == 0 and x/3 + 3 not in b:
        continue

    if x % 5 == 0 and x/5 + 5 not in b:
        continue

    if x % 7 == 0 and x/7 + 7 not in b:
        continue
    
    # Pull out the big guns: factorise
    primes = []
    val = x
    i = 0
    found = False
    while a[i] < val ** 0.5 + 1:
        if val % a[i] == 0:
            val /= a[i]
            primes.append(a[i])
            if c[val] != -1:
                primes.extend(c[val])
                val = 1
        elif val == 1:
            found = True
        elif val in b:
            primes.append(val)
            val = 1
        else:
            i += 1
    if not found and val != 1:
        primes.append(val)
    c[x] = primes

    # Primes is the ordered list of primes
    d = defaultdict(int)
    for p in primes:
        d[p] += 1
        
    if x == 1:
        d[1] += 1

    item = d.items()
    first = [x[0] for x in item]
    found = False
    for v in itertools.product(*[[x for x in xrange(it[1]+1)] for it in item], repeat=1):
        total = 1
        for m,n in zip(first, v):
            total *= m ** n
        if total + orig / total not in b:
            found = True
            #print total, orig, v

    if not found:
        answer += orig

print "Answer:", answer
print int(time.time() - start), "secs"
