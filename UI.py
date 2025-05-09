import blessed
import time
from utilities import load_map, print_map, randomMaze, getCurrentLocation, setLocation, guard_found, generate_problem, loadSavedGame, savingGame

term = blessed.Terminal()

currentMapNum = 1
progressMade = False

def selectMap():
    """
    starts the game by allowing player to input which map they would like. Uses load_map to set 'grid' to desired map
    :return: grid, progMap, the user's current location coordinates
    """
    global player_x, player_y, currentMapNum, progressMade
    print(
        "Choose how you would like to play the game: \n"
        "1. Progress through pre-built maps (map1 -> map5)\n"
        "2. Generate a random map.\n"
        "3. Load a saved game\n")
    s = input("Your choice: ")
    if s == "1":
        progressMade = True
        currentMapNum = 1
        grid = load_map(f"map{currentMapNum}.txt")
    elif s == "2":
        try:
            print("The value for rows and columns must be greater than 1!")
            r = int(input('How many rows will your grid have? '))
            c = int(input('How many columns will your grid have? '))
            grid = randomMaze(r, c)
        except ValueError:
            print("Invalid input for grid size\n")
            return selectMap()
    elif s == "3":
        try:
            loc, grid, progMap = loadSavedGame()
            player_x, player_y = loc
            print("Your last game has been uploaded!\n"
                  f"This is your maze:\n{progMap}\n"
                  f"Current location: ({player_y}, {player_x})\n")
            return grid, progMap, player_x, player_y
        except (FileNotFoundError, ValueError):
            print("No saved game found. Please choose a new map.\n")
            return selectMap()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return selectMap()

    progMap = print_map(grid)
    player_x, player_y = getCurrentLocation()

    print(f'\nYour selected map has the following dimensions: {len(grid)}x{len(grid[0])}.')
    print(
        'You are currently trapped in a castle and must find your way out. To move, you must choose a direction (north, south, west, or east) to move 1 unit.\n'
        'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n\n'
        f"Reminder, this is what your maze looks like:\n{progMap}\n\n"
        "Find a path through the castle using the commands! 7s will represent your carved path.\n"
        f"You will start at the top left corner of the maze."
    )
    return grid, progMap, player_x, player_y

def UI_run(player_x, player_y):
    global grid, progMap, currentMapNum, progressMade
    win = False
    #continuous input dependent on if the player wins or not
    while win == False:
        i = input("\nWhat would you like to do? (move/save): ").lower()
        if 'move' in i:
            direction = input("Which direction would you like to go? (north/south/east/west): ")
            x, y = player_x, player_y
            if direction == "east":
                distMoved = setLocation(x, y + 1, grid, progMap)
            elif direction == "west":
                distMoved = setLocation(x, y - 1, grid, progMap)
            elif direction == "south":
                distMoved = setLocation(x + 1, y, grid, progMap)
            elif direction == "north":
                distMoved = setLocation(x - 1, y, grid, progMap)
            else:
                print("\nInvalid direction. Please try again.")
                continue

            player_x, player_y = getCurrentLocation()

            if distMoved == False:
                print(f"\nYou cannot move there, your location is still {getCurrentLocation()}.")
            elif grid[player_x][player_y] == 3:
                if guard_found():
                    print(f"\nMoved a unit {direction}")
                    progMap[player_x][player_y] = 7
                    print(f"Your current location is {getCurrentLocation()} and current progress map is {progMap}.")
                else:
                    win = True
            else:
                print(f"\nMoved a unit {direction}.")
                progMap[player_x][player_y] = 7
                print(f"Your current location is {getCurrentLocation()} and current progress map is {progMap}.")

        elif "save" in i:
            savingGame(player_x, player_y, grid, progMap)
            return

        elif "print" in i:
            print(grid)

        if grid[player_x][player_y] == 2:
            print(f"You found the exit!\nThe actual maze was {grid}\n")
            print('Congratulations! You have escaped this castle level.\n')
            open('lastGameSaved.json', 'w').close() #clears the last saved game
            win = True

    if progressMade and currentMapNum < 5:
        currentMapNum += 1
        print(f"You have leveled up to map {currentMapNum}. ")
        grid = load_map(f"map{currentMapNum}.txt")
        progMap = print_map(grid)
        player_x, player_y = 0, 0
        print(player_x, player_y, getCurrentLocation())
        print(f"Your maze looks like this: {progMap}")
        UI_run(player_x, player_y)
    elif progressMade and currentMapNum == 5:
        print("Congrats! You have completed all of the pre-built levels.")


if __name__ == "__main__":
    print("Welcome to Medieval Math Mayhem, a text-based math adventure game!\n")
    startTime = time.time()
    print(f"Your start time is {time.ctime(startTime)}")
    grid, progMap, player_x, player_y = selectMap()
    UI_run(player_x, player_y)
    endTime = time.time()
    print(f"Your end time is {time.ctime(endTime)}")
    timePlayed = round(endTime - startTime, 2)
    mins = int(timePlayed // 60)
    secs = int(timePlayed % 60)
    if mins > 0:
        print(f"It has taken you {mins} minutes {secs} seconds to play the game.")
    else:
        print(f"It has taken you {secs} seconds to play the game.")
    print("Thanks for playing!\nRestart to play again.")
