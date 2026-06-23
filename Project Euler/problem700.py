smallest = float('inf')
prev = set()
total = 0
times = 0
while True:
    total += 1504170715041707
    total %= 4503599627370517
    if total in prev:
        break

    if total < smallest:
        smallest = total
        prev.add(total)

        print(total)

        if len(prev) > 15:
            break

    times += 1

def extended_gcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        quotient = old_r // r
        old_r, r = (r, old_r - quotient * r)
        old_s, s = (s, old_s - quotient * s)
        old_t, t = (t, old_t - quotient * t)
    #print "Bezout coefficients:", (old_s, old_t)
    #print "greatest common divisor:", old_r
    #print "quotients by the gcd:", (t, s)
    return old_s, old_t, old_r

A_INVERSE = pow(1504170715041707, -1, 4503599627370517)
old_s, old_t, old_r = extended_gcd(1504170715041707, 4503599627370517)
print(old_s % 4503599627370517, old_t, old_r)

# S(N) = 1504170715041707N mod 4503599627370517
# eulercoin * A ** -1 = N mod 4503599627370517

sorted = []
for v in range(1, smallest - 1):
    N = v * A_INVERSE % 4503599627370517
    sorted.append((N, v))

sorted.sort()

running_minimum = smallest

for pair in sorted:
    n, v = pair
    if v < running_minimum:
        running_minimum = v
        prev.add(v)
        print(v)

print(sum(prev))
