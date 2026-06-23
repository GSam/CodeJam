ZERO = [[1, 1, 1],
        [8, 0, 8],
        [1, 1, 1]]

ONE = [[0, 0, 1],
       [8, 0, 8],
       [0, 0, 1]]

TWO = [[0, 1, 1],
       [8, 1, 8],
       [1, 1, 0]]

THREE = [[0, 1, 1],
         [8, 1, 8],
         [0, 1, 1]]

FOUR = [[1, 0, 1],
        [8, 1, 8],
        [0, 0, 1]]

FIVE = [[1, 1, 0],
        [8, 1, 8],
        [0, 1, 1]]

SIX = [[1, 1, 0],
       [8, 1, 8],
       [1, 1, 1]]

SEVEN = [[1, 1, 1],
         [8, 0, 8],
         [0, 0, 1]]

EIGHT = [[1, 1, 1],
         [8, 1, 8],
         [1, 1, 1]]

NINE = [[1, 1, 1],
        [8, 1, 8],
        [0, 1, 1]]

EMPTY = [[0, 0, 0],
         [8, 0, 8],
         [0, 0, 0]]

indexed = {0:ZERO, 1:ONE, 2:TWO, 3:THREE, 4:FOUR, 5:FIVE, 6:SIX, 7:SEVEN, 8:EIGHT, 9:NINE, -1: EMPTY}
cached = {}

cached_flat = {}
for i in indexed:
    n = indexed[i]
    count = 0
    for y in n:
        for x in y:
            if x == 1:
                count += 1
    cached_flat[i] = count

print(cached_flat)

def count_transitions_sam(initial=137):
    #print(initial)
    digital_root = initial
    total = 0
    total += 2 * sum(cached_flat[int(digit)] for digit in str(digital_root))
    while True:
        digital_root = sum(int(x) for x in str(digital_root))
        #print(digital_root)

        total += 2 * sum(cached_flat[int(digit)] for digit in str(digital_root))

        if digital_root < 10:
            break

    return total

def diff(prev_idx, current_idx):
    prev = indexed[prev_idx]
    current = indexed[current_idx]

    result = 0
    for y in range(3):
        for x in range(3):
            if prev[y][x] == 1 and current[y][x] == 0:
                result += 1
            elif prev[y][x] == 0 and current[y][x] == 1:
                result += 1

    cached[(prev_idx,current_idx)] = result

    return result

def digitify(digit):
    if digit == '#':
        return -1
    else:
        return int(digit)

def digit_sum(list):
    total = 0
    for i in list:
        if i == -1:
            continue
        total += i
    return total

def count_transitions_max(initial=137):
    #print(initial)
    digital_root = initial
    total = 0
    total += sum(cached_flat[int(digit)] for digit in str(digital_root))
    prev = [digitify(digit) for digit in str(digital_root).rjust(10, '#')]
    while True:
        digital_root = digit_sum(prev)
        current = [digitify(digit) for digit in str(digital_root).rjust(10, '#')]
        #print(digital_root)
        #print(prev, current)

        sub_total = 0
        for x in range(10):
            #print(prev[x], current[x])
            if (prev[x], current[x]) in cached:
                c = cached[(prev[x], current[x])]
                sub_total += c
                #print("CACHED", c)
            else:
                d = diff(prev[x], current[x])
                sub_total += d
                #print("DIFF", d)
        #print("SUB", sub_total)

        total += sub_total

        prev = current

        if digital_root < 10:
            total += sum(cached_flat[int(digit)] for digit in str(digital_root))
            break

    return total


print(count_transitions_sam())
print(count_transitions_max())

def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

a = rwh_primes(20000000)
primes = set(a)

sam = 0
m_x = 0
for x in range(10**7, 2*10**7+1):
    if x in primes:
        sam += count_transitions_sam(x)
        m_x += count_transitions_max(x)

print(sam, m_x, sam-m_x)
