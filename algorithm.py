from hashlib import new
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
            
            placement = []
            for j in range(d-1-N_q):
                placement.append(j in combo)

    pass


def fillGap():


    pass


