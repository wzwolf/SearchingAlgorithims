#!/usr/bin/env python3

def file_to_array(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        output = []
        for element in lines:
            if element.isdigit:
                output.append(int(element))
            else:
                output.append(element)
        return output


