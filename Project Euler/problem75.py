def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

matrix = [None] * 1500001

for m in xrange(2, 865+1):  #1224+1):
    # m > n
    for n in xrange(1, m):
        # check the difference is odd and values are coprime
        if (m - n) % 2 == 0 or gcd(m, n) != 1:
            continue
        
        # calculate half-sum
        half = m * (m + n)

        # calculate total
        total = 2 * half

        if total > 1500000:
            break
        
        #print total, m, n
        if matrix[total]:
            matrix[total] = False
        elif matrix[total] == False:
            pass
        else:
            matrix[total] = True
        
        for y in xrange(2 * total, 1500000, total):
            if matrix[y]:
                matrix[y] = False
            elif matrix[y] == False:
                pass
            else:
                matrix[y] = True

count = 0
for x in xrange(12, len(matrix)):
    if matrix[x]:
        count += 1

print "RESULT:", count
