l = ['A']  # lhs of grammar
# R = [ ['A','a'],['B']] #rhs of grammar
#R = [ [ 'A','a'], ['A','b'],['A','c'], ['B'],['C'],['D'] ]
R = [['A', '+', 'A'], ['A', '*', 'A'], ['a'], ['b'], ['c']]
nl = []  # new left
nR = []  # new Right
nRightWithRecursion = []  # new Right side Grammar with Recursion, has Recursion
fR = [nR, nRightWithRecursion]  # to print, list for new Right

lenR = len(R)  # length of right side
lenL = len(l)
lenInnerList = 0

for i in range(lenR):  # iright grammar
    lenInnerList = len(R[i])

    for j in range(lenL):  # at inner grammar, to compare left with right grammar
        # print [ 'R', R,'i',i,'j',j ] #debug print
        if(l[j] == R[i][j]):  # same symbol on left, right inner grammar
            R[i].pop(0)
            nRightWithRecursion.append(R[i])
        else:
            nR.append(R[i])  # take where there is no left recursion
            break  # not equal don't do anything, move to next or grammar

# add new variables where there is no left recursion
# -------------------------------------------------
nVar = 1  # new variable for left and right

lenNewRight = len(nR)
nl.append([l[0]])  # adding a list, previous left

for i in range(lenNewRight):
    nR[i].append(nVar)

lenNewRightWithRec = len(nRightWithRecursion)
# add next symbol, new left symbol, new grammar, contains right recursion's lhs
nl.append([nVar])

for i in range(lenNewRightWithRec):
    nRightWithRecursion[i].append(nVar)

nRightWithRecursion.append(['e'])  # empty string at converted right recursion

# -------------------------------------------------


# print R
# print nR
# print nRightWithRecursion

print(nl[0], "===>", fR[0])
print(nl[1], "===>", fR[1])
