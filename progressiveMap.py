from loadingMaps import load_map
from typing import List
from movement_functions import getCurrentLocation

#prints map when given input "print" and "map(number)" as parameter values
def print_map(i):
    if "print" and "map1" in i:
        return load_map("map1.txt")
    elif "print" and "map2" in i:
        return load_map("map2.txt")
    elif "print" and "map3" in i:
        return load_map("map3.txt")
    elif "print" and "map4" in i:
        return load_map("map4.txt")
    elif "print" and "map5" in i:
        return load_map("map5.txt")

print(print_map(input()))

#returns map with progess ('7' where player has been) when given current map configuration
def progressive_map(c_map):
    m = print_map(c_map)
    l = getCurrentLocation()
    m[l[0]][l[1]] = '7'
    return m

progressive_map("print map1")