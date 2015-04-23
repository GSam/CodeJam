# Solution using numpy which was awfully slow
# Two strategies missing:
# - i x Z x k always means Z = j
# - (...)(...)(...)ijk(...)(...) = 1 * 1 * .. (ijk) .. * 1 * 1

import numpy
# 0       1      2     3     4
# -2: 1, -1: -1, 0: 0, 1: 1, 2: -1
fixup = [1, -1, 0, 1, -1]
def find(ijk, pr = False):
    print "FND",len(ijk)
    leti = iden.copy()
    for ii in xrange(len(ijk)):
        letter = mapping[ijk[ii]]
        leti *= letter
        leti[0,0] = fixup[leti[0,0] + 2]
        leti[0,1] = fixup[leti[0,1] + 2]
        leti[1,0] = fixup[leti[1,0] + 2]
        leti[1,1] = fixup[leti[1,1] + 2]

        letj = iden.copy()
        
        #print ijk[:ii+1]
       # print leti
        if numpy.array_equal(leti, i):
            # Now find j
            for jj in xrange(ii + 1, len(ijk)):
                if jj % 1000 == 0:
                    print jj, ii
                letter = mapping[ijk[jj]]
                letj *= letter
                letj[0,0] = fixup[letj[0,0] + 2]
                letj[0,1] = fixup[letj[0,1] + 2]
                letj[1,0] = fixup[letj[1,0] + 2]
                letj[1,1] = fixup[letj[1,1] + 2]
                if pr:
                    print ijk[ii+1:jj+1]
                    
                #e = evaluate(ijk[ii+1:])
               # a = e[0,0]
                #if a != 0:
                #    e /= abs(a)
                #if a < 0:
                #    e /= -1
                    
                #if not numpy.array_equal(e, i):
                #print "BE", ijk[ii+1:jj+1]
                #    continue
                #else:
                #print "AR", e
                
                if numpy.array_equal(letj, j):
                    # Now find k
                    #print "E", ijk[jj+1:]
                    e = evaluate(ijk[jj+1:])
                    e[0,0] = fixup[e[0,0] + 2]
                    e[0,1] = fixup[e[0,1] + 2]
                    e[1,0] = fixup[e[1,0] + 2]
                    e[1,1] = fixup[e[1,1] + 2]
                    if numpy.array_equal(e, k):
                        # FOUND!!!
                        return True
    return False

def evaluate(ijk):
    start = iden.copy()
    for c in ijk:
        letter = mapping[c]
        start *= letter
        start[0,0] = fixup[start[0,0] + 2]
        start[0,1] = fixup[start[0,1] + 2]
        start[1,0] = fixup[start[1,0] + 2]
        start[1,1] = fixup[start[1,1] + 2]
        #print start
    return start

def find2(kji, pr = False):
    print "FOND",len(kji)
    letk = iden.copy()
    for kk in xrange(len(kji)):
        letter = mapping[kji[len(kji)-kk-1]]
        #print kji[len(kji)-kk-1], letter
        letk = letter * letk
        letk[0,0] = fixup[letk[0,0] + 2]
        letk[0,1] = fixup[letk[0,1] + 2]
        letk[1,0] = fixup[letk[1,0] + 2]
        letk[1,1] = fixup[letk[1,1] + 2]

        if pr:
            print ijk[:ii+1]
       # print leti
        if numpy.array_equal(letk, k):
            yield (len(kji)-kk-1, len(kji))

iden = numpy.matrix("1 0; 0 1")
i = numpy.matrix("1 1; 1 -1")
j = numpy.matrix("-1 1; 1 1")
k = numpy.matrix("0 -1; 1 0")

mapping = {'i':i, 'j': j, 'k': k}

f = open("C:/C-small-attempt2.in", "r")
g = open("C:/quarternion.txt", "w")

lines = f.readlines()
cases = int(lines[0])

line = 1
for x in range(cases):
    L, X = lines[line].split()
    ijk = lines[line+1].strip()
    line += 2
    if len(set(ijk)) < 2:
        ans = False
    else:
        ans = True
        
    print x, X, len(ijk) * int(X)
    if ans:
        #print L, X, ijk 
        ijk = ijk * int(X)
        e = evaluate(ijk)
        e[0,0] = fixup[e[0,0] + 2]
        e[0,1] = fixup[e[0,1] + 2]
        e[1,0] = fixup[e[1,0] + 2]
        e[1,1] = fixup[e[1,1] + 2]
        
        #print "EVAL", e, ijk
        
        #print ijk
        #print iden
        aa= list(find2(ijk))
        #print aa,e 
        if numpy.array_equal(e, -iden) and len(aa) > 0:
            #print ijk
            ans = find(ijk)
        else:
            ans = False
        
    g.write("Case #" + str(x+1)+": " + ("YES" if ans else "NO") + "\n")

g.close()
