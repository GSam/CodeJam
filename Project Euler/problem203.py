import fractions
import bisect

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

# 50 choose 25 is approximately 10^14
# 50 choose 25 ^ 0.5 is approximately 10^7
# Therefore 10^8 should suffice

primes = primes2(10 ** 8)
for i in xrange(len(primes)):
    primes[i] = primes[i] * primes[i]

row = [1]
#print row
row = [1,1]
#print row
distinct = set([1])
for x in xrange(49):
    newrow = [1] * (len(row)+1)
    for y in xrange(1, len(newrow)-1):
        v = row[y-1] + row[y]
        newrow[y] = v
        distinct.add(v)
    row = newrow
    #print newrow

sumt = 0
aaa = []
for d in sorted(distinct):
    # check squarefree
    check = True
    for p in primes:
        if p > d:
            check2 = d 
            o = bisect.bisect_left(primes, check2)
            if o != len(primes) and primes[o] == check2:
                check = False
            break
        
        if d % p == 0:
            check = False
            break
        
    if check:
        sumt += d
        aaa.append(d)
        
print sumt
