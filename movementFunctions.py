from Logic import precondition
from loadingMaps import load_map
from progressiveMap import print_map

player_x = 0
player_y = 0
#map = print_map(input("Which map would you like?"))

def canGoEast(x: int) -> bool:
    if grid[player_y][x] == 0:
        return False
    else:
        return True

def canGoWest(x: int) -> bool:
    if grid[player_y][x] == 0:
        return False
    else:
        return True

def canGoNorth(y: int) -> bool:
    if grid[y][player_x] == 0:
        return False
    else:
        return True

def canGoSouth(y: int) -> bool:
    if grid[y][player_x] == 0:
        return False
    else:
        return True


def goEast(x: int):
    global player_y, player_x
    for i in range(abs(player_x - x)):
        progMap[player_y][player_x + i] = 7
    player_x = x

def goWest(x: int):
    global player_y, player_x
    for i in range(abs(player_x - x)):
        progMap[player_y][player_x - i] = 7
    player_x = x

def goNorth(y: int):
    global player_y, player_x
    for i in range(abs(player_y - y)):
        progMap[player_y - i][player_x] = 7
    player_y = y

def goSouth(y: int):
    global player_y, player_x
    for i in range(abs(player_y - y)):
        progMap[player_y + i][player_x] = 7
    player_y = y

def getCurrentLocation() -> tuple:
    location: tuple = (player_x, player_y)
    return location


def setLocation(x: int, y: int) -> bool:
    precondition(x == player_x or y == player_y)
    if x < 0 or y < 0:
        print("Please input a positive index.")
    elif x > player_x:
        if canGoEast(x):
            print("Moved " + str(abs(player_x - x)) + " units east.")
            goEast(abs(player_x - x))
        else:
            print("Cannot go east.")

    elif x < player_x:
        if canGoWest(x):
            print("Moved " + str(abs(player_x - x)) + " units west.")
            goWest(abs(player_x - x))
        else:
            print("Cannot go west.")

    elif y < player_y:
        if canGoNorth(y):
            print("Moved " + str(abs(player_y - y) )+ " units north.")
            goNorth(abs(player_y - y))
        else:
            print("Cannot go north.")

    elif y > player_y:
        if canGoSouth(y):
            print("Moved " + str(abs(player_y - y)) + " units south.")
            goSouth(abs(player_y - y))
        else:
            print("Cannot go south.")
    progMap[player_y][player_x] = 7

grid = load_map("map1.txt")
print(grid)
print(" ")
progMap = print_map(grid)
print(progMap)
print(getCurrentLocation())
print(" ")
setLocation(1,0)
setLocation(2,0)
# setLocation(2,0) #1st param columns, 2nd param rows
# print(maze)
# # setLocation(2,1)
# setLocation(1,0)

# setLocation(1, 1)
# print(maze)
# setLocation(1, 2)
# print(maze)
