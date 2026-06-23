from collections import defaultdict
answers = defaultdict(int)

def problem174(max=100):
    total = 0
    N = int(max // 4 + 1)
    for length in range(N, 2, -1):
        if length % 2 == 0:
            for hole in range(2, length, 2):
                usage = length * length - hole * hole
                if usage <= max:
                    total += 1
                    answers[usage] += 1
        else:
            for hole in range(1, length, 2):
                usage = length * length - hole * hole
                if usage <= max:
                    total += 1
                    answers[usage] += 1
    return total

print(problem174(1000000))
final = 0
for x in answers:
    if answers[x] >= 1 and answers[x] <= 10:
        final += 1
print(final)
