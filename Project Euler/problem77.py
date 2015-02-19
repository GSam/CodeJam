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

a = primes2(10**6)

for x in range(10, 10**6):
    index = bisect.bisect(a, x)
    
    limit = x+1
    ways = [0] * limit
    ways[0] = 1

    for i in range(0, index):
        value = a[i]
        for j in range(value, limit):
            ways[j] += ways[j - value]
            #print ways, value, j
            
    ans = ways[x]
    if ans > 5000:
        print "Answer:", x
        break
