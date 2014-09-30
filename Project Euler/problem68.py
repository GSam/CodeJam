import itertools
a = itertools.permutations([1,2,3,4,5,6,7,8,9])

smallest = "000000000000000"

for x in a:
    i = 10 + x[0] + x[1]
    j = x[2] + x[1] + x[3]
    k = x[4] + x[3] + x[5]
    l = x[6] + x[5] + x[7]
    m = x[8] + x[7] + x[0]

    if i == j and i == k and i == l and i == m:
        # check the strings

        list = [(x[2], 2), (x[4], 4), (x[6], 6), (x[8], 8)]
        list.sort()
        start = list[0][1]
        
        string = ""
        
        beg = start

        while beg < 9:
            string += str(x[beg]) + str(x[beg-1]) + str(x[(beg+1) % 9])
            beg += 2
        
        beg = 2
        
        string += str(10) + str(x[0]) + str(x[1])
        
        while beg < start:
            string += str(x[beg]) + str(x[beg-1]) + str(x[(beg+1) % 9])
            beg += 2

        if string >= smallest:
            smallest = string

print smallest
            
