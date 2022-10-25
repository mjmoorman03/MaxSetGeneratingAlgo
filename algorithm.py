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

    maximalSets = set()

    for i in range(newOrbit[len(newOrbit) - 1]):
        placements = []

        for combo in itertools.combinations(range(d-1-newOrbit[len(newOrbit) - 1]), d-1-i):
            pass

    pass


def fillGap():


    pass


