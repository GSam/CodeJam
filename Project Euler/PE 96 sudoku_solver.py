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
base = None
def solve(sudoku, index):
    global base
    if index >= 81:
        print sudoku
        return sudoku
    if base[index] != 0:
        return solve(sudoku, index + 1)
    for x in xrange(1, 10):
        clone = sudoku[:]
        clone[index] = x
        if (is_ok(clone, index)):
            #print clone
            res = solve(clone, index + 1)
            if (res is not None):
                return res
    return None 

def solve_init(sudoku):
    global base
    base = sudoku[:]
    return solve(sudoku, 0)

solve_init([int(x) if x != '.' else 0 for x in a])
