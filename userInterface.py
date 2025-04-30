import blessed
from loadingMaps import load_map
from generateRandomMazes import randomMaze
from progressiveMap import print_map
from movementFunctions import goEast
from movementFunctions import goWest
from movementFunctions import goNorth
from movementFunctions import goSouth
player_x = 0
player_y = 0
uni_map = []

term = blessed.Terminal()
print('Welcome to ZORK, a text based adventure game.\nPlease select your map: map1, map2, map3, map4, map5, save. Or input map6 to generate your own map')

def save():
    s = uni_map
    return s
save1 = save()

def UI_start():
    s = input()
    p = 'you have selected a map'
    if s == 'map1':
        uni_map = load_map('map1.txt')
    if s == 'map2':
        uni_map = load_map('map2.txt')
    if s == 'map3':
        uni_map = load_map('map3.txt')
    if s == 'map4':
        uni_map = load_map('map4.txt')
    if s == 'map5':
        uni_map = load_map('map5.txt')
    if s == 'map6':
        r = int(input('how many rows will your maze have?'))
        c = int(input('how many columns will your maze have'))
        uni_map = randomMaze(r,c)
    if s == 'save':
        uni_map = save1
    print(p)
    return uni_map
uni_map = UI_start()

alive = True
print('You are in a castle use commands ... to move and navigate and watch out for guards. Input your first move:')
def UI_run(a):
    while a == True:
        i = input()
        key_words = ['print','move','save']
        if 'print' in i:
            print(print_map(uni_map))

        if 'move' in i:
            l = input("Which direction, how many units?")
            digit = l.split(',')
            if 'east' in l:
                goEast(digit[1])
            if 'west' in l:
                goWest(digit[1])
            if 'north' in l:
                goNorth(digit[1])
            if 'south' in l:
                goSouth(digit[1])

        if 'save' in i:
            save()
            print('map saved')

        for l in key_words:
            string = ""+l
    if i not in string:
        print('huh? try a different action')





UI_run(alive)
