def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

a = rwh_primes(10000000)
primes = set(a)

import itertools

def problem_51():
    for x in range(11, 10000000, 2):
        if a[x] not in primes:
            continue

        string = str(x)

        for digit in ['0', '1', '2']:
            if string.count(digit) >= 3:
                locs = [loc for loc, char in enumerate(string) if char == digit]
                replace_locs = itertools.combinations(locs, 3)
                for combo in replace_locs:
                    start_digit = 1 if 0 in combo else 0

                    exceptions = start_digit

                    string_digits = list(string)
                    for y in range(start_digit, 10):
                        if y == str(start_digit):
                            continue

                        string_digits[combo[0]] = str(y)
                        string_digits[combo[1]] = str(y)
                        string_digits[combo[2]] = str(y)
                        candidate = int(''.join(string_digits))

                        if candidate not in primes:
                            exceptions += 1

                    if exceptions <= 2:
                        return (string, exceptions)

print(problem_51())

