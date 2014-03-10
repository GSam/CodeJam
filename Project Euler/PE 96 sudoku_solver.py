import copy

a = "7..25..98..6....1....61.3..9....1.......8.4.9..75.28.1.94..3.......4923.61.....4."
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
    row = index / 9
    for i in xrange(row * 9, row * 9 + 9):
        if i == index:
            continue
        constraints[i].discard(sudoku[index])
        if sudoku[i] == sudoku[index]:
            return False
    # check column
    column = index % 9
    for i in xrange(0, 9):
        if column == index:
            continue
        constraints[column].discard(sudoku[index])
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
            constraints[i].discard(sudoku[index])
            if sudoku[i] == sudoku[index]:
                return False
    return True


base = None
constraints = [{1,2,3,4,5,6,7,8,9} for x in range(81)]
sud = None
def solve(sudoku, constraints, index):
    global base, sud
    sud = sudoku 
    #print sudoku, constraints
    if index >= 81:
        return sudoku
    if base[index] != 0:
        return solve(sudoku, constraints, index + 1)
    #for x in xrange(1, 10):
   # print "ddd", constraints
    for x in constraints[index]:
       # print 'ddddd', x
        clone = sudoku[:]
        clone[index] = x
        clone_con = copy.deepcopy(constraints)
        if (is_ok(clone, index) and mark(clone, clone_con, index)):
         #   print 'boo'
            res = solve(clone, clone_con, index + 1)
            if (res is not None):
                return res
    return None 

def solve_init(sudoku):
    global base, constraints
   # print constraints
    base = sudoku[:]
    for x in xrange(len(sudoku)):
        if sudoku[x] != 0:
            mark(sudoku, constraints, x)
     #       print sudoku[x]
     #       print constraints, '\n'
 #   print constraints
    return solve(sudoku, constraints, 0)

print solve_init([int(x) if x != '.' else 0 for x in a])
