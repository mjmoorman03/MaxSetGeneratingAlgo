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

        gapSizes = gapSizes(orbit, p, q)

    pass


def fillGap(placements, currentGap, gapSizes, numPreimagesLeft):

    pass


def gapSizes(orbit, p, q):

    sizes = [orbit[i+1]-orbit[i] for i in range(len(orbit)-1)]
    sizes[q-p-1] -= 1
    return sizes