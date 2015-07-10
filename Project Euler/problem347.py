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
    

a = primes2(10000000/2 + 2)

c = [set() for x in xrange(10000000+1)]

for prime in a:
    for i in xrange(prime, 10000000+1, prime):
        c[i].add(prime)

visited = set()
total = 0
for i,x in enumerate(reversed(c)):
    if len(x) == 2 and tuple(sorted(x)) not in visited:
        total += (10000000-i)
        #print x, 10000000-i
        visited.add(tuple(sorted(x)))

print "Answer:", total
