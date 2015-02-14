odd = 0
for x in range(2, 10000 + 1):
    m = 0
    d = 1
    a0 = int(x ** 0.5)

    # Ignore perfect squares
    if a0 * a0 == x:
        continue
    
    a = a0
    count = 0
    while True:
        m = d * a - m
        d = (x - m ** 2) / d
        a = int((a0 +  m) / d)
        count += 1
        if (a == 2 * a0):
            if count % 2 == 1:
                odd += 1
            break

print "Result:", odd
