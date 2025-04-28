
#from Logic import precondition
from loadingMaps import load_map
from progressiveMap import print_map

player_x = 0
player_y = 0
map = print_map(input("Which map would you like?"))

#this is a test comment
def getCurrentLocation() -> tuple:
    location: tuple = (player_x, player_y)
    return location

print(getCurrentLocation())


def setLocation(x: int, y: int) -> bool:
    #precondition(x == player_x or y == player_y)
    if x > player_x:
        if canGoEast(x):
            goEast(abs(player_x - x))
            print("Moved " + abs(player_x - x) + " units east.")
        else:
            print("Cannot go east.")
    if x < player_x:
        if canGoWest(x):
            goWest(abs(player_x - x))
            print("Moved " + abs(player_x - x) + " units west.")
        else:
            print("Cannot go west.")
    if y > player_y:
        if canGoNorth(y):
            goNorth(abs(player_y - y))
            print("Moved " + abs(player_y - y) + " units north.")
        else:
            print("Cannot go north.")
    if y < player_y:
        if canGoSouth(y):
            goSouth(abs(player_y - y))
            print("Moved " + abs(player_y - y) + " units south.")
        else:
            print("Cannot go south.")


def canGoEast(x: int) -> bool:
    if map[player_y][x] == 0:
        return False
    else:
        return True

def canGoWest(x: int) -> bool:
    if map[player_y][x] == 0:
        return False
    else:
        return True

def canGoNorth(y: int) -> bool:
    if map[y][player_x] == 0:
        return False
    else:
        return True

def canGoSouth(y: int) -> bool:
    if map[y][player_x] == 0:
        return False
    else:
        return True


def goEast(x: int):
    for i in range(abs(player_x - x)):
        map[player_y][player_x + i] = 7
    player_x = x

def goWest(x: int):
    for i in range(abs(player_x - x)):
        map[player_y][player_x - i] = 7
    player_x = x

def goNorth(y: int):
    for i in range(abs(player_y - y)):
        map[player_y + i][player_x] = 7
    player_y = y

def goSouth(y: int):
    for i in range(abs(player_y - y)):
        map[player_y - i][player_x] = 7
    player_y = y
