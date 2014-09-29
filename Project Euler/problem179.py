# Used to run in about a minute, now closer to half
# Basically slowed down a prime sieve to fit the problem
# Could probably be made immensely more efficient by actually skipping values

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

val = None
def primes(n):
    global val
    """ Returns  a list of primes < n """
    #sieve = [True] * n
    val = [0 for x in xrange(n)]
    for i in xrange(3,n,1):
        for x in xrange(i, n, i):
            val[x] += 1

primes(10 ** 7)
print "DONE"
this = True
last = -1
count = 0
for x in xrange(2, 10**7):
    somelist = val[x]
    if this:
        somelist += 1
    somelist += 1
    if somelist == last:
        count += 1
        #print somelist, lastlist, len(somelist), len(lastlist)
    last = somelist
    #print somelist
    this = not this
    

"""a = primes2(int((10**7)** 0.5)+1)
b = set(a)

c = [-1 for x in xrange(10 ** 7)]
print "HELLO"
for x in xrange(2, 10**7):
    # prime factorise
    primes = []
    val = x
    i = 0
    found = False
    while a[i] < val ** 0.5 + 1:
        if val % a[i] == 0:
            val /= a[i]
            primes.append(a[i])
            if c[val] != -1:
                primes += c[val]
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
    c[x] = primes"""
