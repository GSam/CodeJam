# The requirement is that the XOR is equal to the sum.
# This means that no carries must occur.
# This is possible with an alternating sequence of 0,1
# (with the caveat that there may be 0 gaps longer than 1 digit)
#
# 01 10 00
# 100 101 000 001 010
#
#   1 2 3 4 5
# N 1 2 3 5
# Y 1 1 2 3 5
#
# N indicates that is a 1 digit up front
# Y indicates that is not a 1 digit up front
#
# Solution is:
# 1 + Sum[1..30] Fib(n) = Fib(32)
#
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print "Answer:", fib(32)
