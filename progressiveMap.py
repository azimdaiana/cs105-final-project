from loadingMaps import load_map
#from userInterface import uni_map

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
    '''elif "print" and "map" in i:
        return uni_map'''


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