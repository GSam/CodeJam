# Problem 66:
# Could've used normal continued fractions method, but this was method was interesting
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
    #print "Bezout coefficients:", (old_s, old_t)
    #print "greatest common divisor:", old_r
    #print "quotients by the gcd:", (t, s)
    return old_s, old_t, old_r

    
# Chakravala method - Brahmagupta
#
# m must satisfy two conditions
#  1) k | a + bm
#  2) m^2 - N must be minimal
#
# a0 = best approximation for m
def find(a0, a, b, k, N):
    k = abs(k)
    m0 = a0
    f = a % k
    g = k - f # bm ~ g (mod k)
    inv = extended_gcd(b, k)[0]
    m = (g * inv) % k
    
    # kt + m
    # exact match
    q = (m0 - m) / k
    if q * k == (m0 - m) and (m0 - m) != 0:
        return m0

    m0 = q * k + m
    m1 = q * k + m + k

    return m0 if abs(m0*m0 - N) < abs(m1*m1 - N) else m1

highest = 0
d = -1
for N in range(2, 1000 + 1):
    a0 = a = int(N ** 0.5)
    # perfect square
    if a * a == N:
        continue
    
    # first round
    k = a * a - N
    b = 1
    
    # LOOP HERE
    triple = (a, b, k)
    # compose with trivial triple (m, 1, m^2 - N)
    #   -> (am + Nb, a + bm, k(m^2 - N))
    while True:
        a, b, k = triple
        m = find(a0, a, b, k, N)
        a1 = (a*m + N*b) / abs(k)
        b1 = (a + b*m) / abs(k)
        k1 = (m*m - N) / k
        triple = (a1, b1, k1)

        if k1 == 1:
            # complete
            if a1 > highest:
                highest = a1
                d = N
            break

##n = 5
##
##def f(x,y):
##    return (2*x*y, y*y + n*x*x)
##
##m = 0
##x = 1
##y = 1
##
##while m <= 5:
##    m += 1
##    print x, y, (y + 0.0)/x
##    x,y = f(x,y)
##    
    
    
