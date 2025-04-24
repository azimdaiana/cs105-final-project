
#printing map when player inputs "print map"
def print_map():
    p = "print map"
    i = input()
    #map 1 is hardcoded into the map function, needs to be replaced with global variable
    m = open('map1.txt','r')
    if p == i:
        print(m.read())


