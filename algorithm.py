import math
from itertools import combinations

''' rotNum must be a tuple of p and q '''
def MaxSetGenerating(d, rotNum, orbit):

    p = rotNum[0]
    q = rotNum[1]
    orbit.sort()
    newOrbit = orbit 

    gapSizes = getGapSizes(orbit, p, q)

    # reduce first digit to 0
    while newOrbit[0] > 0:
        newOrbit = map(lambda x: x - 1, newOrbit)

    N_q = newOrbit[-1]

    #maximalSets = set()
    maximalSets = []

    for i in range(N_q):
        placements = []
        for combo in combinations(range(i, d-2), d-1-N_q):
            
            placements.append([(q-1) if j in combo else None for j in range(d-2)])
        
        # because this and fillGap() do not depend on what placements have been determined so far,
        # and do not dependent on the outermost for loop as well for the arguments, can we not move both this
        # and fillGap() outside our for loop altogether?
        #^
        # Yes for gapSizes, but I actually realized we can make fillGap dependent
        # on current combinations in a useful manner by passing in placements
        placements = fillGap(i, 0, gapSizes, N_q - 1, placements)

        for placement in placements:
            maximalSets.append(convertPlacementToSet(placement, d, p, q))

    return maximalSets

''' placements is now last argument so that it can be a keyword argument with default 
    value of an empty list'''
def fillGap(position, currentGap, gapSizes, numPreimagesLeft, placements=[[]]):

    if numPreimagesLeft == 0:
        return placements
    newPlacements = []
    
    for i in range(len(placements)):
        for combo in combinations(range(numPreimagesLeft), gapSizes[currentGap]):
            newPlacements.append(placements[i])
            numberEmptySeen = 0
            for j in range(len(newPlacements[-1])):
                if newPlacements[-1][j] is None:
                    if numberEmptySeen in combo:
                        if j < position:
                            newPlacements[-1][j] = currentGap + 1
                        else:
                            newPlacements[-1][j] = currentGap
                    numberEmptySeen += 1 

    return fillGap(position, currentGap + 1, gapSizes, numPreimagesLeft - gapSizes[currentGap], placements=newPlacements)


def getGapSizes(orbit, p, q):
    sizes = [orbit[i+1]-orbit[i] for i in range(len(orbit)-1)]
    sizes[q-p-1] -= 1
    return sizes

def convertPlacementToSet(placement, d, p, q):

    digitLists = [[] for _ in range(d - 1)]

    currentDigit = 0

    for i in range(q):
        if i == q - p:
            currentDigit += 1
        for j in range(len(digitLists)):
            if j != 0 and placement[j-1] == i:
                currentDigit += 1
            digitLists[j].append(str(currentDigit))


    maxSet = []

    for digitList in digitLists:
        orbit = "_"
        i = 0
        orbit += str(digitList[i])
        i = p
        while i != 0:
            orbit += str(digitList[i])
            i = (i + p) % q
        maxSet.append(orbit)

    return maxSet

print(MaxSetGenerating(5, (1,5), [0,0,1,1,3]))