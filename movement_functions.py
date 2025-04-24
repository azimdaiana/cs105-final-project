
from Logic import precondition
from loadingMaps import load_map

player_x = 0
player_y = 0

def getCurrentLocation() -> tuple:
    location: tuple = (player_x, player_y)
    return location

print(getCurrentLocation())


def setLocation(x: int, y: int) -> bool
    precondition(x == player_x or y == player_y)
    location: tuple = (player_x, player_y)
    if x > player_x:
        if canGoEast():
            goEast(abs(player_x - x))
            print ("Moved " + abs(player_x - x) + " units east.")
        else:
            print("Cannot go east.")
    if x < player_x:
        if canGoWest():
            goWest(abs(player_x - x))
            print("Moved " + abs(player_x - x) + " units west.")
        else:
            print("Cannot go west.")
    if y > player_y:
        if canGoNorth():
            goNorth(abs(player_y - y))
            print("Moved " + abs(player_y - y) + " units north.")
        else:
            print("Cannot go north.")
    if y < player_y:
        if canGoSouth():
            goSouth(abs(player_y - y))
            print("Moved " + abs(player_y - y) + " units south.")
        else:
            print("Cannot go south.")


def canGoEast()
