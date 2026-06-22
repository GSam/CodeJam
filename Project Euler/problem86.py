def problem86():
    solutions = 0
    for M in range(1, 1000000):
        for S in range(2, 2*M+1):
            T = M**2+S**2
            SQRT = int(T ** 0.5)
            if SQRT * SQRT == T:
                solutions += S//2 - max(1, S-M) + 1
                if solutions >= 1000000:
                    print(M)
                    return
problem86()
