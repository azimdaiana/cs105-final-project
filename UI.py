import blessed
from utilities import load_map, print_map, randomMaze, getCurrentLocation, setLocation, guard_found, generate_problem, loadSavedGame, savingGame

term = blessed.Terminal()

#function selectMap starts the game by allowing player to input which map they would like. Uses load_map to set 'grid' to desired map
def selectMap():
    s = input(
        "Welcome to Medieval Math Mayhem, a text-based math adventure game!\nPlease select your map (input one): map1, map2, map3, map4, map5, save. Or, input random to generate your own map\n"
        f"Or if you would like to return your previous game, please type continue\n")
    if s == "continue":
        try:
            loc, grid, progMap = loadSavedGame()
            player_x, player_y = loc
            print('Your last game has been uploaded!\n'
                  f"Reminder, this is what your maze looks like:\n{progMap}\n"
                  f"Your current location is ({player_x}, {player_y})\n"
                  "Find a path through the castle using the commands!\n"
                  )
        except FileNotFoundError:
            print("No saved game found. Please select a map or generate one.")
            return selectMap()
    else:
        if s == 'map1':
            grid = load_map('map1.txt')
        elif s == 'map2':
            grid = load_map('map2.txt')
        elif s == 'map3':
            grid = load_map('map3.txt')
        elif s == 'map4':
            grid = load_map('map4.txt')
        elif s == 'map5':
            grid = load_map('map5.txt')
        elif s == 'random':
            r = int(input('How many rows will your grid have?'))
            c = int(input('How many columns will your grid have?'))
            grid = randomMaze(r,c)
        else:
            print("Invalid input. Please try again.")
            return selectMap()
        progMap = print_map(grid)
        player_x, player_y = getCurrentLocation()
        print(f'Your selected map has the following dimensions: {len(grid)}x{len(grid[0])}')
        print(
            'You are currently trapped in a castle and must find your way out. To move, you must choose a direction (north, south, west, or east) and you will be moved 1 unit.\n'
            'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n'
            'Get ready, the game is about to launch! '
            f"Reminder, this is what your maze looks like:\n{progMap}\n"
            "Find a path through the castle using the commands!\n"
            f"You will start at the top left corner of the maze"
        )
    return grid, progMap, player_x, player_y

# grid = selectMap(s)
# progMap = print_map(grid)

# print('You are currently trapped in a castle and must find your way out. To move, you may choose a direction (north, south, west, or east) and you will be moved 1 unit.\n'
#       'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n'
#       'Get ready, the game is about to launch!'
#       f"Reminder, this is what your maze looks like:\n{progMap}\n"
#       "Find a path through the castle using the commands!\n"
#       "You will start at the top left corner of the maze.\n"
#       )

def UI_run():
    global grid, player_y, player_x, progMap
    win = False
    #continuous input dependent on if the player wins or not
    while win == False:
        i = input("\nWhat would you like to do? (move/save): ").lower()
        if 'move' in i:
            direction = input("Which direction would you like to go? (north/south/east/west)\n")
            # distance = int(input("How many units would you like to move? (please print a numerical value)\n"))
            x, y = getCurrentLocation()
            if direction == "east":
                distMoved = setLocation(x + 1, y, grid, progMap)
                player_x, player_y = getCurrentLocation()
                progMap[player_y][player_x] = 7
            elif direction == "west":
                distMoved = setLocation(x - 1, y, grid, progMap)
                player_x, player_y = getCurrentLocation()
                progMap[player_y][player_x] = 7
            elif direction == "south":
                distMoved = setLocation(x, y + 1, grid, progMap)
                player_x, player_y = getCurrentLocation()
                progMap[player_y][player_x] = 7
            elif direction == "north":
                distMoved = setLocation(x, y - 1, grid, progMap)
                player_x, player_y = getCurrentLocation()
            else:
                print("Invalid direction. Please try again.")
                continue
            if distMoved == False:
                print(f"You cannot move there, your location is still {getCurrentLocation()}")
            elif grid[player_y][player_x] == 3:
                if guard_found() == True:
                    continue
                else:
                    win = True
                    return "You have failed the level. Please try again."
            # if grid[player_y][player_x] == 3:
            #     print(guard_found(grid, player_y, player_x))
            #     if guard_found(grid, player_y, player_x) == True:
            #         continue
            #     else:
            #         return "You have failed the level. Please try again."
            else:
                print(f"Your current location is {getCurrentLocation()} and current progress map is {progMap}.")
        elif "save" in i:
            savingGame(player_x, player_y, grid, progMap)
        elif "print" in i:
            print(grid)
        player_x, player_y = getCurrentLocation()
        if grid[player_y][player_x] == 2:
            print(grid)
            print('Congratulations! You have escaped the castle.')
            open('lastGameSaved.json', 'w').close()

            win = True

if __name__ == "__main__":
    # s = input("Welcome to Medieval Math Mayhem, a text-based math adventure game!\nPlease select your map (input one): map1, map2, map3, map4, map5, save. Or, input random to generate your own map\n"
    #     f"Or if you would like to return your previous game, please type continue\n")
    # if s == "continue":
    #     try:
    #         loc, grid, progMap = loadSavedGame()
    #         player_x, player_y = loc
    #         print('Your last game has been uploaded!\n'
    #     f"Reminder, this is what your maze looks like:\n{progMap}\n"
    #     f"Your current location is ({player_x}, {player_y})\n"
    #     "Find a path through the castle using the commands!\n"
    #     )
    #     except FileNotFoundError:
    #         print("No saved game found. Please select a map or generate one.")
    # else:
    #     grid = selectMap(s)
    #     progMap = print_map(grid)
    #     player_x, player_y = getCurrentLocation()
    #     print('You are currently trapped in a castle and must find your way out. To move, you must choose a direction (north, south, west, or east) and you will be moved 1 unit.\n'
    #     'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n'
    #     'Get ready, the game is about to launch! '
    #     f"Reminder, this is what your maze looks like:\n{progMap}\n"
    #     "Find a path through the castle using the commands!\n"
    #     f"You will start at the top left corner of the maze"
    #     )
    selectMap()
    UI_run()
    again = (input("Would you like to play again?")).lower()


