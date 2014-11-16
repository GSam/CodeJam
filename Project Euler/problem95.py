# Another modified sieve
# This is a little of a nostalgic problem
# 3 years ago, I was trying this problem to no avail in C#. 
val = None
def primes(n):
    global val
    """ Returns a list of primes < n """
    #sieve = [True] * n
    #val = [[1] for x in xrange(n)]
    val = [1 for x in xrange(n)]
    for i in xrange(3,n,1):
        for x in xrange(i, n, i):
            if x != i:
                #val[x].append(i)
                val[x] += i

    for i in xrange(2, n, 2):
        #val[i].insert(1,2)
        val[i] += 2
            
primes(10 ** 6 + 1)

mem = [False for x in xrange(10 ** 6 + 1)]

longest = None
maxi = 0
# For everything below 1 million
for x in xrange(1, 10 ** 6 + 1):
    current = x
    visited = set()
    visit= []
    # while element doesn't exceed 1M
    while current <= 10 ** 6:
        visited.add(current)
        visit.append(current)
        
        if len(visited) != len(visit):
            # you've encountered a visited number!
            # some chain found
            first = visit.index(current)
            if first == 0:
                # amicable chain found
                if len(visited) > maxi:
                    longest = visited
                    maxi = len(visited)
            else:
                temp = visit[first:-1]
                if len(temp) > maxi:
                    longest = temp
                    maxi = len(temp)
                    
            # mark the visited
            for y in visited:
                mem[y] = True
            break
        
        # Find the next chain
        current = val[current]

        # Joins an existing known chain
        if current <= 10**6 and mem[current]:
            # mark the visited
            for y in visited:
                mem[y] = True
            break

print sorted(longest)[0]

