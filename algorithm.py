import math
import itertools 

''' rotNum must be a tuple of p and q '''
def MaxSetGenerating(d, rotNum, orbit):
    p = rotNum[0]
    q = rotNum[1]
    orbit = orbit.sort()
    newOrbit = orbit 

    # reduce first digit to 0
    while newOrbit[0] > 0:
        newOrbit = map(lambda x: x - 1, newOrbit)

    N_q = newOrbit[len(newOrbit) - 1]

    maximalSets = set()

    for i in range(N_q - 1):
        placements = []

        for combo in itertools.combinations(range(d-1-N_q), d-1-i):
            
            placements.append([j in combo for j in range(d-1-N_q)])
        
        # because this and fillGap() do not depend on what placements have been determined so far,
        # and do not dependent on the outermost for loop as well for the arguments, can we not move both this
        # and fillGap() outside our for loop altogether?
        gapSizes = gapSizes(orbit, p, q)

    pass


''' placements is now last argument so that it can be a keyword argument with default 
    value of an empty list'''
def fillGap(currentGap, gapSizes, numPreimagesLeft, placements=[[]]):
    
    if numPreimagesLeft == 0:
        return placements
    newPlacements = []
    
    for i in range(len(placements)):
        # temporary, not sure what arguments should be
        for combo in itertools.combinations([], 0):
            newPlacements.append(placements[i] + combo)

    return fillGap(currentGap + 1, gapSizes, numPreimagesLeft - 1, placements=newPlacements)


def gapSizes(orbit, p, q):

    sizes = [orbit[i+1]-orbit[i] for i in range(len(orbit)-1)]
    sizes[q-p-1] -= 1
    return sizes