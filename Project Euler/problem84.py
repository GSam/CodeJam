import random

temp = """GO 	A1 	CC1 	A2 	T1 	R1 	B1 	CH1 	B2 	B3 	JAIL
H2 	  	C1
T2 	  	U1
H1 	  	C2
CH3 	  	C3
R4 	  	R2
G3 	  	D1
CC3 	  	CC2
G2 	  	D2
G1 	  	D3
G2J 	F3 	U2 	F2 	F1 	R3 	E3 	E2 	CH2 	E1 	FP""".split()


board =[None] * 40
board[0:11] = temp[0:11]
board[11:20] = temp[12:29:2]
board[20:31]= temp[39:28:-1]
board[31:40] = temp[27:10:-2]

bdict = dict(zip(board, range(40)))

# initialize the community chest
chest = ['GO', 'JAIL'] + 14 * [None]
random.shuffle(chest)
# initialize the chance deck 
chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R', 'R', 'U', '3'] + 6 * [None]
random.shuffle(chance)

pos = 0
double_count = 0
counts = [0] * 40
count = 0

while(True):
    # run simulation
    die1 = random.randint(1,4)
    die2 = random.randint(1,4)
    #print pos
    pos += die1 + die2
    pos %= 40
    #print pos, die1+die2, board[pos]

    if die1 == die2:
        double_count += 1
    else:
        double_count = 0
    
    # check if they rolled three triples in a row
    if double_count > 2:
        double_count = 0
        pos = bdict['JAIL']
    else:    
        # check if they land on a special square
        tile = board[pos]
        if tile.startswith('CC'):
            card = chest.pop(0)
            if card is not None:
                pos = bdict[card]
            chest.append(card)
        elif tile.startswith('CH'):
            card = chance.pop(0)
            if card is not None:
                loc = bdict.get(card)
                if loc is None:
                    if card == '3':
                        pos -= 3
                        pos %= 40
                        if board[pos].startswith('CC'):
                            card = chest.pop(0)
                            if card is not None:
                                pos = bdict[card]
                            chest.append(card)
                else:  
                    while(True):
                        pos += 1
                        pos %= 40
                        if board[pos].startswith(card):
                            break
                    
            chance.append(card)
        if board[pos] == 'G2J':
            pos = bdict['JAIL']
    
    counts[pos] += 1
    count += 1
    if (count > 5000000):
        break

a = sorted(zip(counts, board), reverse=True)
ss = ""
for x in range(3):
    xx = a[x]
    ss += "%02d" % bdict[xx[1]]
print ss
