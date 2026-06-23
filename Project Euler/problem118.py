import itertools

def is_prime(n):
    """
    Checks if a number n is prime using optimized trial division.
    Time Complexity: O(sqrt(n))
    """
    # 1. Handle base cases
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime

    # 2. Eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # 3. Test divisors of the form 6k +/- 1 up to sqrt(n)
    # Since we already checked divisibility by 2 and 3, we can step by 6
    limit = int(n**0.5)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

a = rwh_primes(10**8)
primes = set(a)

count = 0
ans = set()

for permutation in itertools.permutations(list("123456789")):
    string = ''.join(permutation)

    if is_prime(int(string)):
        count += 1
        ans.add(string)

    for y in range(len(string), 0, -1):
        for z in range(y, 0, -1):
            for combo in itertools.combinations(range(1,y), z):
                combination = list(combo)
                combination = [0] + combination
                combination = combination + [len(string)]
                found = True
                l = []
                for i in range(len(combination) - 1):
                    substr = int(string[combination[i]: combination[i+1]])

                    if substr not in primes:
                        if substr > 10**8:
                            if not is_prime(substr):
                                found = False
                                break
                        else:
                            found = False
                            break

                    l.append(str(substr))

                if not found:
                    continue
                else:
                    l.sort()
                    ans.add('#'.join(l))
                    count += 1

print(count)
print(len(ans))
