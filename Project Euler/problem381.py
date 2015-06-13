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

def extended_gcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        quotient = old_r / r
        old_r, r = (r, old_r - quotient * r)
        old_s, s = (s, old_s - quotient * s)
        old_t, t = (t, old_t - quotient * t)       
    return old_s, old_t, old_r

a = primes2(10**8+1)
ans = 0

# Wilson's theorem states that (n - 1)! = -1 (mod n)
for x in xrange(2, len(a)):
    x = a[x]
    # 0-2, 1-3, 2-5
    total = 0
    # Case -1:
    # (n - 1)! ~ -1 (mod n)
    total += x-1

    # Case -2:
    # (n - 2)! ~ v (mod n)
    # (n - 1) * v ~ -1
    inv = extended_gcd(x-1, x)[0]
    m =  ((x-1) * inv) % x
    total += m
    
    # Case -3:  
    inv = extended_gcd(x-2, x)[0]
    m = (m * inv) % x
    total += m

    # Case -4:
    inv = extended_gcd(x-3, x)[0]
    m = (m * inv) % x
    total += m

    # Case -5:
    inv = extended_gcd(x-4, x)[0]
    m = (m * inv) % x
    total += m

    total %= x
    ans += total

print "Answer:", ans
    
