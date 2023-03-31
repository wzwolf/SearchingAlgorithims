#!/usr/bin/env python3

import math

def binarysearch(array,target):
    '''Searches a Sorted Array for index of item
        contnues to divides array at midpoint and checks if the number belongs to which array

        return index if item is found. only returns the first item
        returns null if nothing is found'''
    # check if array is array, check if target is valid
    #print(array)
    #print(target)
    # create array pointers 
    startindex = 0
    endindex = len(array) - 1
    # create output to return
    output = -1
    # while no target is found in array yet
    if target == array[startindex]:
        return startindex
    if target == array[endindex]:
        return endindex
    while output == -1 and startindex != endindex:
        midwayPointer = math.floor((endindex - startindex)/2+startindex)
        #print("startindex : {}".format(startindex))
        #print("endindex :{}".format(endindex))
        #print("midwayPointer : {}".format(midwayPointer))
        if target == array[midwayPointer]:
            output = midwayPointer
        if target > array[midwayPointer]:
            startindex = midwayPointer
        if target < array[midwayPointer]:
            endindex = midwayPointer
        if (endindex-startindex)/2<1:
            return None
    return output
