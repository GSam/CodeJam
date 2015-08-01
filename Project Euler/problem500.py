import decimal
import heapq

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

a = primes2(10**7)

# 500500th prime
prime = a[500500-1]

queue = []
count = 0
total = 1
for i in a:
    heapq.heappush(queue, (i,))
    if i == prime:
        break

while count < 500500:
    num, = heapq.heappop(queue)
    topush = num * num
    if topush <= prime:
        heapq.heappush(queue, (topush,))
    total *= num
    total %= 500500507
    count += 1
    
print "Answer:", total
