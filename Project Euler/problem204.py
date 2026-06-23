primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#primes.reverse()

count = 0

def dfs(sum, prime_index):
    global count
    count += 1

    for p in range(prime_index, len(primes)):
        if sum * primes[p] > 10 ** 9:
            break
        dfs(sum * primes[p], p)

dfs(1, 0)

print(count)
