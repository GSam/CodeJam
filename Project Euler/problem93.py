import itertools

def generate(li, pos, z, nums = [1,2,3,4,5,6,7,8,9]):
    if (pos > 6):
        i = evaluate(z)
        set.add(i)
        return
    if (li[pos]):
        for x in ['+','-','*','/']:
            generate(li, pos+1, z + x, nums)
    else:
        for x in xrange(len(nums)):
            num = nums[:]
            sss = num[x]
            del num[x]
            generate(li, pos+1, z + str(sss), num)

            
def evaluate(x):
    stack = []
    for char in x:
        if (char.isdigit()):
            stack.append(int(char))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if (char == '+'):
                stack.append(num1+num2)
            elif (char == '-'):
                stack.append(num2-num1)
            elif (char == '*'):
                stack.append(num1*num2)
            elif (char == '/'):
                if (num1 == 0):
                    return -1
                stack.append((1.0*num2)/num1)
            else:
                raise
    return stack.pop()

maxCount = 0
per = None
set = set()

for permutation in itertools.combinations([1,2,3,4,5,6,7,8,9], 4):
    permutation = list(permutation)
    set.clear()
    generate([False, False, False, False, True, True, True], 0, "", permutation[:])
    generate([False, False, False, True, False, True, True], 0, "", permutation[:])
    generate([False, False, False, True, True, False, True], 0, "", permutation[:])
    generate([False, False, True, False, False, True, True], 0, "", permutation[:])
    generate([False, False, True, False, True, False, True], 0, "", permutation[:])
    li = sorted(set)
    try:
        index = li.index(1)
    except:
        continue
    count = 1
    for s in range(index, len(li)):
        if (li[s] % 1 != 0):
            continue
        if (count == li[s]):
            count += 1
        else:
            count -= 1
            break
    if count > maxCount:
        maxCount = count
        per = permutation
    print count
        
print 'Answer:', per
