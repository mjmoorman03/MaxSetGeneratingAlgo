from hashlib import new
import math
import itertools 


''' rotNum must be a tuple of p and q '''
def MaxSetGenerating(d, rotNum, orbit):
    p = rotNum[0]
    q = rotNum[1]
    orbit = orbit.sort()
    newOrbit = orbit 
    while newOrbit[0] != 0:
        newOrbit = map(lambda x: x - 1, newOrbit)


    pass


def fillGap():


    pass


