count = 0
tri = {}
for x in range(1000):
    v = x * (x + 1) / 2
    string = str(v)
    if (v > 999 and v < 10000):
        count += 1
        temp = tri.get(string[:2])
        if temp is None:
            temp = []
            tri[string[:2]] = temp
        temp.append(string)
        
print count

square = {}
for x in range(1000):
    v = x * x
    string = str(v)
    if (v > 999 and v < 10000):
        count += 1
        temp = square.get(string[:2])
        if temp is None:
            temp = []
            square[string[:2]] = temp
        temp.append(string)
        
print count

pent = {}
for x in range(1000):
    v = x * (3 * x - 1) / 2
    string = str(v)
    if (v > 999 and v < 10000):
        count += 1
        temp = pent.get(string[:2])
        if temp is None:
            temp = []
            pent[string[:2]] = temp
        temp.append(string)
        
print count

hexa = {}
for x in range(1000):
    v = x * (2 * x - 1)
    string = str(v)
    if (v > 999 and v < 10000):
        count += 1
        temp = hexa.get(string[:2])
        if temp is None:
            temp = []
            hexa[string[:2]] = temp
        temp.append(string)
                
print count

hept = {}
for x in range(1000):
    v = x * (5 *x - 3) /2
    string = str(v)
    if (v > 999 and v < 10000):
        count += 1
        temp = hept.get(string[:2])
        if temp is None:
            temp = []
            hept[string[:2]] = temp
        temp.append(string)
        
print count

octa = {}
for x in range(1000):
    v = x * (3 *x - 2)
    string = str(v)
    if (v > 999 and v < 10000):
        count += 1
        temp = octa.get(string[:2])
        if temp is None:
            temp = []
            octa[string[:2]] = temp
        temp.append(string)
        
print count

todo = [hept, hexa, pent, square, tri]

def recurse(todo, current):
    if len(todo) == 0 and current[:2] == current[-2:]:
        return current
    end = current[-2:]
    for thing in todo:
        match = thing.get(end)
        if match is not None:
            # Found a possible match
            for m in match:
                newtodo = todo[:]
                newtodo.remove(thing)
                ans = recurse(newtodo, current + m)
                if ans is not None:
                    return ans
            
    return None

done = False
for oc in octa.itervalues():
    for o in oc: 
        a = recurse(todo, o)
        if a is not None:
            print a, o
            done = True
            break
    if done:
        break

total = 0
for x in range(6):
    start = a[:4]
    a = a[4:]
    total += int(start)

print "RESULT:",total
