f = open("C:/A-large.in", "r")
g = open("C:/codejam2015Alarge.txt", "w")
lines = f.readlines()

cases = int(lines[0])
for x in range(1, cases + 1):
    a, b = lines[x].split()
    standing = 0
    to_stand = 0
    for y in range(int(a) + 1):
        if y <= standing:
            standing += int(b[y])
        else:
            to_stand += (y - standing)
            standing = y + int(b[y])
            
    #print "Case #%d: %d" % (x, to_stand)
    g.write("Case #%d: %d\n" % (x, to_stand))

g.close()
    
