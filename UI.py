import blessed
from utilities import load_map, print_map, randomMaze, getCurrentLocation, setLocation, guard_found, generate_problem, loadSavedGame, savingGame

term = blessed.Terminal()

#function selectMap starts the game by allowing player to input which map they would like. Uses load_map to set 'grid' to desired map
def selectMap():
    s = input(
        "Please select your map (input one): map1, map2, map3, map4, map5, save. If you want to generate your own map input random.\n"
        f"Or, if you would like to return to your previous game, please type continue\n")
    if "continue" in s:
        try:
            loc, grid, progMap = loadSavedGame()
            player_x, player_y = loc
            print("Your last game has been uploaded!\n"
                  f"This is your maze:\n{progMap}\n"
                  f"Current location: ({player_y}, {player_x})\n")
            return grid, progMap, player_x, player_y
        except (FileNotFoundError, ValueError):
            print("No saved game found. Please choose a new map.")
            return selectMap()
    else:
        if "map" and "1" in s:
            grid = load_map('map1.txt')
        elif "map" and "2" in s:
            grid = load_map('map2.txt')
        elif "map" and "3" in s:
            grid = load_map('map3.txt')
        elif "map" and "4" in s:
            grid = load_map('map4.txt')
        elif "map" and "5" in s:
            grid = load_map('map5.txt')
        elif s == 'random':
            try:
                print("The value for rows and columns must be greater than 1!")
                r = int(input('How many rows will your grid have? '))
                c = int(input('How many columns will your grid have?'))
                grid = randomMaze(r,c)
            except ValueError:
                print("Invalid input for grid size")
                return selectMap()

        progMap = print_map(grid)
        player_x, player_y = getCurrentLocation()

        print(f'\nYour selected map has the following dimensions: {len(grid)}x{len(grid[0])}')
        print(
            'You are currently trapped in a castle and must find your way out. To move, you must choose a direction (north, south, west, or east) and you will be moved 1 unit.\n'
            'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n\n'
            f"Reminder, this is what your maze looks like:\n{progMap}\n\n"
            "Find a path through the castle using the commands!\n"
            f"You will start at the top left corner of the maze."
        )
    return grid, progMap, player_x, player_y

def UI_run():
    global grid, player_y, player_x, progMap
    player_x, player_y = 0, 0
    win = False
    #continuous input dependent on if the player wins or not
    while win == False:
        i = input("\nWhat would you like to do? (move/save): ").lower()
        if 'move' in i:
            direction = input("Which direction would you like to go? (north/south/east/west)\n")
            # distance = int(input("How many units would you like to move? (please print a numerical value)\n"))
            x, y = player_x, player_y
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
                print("\nInvalid direction. Please try again.")
                continue
            if distMoved == False:
                print(f"You cannot move there, your location is still {getCurrentLocation()}")
            elif grid[player_y][player_x] == 3:
                if guard_found() == True:
                    print(f"\nYour current location is {getCurrentLocation()} and current progress map is {progMap}.")
                else:
                    win = True
            else:
                print(f"\nYour current location is {getCurrentLocation()} and current progress map is {progMap}.")
        elif "save" in i:
            savingGame(player_x, player_y, grid, progMap)
            win = True
        elif "print" in i:
            print(grid)
        player_x, player_y = getCurrentLocation()
        if grid[player_y][player_x] == 2:
            print(f"The actual maze was {grid}\n")
            print('Congratulations! You have escaped the castle.\n')
            open('lastGameSaved.json', 'w').close()
            win = True


if __name__ == "__main__":
    print("Welcome to Medieval Math Mayhem, a text-based math adventure game!\n")
    grid, progMap, player_x, player_y = selectMap()
    UI_run()
    again = input("Would you like to play again? (yes/no): ").strip().lower()
    if again == "yes":
        grid, progMap, player_x, player_y = selectMap()
        globals()["player_y"] = 0
        globals()["player_x"] = 0
        print(grid, progMap, player_x, player_y)
        UI_run()
    else:
        print("Thanks for playing!")