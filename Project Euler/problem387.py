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
begin = ['1','2','3','4','5','6','7','8','9']
ans = 0

checked = set()

while length < 4:
    out = []
    for num in begin:
        for char in ['0','1','2','3','4','5','6','7','8','9']:
            n = num + char
            intn = int(n)
            sq = intn ** 0.5 + 1

            if intn in a:
                # right truncatable Harshad prime
                # check if strong
                prior = n[:-1]
                priors = sum(int(b) for b in prior)
                tocheck = int(prior) / priors
                tosq = tocheck ** 0.5 + 1
                
                if tocheck in a:
                    # strong
                    ans += intn
                    print intn
                    continue
                
                if tocheck in checked:
                    continue
                
                checked.add(tocheck)

                if tocheck > 10 ** 8 - 1:
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
                        a.add(tocheck)
                        ans += intn
                        print intn
                
                continue
            
            s = sum(int(b) for b in n)
            if intn % s != 0:
                # right truncatable maybe prime
                if intn > 10 ** 8 - 1:
                    # might still be prime
                    isPrime = True
                    for y in primes:
                        if y > sq:
                            # prime
                            break
                        if intn % y == 0:
                            isPrime = False
                            break
                    if isPrime:
                        a.add(intn)
                        # right truncatable Harshad prime
                        # check if strong
                        prior = n[:-1]
                        priors = sum(int(b) for b in prior)
                        tocheck = int(prior) / priors
                        tosq = tocheck ** 0.5 + 1

                        if tocheck in a:
                            # strong
                            ans += intn
                            print intn
                            continue

                        if tocheck in checked:
                            continue
                
                        checked.add(tocheck)
                        
                        if tocheck > 10 ** 8 - 1:
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
                                a.add(tocheck)
                                print intn
                                ans += intn
                        
                continue



            out.append(n)
    length += 1
    begin = out
   # print begin

print "Answer:", ans
print time.time() - start 
