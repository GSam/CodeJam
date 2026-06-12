import itertools

T = set()
for x in range(1, int((10**12) ** 0.5)+1):
    string = str(x * x)
    #print('*****', string)
    for y in range(len(string), 0, -1):
        for z in range(y, 0, -1):
            for combo in itertools.combinations(range(1,y), z):
                #print("NEW COMBO", combo)
                total = 0
                combination = list(combo)
                combination = [0] + combination
                combination = combination + [len(string)]
                for i in range(len(combination) - 1):
                    substr = int(string[combination[i]: combination[i+1]])
                    total += substr
                    #print('blah' + str(substr), combination, y, z)

                if total == x:
                    print("RESULT", x, string)
                    T.add(int(string))

print(sum(T))
