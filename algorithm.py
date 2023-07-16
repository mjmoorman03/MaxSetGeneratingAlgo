from itertools import combinations

def MaxSetGenerating(d : int, orbit : list[int]) -> list[list[str]]:
    ''' Given a degree d and a rotational orbit O = [o_1, o_2, ..., o_n],
        returns a list of all maximal rotational sets of degree d 
        containing orbit O, with each orbit represented as a string.'''

    p, q = rotNum(orbit)

    orbit.sort()
    newOrbit = orbit 

    gapSizes = getGapSizes(orbit, p, q)

    # reduce first digit to 0
    while newOrbit[0] > 0:
        newOrbit = list(map(lambda x: x - 1, newOrbit))

    # last point in orbit spatially
    N_q = newOrbit[-1]

    maximalSets = []

    for i in range(N_q):
        placements = []
        for combo in combinations(range(i, d-2), d-1-N_q):
            
            placements.append([(q-1) if j in combo else None for j in range(d-2)])
        
        placements = fillGap(i, 0, gapSizes, N_q - 1, placements)

        for placement in placements:
            maximalSets.append(convertPlacementToSet(placement, d, p, q))

    return maximalSets


def fillGap(position : int, currentGap : int, gapSizes : list[int], numPreimagesLeft : int, placements=[[]]) -> list[list[int]]:

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
    sizes = [orbit[i+1]-orbit[i] for i in range(len(orbit)-1)]
    sizes[q-p-1] -= 1
    return sizes


def convertPlacementToSet(placement : list[int], d : int, p : int, q : int) -> list[str]:

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


def rotNum(orbit : list[int]) -> tuple[int, int]:
    ''' Given a rotational orbit O = [o_1, o_2, ..., o_n], returns the 
        rotational number of O.'''

    copy = orbit.copy()
    ordered = sorted(orbit)

    while copy[0] != ordered[0]:
        for i in range(len(copy) - 1):
            copy[i] = copy[i + 1]
        copy[-1] = ordered[0]

    rotNumer = 1

    while copy[1] != ordered[rotNumer]:
        rotNumer += 1
        if rotNumer == len(copy):
            break

    return rotNumer, len(orbit)


if __name__ == "__main__":
    print(MaxSetGenerating(3, [0,1,2]))
