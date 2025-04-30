import blessed
from loadingMaps import load_map
from gameSaveLoad import savingGame
from generateRandomMazes import randomMaze
from progressiveMap import print_map
from movementFunctions import goEast
from movementFunctions import goWest
from movementFunctions import goNorth
from movementFunctions import goSouth
from movementFunctions import getCurrentLocation, grid


uni_map = []
term = blessed.Terminal()
with term.fullscreen():
    print(term.gold3('ZORK'))

print(term.red('hi there'))
with term.location(0, 10):
    print('this is at the bottom')
    print(term.fullscreen())

def UI(map):
    with term.fullscreen():
        print(map)

def UI_start():
    with term.location(0, 10):
        print('Welcome to ZORK, a text-based adventure game.\nPlease select your map: map1, map2, map3, map4, map5')
        s = input()
        p ='you have selected a map'
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
            uni_map = randomMaze(r, c)
        print(p)
        return uni_map
uni_map = UI_start()


print(UI_start())
alive = True
def UI_run(a):
    while a == True:
        i = input()
        key_words = ['print','move','save']
        if 'print' in i:
            print(print_map(uni_map))

        if 'move' in i:
            l = input("Which direction, how many units?")
            digit = l.split(',')
            print(digit)
            if 'east' in l:
                goEast(int(digit[1]))
            if 'west' in l:
                goWest(int(digit[1]))
            if 'north' in l:
                goNorth(int(digit[1]))
            if 'south' in l:
                goSouth(int(digit[1]))
print(UI_run(alive))

#sample code
progress = input("Would you like to save your progress?(yes/no)")
if progress == "yes":
    print(savingGame())

else:
    pass #start a new game