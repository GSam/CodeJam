# Heronian Triangles
# Triangles with integer sides and integer perimeter
#
# Generating almost-equilateral Heronian triangles follows
# linear recursive equations
#
# Source:
# http://www.had2know.com/academics/nearly-equilateral-heronian-triangles.html
#
# Type 1: n-1, n, n+1
# T(n+2) = 4T(n+1) - T(n)
# T(1) = 4, T(2) = 14, T(3) = 52
#
# Type 2: n, n, n+1
# V(n+3) = 15V(n+2) - 15V(n+1) + V(n)
# V(1) = 5, V(2) = 65, V(3) = 901
#
# Type 3: n, n+1, n+1
# W(n+3) = 15W(n+2) - 15W(n+1) + W(n)
# W(1) = 16, W(2) = 240, W(3) = 3360
#
# PE Problem 94 concerns Type 2 & 3 of the above
#
# The method this will use is simply generating using the relation
# A better solution would be to find the closed form and solve the end point.
# A binary search could work in such a situation.

# Type 2: n, n, n+1
prev1 = 5
prev0 = 65
current = 901

total = 0
total += 16 + 196 + 2704

while True:
    temp = current
    current = 15 * current - 15 * prev0 + prev1
    prev1 = prev0
    prev0 = temp

    # semip = (current + current + current + 1.0)/2
    # A = (semip * (semip - current) * (semip - current) * (semip - current - 1)) ** 0.5

    perimeter = current + current + current + 1
    
    # While perimeter does not exceed 1B
    if perimeter > 1000000000:
        break

    total += perimeter

# Type 2: n, n+1, n+1
prev1 = 16
prev0 = 240
current = 3360

total += 50 + 722 + 10082

while True:
    temp = current
    current = 15 * current - 15 * prev0 + prev1
    prev1 = prev0
    prev0 = temp

    # semip = (current + current + current + 2.0)/2
    # A = (semip * (semip - current) * (semip - current - 1) * (semip - current - 1)) ** 0.5

    perimeter = current + current + 1 + current + 1
    
    # While perimeter does not exceed 1B
    if perimeter > 1000000000:
        break

    total += perimeter

print total
    
