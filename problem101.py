# sympy apparently had matrix calculation for reduced row echelon 
import sympy

sum = 0
print [1-y+y**2-y**3+y**4-y**5+y**6-y**7+y**8-y**9+y**10 for y in xrange(1,12)]

for g in range(2, 12):
    mat, stuff = sympy.Matrix([[y ** x for x in xrange(1,g-1)]+ [1] + [-y+y**2-y**3+y**4-y**5+y**6-y**7+y**8-y**9+y**10] for y in xrange(1,g)]).rref()
    print mat
    total = 0
    for k in range(1,g+1):
        total = 0
        for h in range(g-1):
            #print mat[h,g-1]
            if (h == g -2):
                total += mat[h, g-1]
                break
            total += mat[h,g-1] *(k ** (h + 1))
        print total + 1
    sum += total + 1
print sum
