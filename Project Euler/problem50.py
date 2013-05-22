primes = [2,3,5,7]
for n in range(12, 1000000, 6):
        for m in [-1,1]:
            nums = n + m
            for x in primes:
                if nums % x == 0:
                    break
                elif x > nums ** 0.5 + 1:
                    primes.append(nums)
                    break
                
cumul = primes[:]
set = set(primes)
for x in range(1, len(cumul)):
    cumul[x] = cumul[x] + cumul[x-1]
min = 1
ans = 0
for x in range(0, len(primes)):
    for y in range(x+min, len(primes)):
        total = cumul[y] - cumul[x]
        if(total > 1000000):
            break
        if(total in set and (y - x + 1) > min):
            min = y - x + 1
            ans = total
print ans
