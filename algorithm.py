from itertools import combinations
from typing import Iterable, Sequence


def MaxSetGenerating(d : int, rotNum : Sequence[int], orbit : list[int]) -> list[list[str]]:
    ''' Given a degree d, a rotational orbit O = [o_1, o_2, ..., o_n], and a 
        rotation number p/q passed as a tuple (p, q), returns a list of all 
        maximal rotational sets of degree d containing orbit O, with each 
        orbit represented as a string.'''

    p = rotNum[0]
    q = rotNum[1]
    orbit.sort()
    newOrbit = orbit 

    gapSizes = getGapSizes(orbit, p, q)

    # reduce first digit to 0
    while newOrbit[0] > 0:
        newOrbit = map(lambda x: x - 1, newOrbit)

    # last point in orbit spatially
    N_q = newOrbit[-1]

    maximalSets = []

    # Find the maximal sets that contain this orbit at the (i+1)th position
    for i in range(N_q):
        # Each placement is an in progress construction of a complete placement of pre-images of zero,
        # these placements correspond one-to-one with maximal sets
        placements = []
        # Place pre-images that fall outside the orbit (i.e. after the last point since we shifted the orbit down)
        for combo in combinations(range(i, d-2), d-1-N_q):
            placements.append([(q-1) if j in combo else None for j in range(d-2)])
        
        # Place pre-images in the gaps that fall within the orbit
        placements = fillGap(i, 0, gapSizes, N_q - 1, placements)

        # Find corresponding maximal set for each placement
        for placement in placements:
            maximalSets.append(convertPlacementToSet(placement, d, p, q))

    return maximalSets


def fillGap(position : int, currentGap : int, gapSizes : list[int], numPreimagesLeft : int, placements=[[]]) -> list[list[int]]:
    """Given the position within the maximal set, the gap that is being checked, the gap sizes, the number of pre-images left to place,
    and the placements found, recursively fill the gaps without repetition."""

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


def getGapSizes(orbit : list[int], p : int, q : int) -> list[int]:
    """Given an orbit, its rotational numerator p, and rotational denominator q,
    finds the size of gaps (i.e. number of pre-images left to place) between each
    adjacent point in the orbit."""
    sizes = [orbit[i+1]-orbit[i] for i in range(len(orbit)-1)]
    # Removes one from this gap because it has the principal pre-image
    sizes[q-p-1] -= 1
    return sizes


def convertPlacementToSet(placement : list[int], d : int, p : int, q : int) -> list[str]:
    """Given a placement of pre-images, degree d, rotational numerator p, and rotational denominator q,
    find the corresponding maximal rotational set for this placement."""

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


if __name__ == "__main__":
    print(MaxSetGenerating(5, (1,5), [0,0,1,1,3]))