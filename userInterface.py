from blessed import Terminal
from loadingMaps import load_map
uni_map = []
term = Terminal()
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
        print('Welcome to ZORK, a text based adventure game.\nPlease select your map: map1, map2, map3, map4, map5')
        s = input()
        if s == 'map1':
            uni_map = load_map('map1.txt')

print(UI_start())