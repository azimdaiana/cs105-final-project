import blessed
from loadingMaps import load_map
from generateRandomMazes import randomMaze
from progressiveMap import print_map
from movementFunctions import goEast
player_x = 0
player_y = 0
uni_map = []
term = blessed.Terminal()
print('Welcome to ZORK, a text based adventure game.\nPlease select your map: map1, map2, map3, map4, map5. Or input map6 to generate your own map')

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
    print(p)
    return uni_map
uni_map = UI_start()


print('You are in a castle use commands ... to move and navigate and watch out for guards. Input your first move:')
def UI_run():
    i = input()
    if 'print' in i:
        print(print_map(uni_map))
    if 'move' in i:
        print(goEast(2))

UI_run()
