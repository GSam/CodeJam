# Run in pypy3, finishes fast enough

rev = set()
for x in range(1, 10**9):
    reversible = True
    reverse = str(x)[::-1]
    if reverse.startswith('0'):
        continue
    string = str(x + int(reverse))
    for y in list(string):
        if int(y) % 2 == 0:
            reversible = False
            break

    if reversible:
        rev.add(x)

print(len(rev))
