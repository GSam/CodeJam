import time

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

start = time.time()

primes = primes2(10**8)
a = set(primes)

length = 1
begin = ['']
ans = 0

checked = set()

while length < 14:
    out = []
    for num in begin:
        for char in ['0','1','2','3','4','5','6','7','8','9']:
            n = num + char
            intn = int(n)
            if intn == 0:
                continue
            sq = intn ** 0.5 + 1
            s = sum(int(b) for b in n)
            if intn % s != 0:
                continue
            
            if True:
                # right truncatable Harshad prime
                # check if strong
                prior = n
                priors = sum(int(b) for b in prior)
                tocheck = int(prior) / priors
                tosq = tocheck ** 0.5 + 1
                
                if tocheck in a:
                    # strong
                    for nextDig in ['1','3','7','9']:
                        maybe = int(prior + nextDig)
                        msq = maybe ** 0.5 + 1
                        isPrime = True
                        for y in primes:
                            if y > msq:
                                # prime
                                break
                            if maybe % y == 0:
                                isPrime = False
                                break
                        if isPrime:
                            ans += maybe
                            #print maybe
                    

                elif tocheck > 10 ** 8 - 1:
                    # might still be prime
                    isPrime = True
                    for y in primes:
                        if y > tosq:
                            # prime
                            break
                        if tocheck % y == 0:
                            isPrime = False
                            break
                    if isPrime:
                        # strong

                        for nextDig in ['1','3','7','9']:
                            maybe = int(prior + nextDig)
                            msq = maybe ** 0.5 + 1
                            isPrime = True
                            for y in primes:
                                if y > msq:
                                    # prime
                                    break
                                if maybe % y == 0:
                                    isPrime = False
                                    break
                            if isPrime:
                                ans += maybe
                                #print maybe


            out.append(n)
    length += 1
    begin = out
   # print begin

print "Answer:", ans
print time.time() - start 
