def problem173(max=100):
    total = 0
    N = int(max // 4 + 1)
    for length in range(N, 2, -1):
        if length % 2 == 0:
            for hole in range(2, length, 2):
                if length * length - hole * hole <= max:
                    total += 1
        else:
            for hole in range(1, length, 2):
                if length * length - hole * hole <= max:
                    total += 1
    return total

print(problem173(1000000))
