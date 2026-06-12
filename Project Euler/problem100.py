# Solve Pell's equation for the recurrence relation.
t = 21
b = 15
while True:
    t_next = 3 * t + 4 * b - 3
    b_next = 2 * t + 3 * b - 2

    if t_next >= 10 ** 12:
        raise Exception(b_next)

    t = t_next
    b = b_next
