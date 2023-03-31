#!/usr/bin/env python3

import math

def BinarySearch(array,target):
    '''Searches a Sorted Array for index of item
        contnues to divides array at midpoint and checks if the number belongs to which array

        return index if item is found. only returns the first item
        returns null if nothing is found'''
    # check if array is array, check if target is valid
    print(array)
    print(target)
    # create array pointers 
    startIndex = 0
    endIndex = len(array) - 1
    # create output to return
    output = -1
    # while no target is found in array yet
    while output == -1:
        midwayPointer = math.floor((endIndex - startIndex)/2)
        print(midwayPointer)
        output = 1
    return output

