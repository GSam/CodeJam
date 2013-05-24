init = [0,1,4,9,16,25,36,49,64,81]
array = [0] * 10000000
array[1] = 1
array[89] = 89
def call(x):
    if(array[x] != 0):
        return array[x]
    y = call(sumFact(x))
    array[x] = y
    return array[x]

def sumFact(x):
    total = 0
    while x != 0:
        total += init[x%10]
        x/=10
    return total

answer = 0
for x in xrange(1,10000000):
    y = call(x)
    if y == 89:
        answer += 1
print answer
