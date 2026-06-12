dictionary = {}

def f(n):
    if n in dictionary:
        return dictionary[n]

    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    ans = f(n-1) + sum([f(i) for i in range(n-4+1)]) + 1

    dictionary[n] = ans
    return ans

print(f(50))
