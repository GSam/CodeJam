import copy

a = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
f = open("C:\Users\Garming\Downloads\sudoku.txt", 'r')

def is_ok(sudoku, index):
    # check row
    row = index / 9
    for i in xrange(row * 9, row * 9 + 9):
        if i == index:
            continue
        if sudoku[i] == sudoku[index]:
            return False
    # check column
    column = index % 9
    for i in xrange(0, 9):
        if column == index:
            continue
        if sudoku[column] == sudoku[index]:
            return False
        column += 9
    # check box
    boxX = (index % 9) / 3
    boxY = index / 27
    box_zero = 3 * boxX + 27 * boxY
    for y in xrange(3):
        for x in xrange(3):
            i = box_zero + x + 9*y
            if index == i:
                continue
            if sudoku[i] == sudoku[index]:
                return False
    return True


def mark(sudoku, constraints, index):
    # check row
  #  print constraints
    constraints[index].intersection_update({sudoku[index]})
   # print constraints
    if len(constraints[index]) == 0:
            #print index, sudoku[index], constraints[index]
            return False
         #   raise Exception("arg %d" % (index))
   # print constraints
    row = index / 9

    to_check = [set() for x in xrange(11)]

    for i in xrange(row * 9, row * 9 + 9):
        if i == index:
            continue
        l = len(constraints[i])
        if len(constraints[i]) == 0:
            #return False
            raise Exception("poop%d %d" % (i,index))
        constraints[i].discard(sudoku[index])
        if len(constraints[i]) == 0:
            #raise Exception("%d %d" % (i,index))
            return False
        if len(constraints[i]) != l and len(constraints[i]) == 1:
            sudoku[i] = constraints[i].pop()
            constraints[i].add(sudoku[i])
            if not mark(sudoku, constraints, i):
                return False
        if sudoku[i] == sudoku[index]:
            return False
        if sudoku[i] == 0:
            to_check[sudoku[i]].add(i)

    for x in xrange(1,10):
        t = to_check[x]
        if len(t) == 1:
            print t, x
            ind = t.pop()
            sudoku[ind] = x
            if not mark(sudoku, constraints, ind):
                return False

    to_check = [set() for x in xrange(11)]
    # check column
    column = index % 9
    for i in xrange(0, 9):
        if column == index:
            continue
        l = len(constraints[column])
        if len(constraints[column]) == 0:
                #return False
                raise Exception("rubbish22%d %d" % (column,index))
        constraints[column].discard(sudoku[index])
        if len(constraints[column]) == 0:
                #print sudoku[index]
                return False
                #raise Exception("rubbishdd%d %d" % (column, index))
        if len(constraints[column]) != l and len(constraints[column]) == 1:
            sudoku[column] = constraints[column].pop()
            constraints[column].add(sudoku[column])
            if(not mark(sudoku, constraints, column)):
                return False
        if sudoku[column] == sudoku[index]:
            return False
        if sudoku[column] == 0:
            to_check[sudoku[column]].add(column)
        column += 9

    for x in xrange(1,10):
        t = to_check[x]
        if len(t) == 1:
            ind = t.pop()
            sudoku[ind] = x
            if not mark(sudoku, constraints, ind):
                return False

    to_check = [set() for x in xrange(11)]

    # check box
    boxX = (index % 9) / 3
    boxY = index / 27
    box_zero = 3 * boxX + 27 * boxY
    for y in xrange(3):
        for x in xrange(3):
            i = box_zero + x + 9*y
            if index == i:
                continue
            l = len(constraints[i])
            if len(constraints[i]) == 0:
                #return False
                raise Exception("rubbish%d %d" % (i,index))
            constraints[i].discard(sudoku[index])
            if len(constraints[i]) == 0:
                #raise Exception("rubbish2%d %d" % (i,index))
                return False
            if len(constraints[i]) != l and len(constraints[i]) == 1:
                sudoku[i] = constraints[i].pop()
                constraints[i].add(sudoku[i])
                if not mark(sudoku, constraints, i):
                    return False
            if sudoku[i] == sudoku[index]:
                return False
            if sudoku[i] == 0:
                to_check[sudoku[i]].add(i)
    for x in xrange(1,10):
        t = to_check[x]
        if len(t) == 1:
            ind = t.pop()
            sudoku[ind] = x
            if not mark(sudoku, constraints, x):
                return False
    return True


base = None
constraints = [{1,2,3,4,5,6,7,8,9} for x in range(81)]
sud = None
def solve(sudoku, constraints, index):
    global base, sud
    sud = sudoku 
    #print sudoku, constraints
    option = [(len(constraints[s]), s) for s in xrange(len(constraints)) if len(constraints[s]) > 1]
    if len(option) == 0:
        return sudoku
    n,s = min(option)
    #if index >= 81:
    #    return sudoku
    if base[index] != 0:
        return solve(sudoku, constraints, s)
    #for x in xrange(1, 10):
   # print "ddd", constraints
    for x in constraints[index]:
       # print 'ddddd', x
        clone = sudoku[:]
        clone[index] = x
        #clone_con = copy.deepcopy(constraints)
        clone_con = [None] * 81
        for x in xrange(len(constraints)):
            clone_con[x] = set(constraints[x])
        if (mark(clone, clone_con, index)):
         #   print 'boo'
            res = solve(clone, clone_con, s)
            if (res is not None):
                return res
    return None 

def solve_init(sudoku):
    global base, constraints
    constraints =  [{1,2,3,4,5,6,7,8,9} for x in range(81)]
    #print sudoku
    base = sudoku[:]
    for x in xrange(len(sudoku)):
        if sudoku[x] != 0:
            mark(sudoku, constraints, x)
            #print sudoku[x]
            #print constraints, '\n'
 #   print constraints
    return solve(sudoku, constraints, 0)

#print solve_init([int(x) if x != '.' else 0 for x in a])

ans = 0

while True:
    n = f.readline()
    if n is None or n.strip() == "":
        break
    s = f.readline().strip() + f.readline().strip() + f.readline().strip() + f.readline().strip()  + f.readline().strip()+ f.readline().strip() + f.readline().strip() + f.readline().strip() + f.readline().strip()
    s = [int(x) for x in s]
    a = solve_init(s)
    ans += a[0] * 100 + a[1] * 10 + a[2]
    print 'next', ans
