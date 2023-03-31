#!/usr/bin/env python3

import random
import extractdata

def generaterandomdata(filename,length,startdigit,enddigit):
    """purpose of this funtion is to generate a file with random digits"""
    with open(filename, "w") as file:
        for index in range(length):
            file.write(str(random.randint(startdigit,enddigit))+"\n")

def generatesorteddata(filename,newfilename):
    array = extractdata.file_to_array(filename)
    sortedarray = sorted(array)
    with open(newfilename, "w") as file:
        for digit in sortedarray:
            file.write(str(digit)+"\n")

def main():
    """generate data2 and sorted data2 , 100 data set, 1 to 100000
    generate data3 and sorted data3, 1000000 data set, 1 to 1000000000"""
    generaterandomdata(filename="data2",length=100,startdigit=1,enddigit=10000)
    generatesorteddata(filename="data2",newfilename="sorteddata2")
    generaterandomdata(filename="data3",length=10000,startdigit=1,enddigit=1000000000)
    generatesorteddata(filename="data3",newfilename="sorteddata3")
    print("dataGenerated")

if __name__ == "__main__":
    main()