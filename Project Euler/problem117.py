dictionary = {}

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    if n in dictionary:
        return dictionary[n]

    ans = f(n-1) + f(n-2) + f(n-3) + f(n-4)
    dictionary[n] = ans
    return ans

print(f(50))
