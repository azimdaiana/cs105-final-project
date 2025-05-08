import blessed
from utilities import load_map, print_map, randomMaze, getCurrentLocation, setLocation, guard_found, generate_problem, loadSavedGame, savingGame

term = blessed.Terminal()

#function selectMap starts the game by allowing player to input which map they would like. Uses load_map to set 'grid' to desired map
def selectMap():
    s = input("Welcome to Medieval Math Mayhem, a text-based math adventure game!\nPlease select your map (input one): map1, map2, map3, map4, map5, save. Or, input random to generate your own map\n"
              f"Or if you would like to return your previous game, please type continue\n")
    if s == "continue":
        savedGrid = loadSavedGame()
        if savedGrid:
            return savedGrid
    elif s == 'map1':
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
        c = int(input('How many columns will your grid have'))
        grid = randomMaze(r,c)
    else:
        print("Invalid input. Please try again.")
        return selectMap()
    print(f'Your selected map has the following dimensions: {len(grid)}x{len(grid[0])}')
    return grid

grid = selectMap()
progMap = print_map(grid)

print('You are currently trapped in a castle and must find your way out. To move, you may choose a direction (north, south, west, or east) and then the number of units you want to move.\n'
      'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n'
      'Get ready, the game is about to launch!'
      f"Reminder, this is what your maze looks like:\n{progMap}\n"
      "Find a path through the castle using the commands!\n"
      "You will start at the top left corner of the maze.\n"
      )

player_y, player_x = getCurrentLocation()

def UI_run():
    global player_x, player_y, grid
    win = False
    #continuous input dependent on if the player wins or not
    while win == False:
        i = input("\nWhat would you like to do? (move/save): ").lower()
        if 'move' in i:
            direction = input("Which direction would you like to go? (north/south/east/west)\n")
            distance = int(input("How many units would you like to move? (please print a numerical value)\n"))
            x, y = getCurrentLocation()
            if direction == "east":
                distMoved = setLocation(x + distance, y, grid, progMap)
            elif direction == "west":
                distMoved = setLocation(x - distance, y, grid, progMap)
            elif direction == "south":
                distMoved = setLocation(x, y + distance, grid, progMap)
            elif direction == "north":
                distMoved = setLocation(x, y - distance, grid, progMap)
            else:
                print("Invalid direction. Please try again.")
                continue
            if distMoved == False:
                print(f"You cannot move there, your location is still {getCurrentLocation()}")
            else:
                print(f"Your current location is {getCurrentLocation()}\n"
                      f"Your current progress map is {progMap}")
        elif "save" in i:
            savingGame(player_x, player_y, grid, progMap)

        player_y, player_x = getCurrentLocation()
        if grid[player_y][player_x] == 2:
            print('Congratulations! You have escaped the castle in this level.')
            win = True

if __name__ == "__main__":
    UI_run()
