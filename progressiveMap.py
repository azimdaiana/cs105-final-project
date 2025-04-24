from loadingMaps import load_map
from typing import List
#printing map when player inputs "print map"

def print_map(i):
    if "print" and "map1" in i:
        return load_map("map1.txt")
    if "print" and "map2" in i:
        return load_map("map2.txt")
    if "print" and "map3" in i:
        return load_map("map3.txt")
    if "print" and "map4" in i:
        return load_map("map4.txt")
    if "print" and "map5" in i:
        return load_map("map5.txt")

print(print_map("print map1"))
#
# def print_map(i)->List[int]:
#     m = []
#     if 'print' and 'map1' in i:
#         m = load_map('map1.txt')
#     else:
#         m = []
#     return m
#
# print_map("print map1")