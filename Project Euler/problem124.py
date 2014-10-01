# Could've done some better prime factorization
# Runs fairly quick anyways

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
    

a = primes2(100000+1)
b = set(a)

c = [-1 for x in xrange(100000+1)]

for x in xrange(2, 100000+1):
    # prime factorise
    primes = set()
    val = x
    i = 0
    found = False
    while a[i] < val ** 0.5 + 1:
        if val % a[i] == 0:
            val /= a[i]
            primes.add(a[i])
            if c[val] != -1:
                primes = primes.union(set(c[val]))
                val = 1
        elif val == 1:
            found = True
        elif val in b:
            primes.add(val)
            val = 1
        else:
            i += 1
    if not found and val != 1:
        primes.add(val)
    c[x] = primes

c[1] = set([1])

for x in xrange(1, 100000+1):
    sum = 1
    for y in c[x]:
        sum *= y
    c[x] = sum, x

print list(sorted(c))[10000]
