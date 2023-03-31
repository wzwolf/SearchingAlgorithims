#!/usr/bin/env python3

# complexity = n^2
def insertionsort(array):
    outputarray = array
    for index in range(0,len(array)):
        # extract current element from array
        key = outputarray[index]
        outputarray.pop(index)
        subindex = index
        while subindex > 0 and key < outputarray[subindex-1]:
            subindex -= 1
        if subindex < 0:
            outputarray.insert(0,key)
        else:
            outputarray.insert(subindex,key)
    return outputarray 