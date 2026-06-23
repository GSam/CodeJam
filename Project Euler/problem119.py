answers = []

for b in range(2, 150):
    for k in range(2, 10**12):
        total = b ** k

        if total > 10 ** 15:
            break

        digit_sum = 0
        for x in str(total):
            digit_sum += int(x)

        if digit_sum == b:
            answers.append(total)

answers.sort()
print(answers[29])
