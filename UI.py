import blessed
import time
from utilities import load_map, print_map, randomMaze, getCurrentLocation, setLocation, guard_found, generate_problem, loadSavedGame, savingGame, goalReached, resetCurrentLocation

term = blessed.Terminal()

currentMapNum = 1
progressMade = False
grid = None
s = None

def selectMap():
    """
    starts the game by allowing player to input which map they would like. Uses load_map to set 'grid' to desired map
    :return: grid, progMap, the user's current location coordinates
    """
    global player_x, player_y, currentMapNum, progressMade, grid, s
    print(
        "Choose a number on how you would like to play the game: \n"
        "1. Progress through pre-built maps (map1 -> map5)\n"
        "2. Generate a random map\n"
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
                  f"Current location: ({player_y+1}, {player_x+1})\n")
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
        'You are currently trapped in a castle and must find your way out. To move, you must choose a direction (north, south, west, or east) to move a unit.\n'
        'However, beware of the guards positioned throughout the castle. They might challenge you to a battle!\n\n'
        "Find a path through the castle using the commands! 7s will represent the places you have been and Y is your current location.\n"
    )
    return grid, progMap, player_x, player_y

def draw_map(progMap, player_x, player_y):
    """

    :param progMap: map displayed to the user
    :param player_x:  row coord
    :param player_y: column coord
    :return: visually comprehensible maze with user's position as a green Y
    """
    for y, row in enumerate(progMap):
        line = ""
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                line += term.on_black + term.green + term.reverse + "Y" + term.normal
            else:
                line += str(cell)
        print(term.move(y + 2, 2) + line)


def UI_run():
    global grid, progMap, currentMapNum, progressMade, player_y, player_x, s
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        win = False
        #continuous input dependent on if the player wins or not
        while win == False:
            print("This is your current map:")
            if s == "3":
                draw_map(progMap, player_x, player_y)
            else:
                draw_map(progMap, player_y, player_x)

            i = input(term.move(len(grid) + 6, 2) + "> What would you like to do? (move/save): ").lower()
            if 'move' in i:
                direction = input(term.move(len(grid) + 6, 2) + "> Which direction would you like to go? (north/south/east/west): ").lower()
                x, y = player_x, player_y
                if direction == "east":
                    distMoved = setLocation(x, player_x, y + 1, player_y, grid, progMap)
                elif direction == "west":
                    distMoved = setLocation(x, player_x, y - 1, player_y, grid, progMap)
                elif direction == "south":
                    distMoved = setLocation(x + 1, player_x, y, player_y, grid, progMap)
                elif direction == "north":
                    distMoved = setLocation(x - 1, player_x, y, player_y, grid, progMap)
                else:
                    print("\nInvalid direction. Please try again.")
                    continue

                player_x, player_y = getCurrentLocation()

                if distMoved == False:
                    print(f"\nYou cannot move there.")
                elif grid[player_x][player_y] == 3:
                    if guard_found():
                        print(f"\nMoved a unit {direction}.")
                    else:
                        win = True
                        progressMade = False
                elif grid[player_x][player_y] == 2:
                    draw_map(progMap, player_y, player_x)
                    goalReached(grid)

                    win = True
                else:
                    print(f"\nMoved a unit {direction}.")

            elif "save" in i:
                savingGame(player_x, player_y, grid, progMap)
                return

            elif "print" in i: #cheat key
                print(grid)

        if progressMade and currentMapNum < 5:
            currentMapNum += 1
            print(f"You have leveled up to map {currentMapNum}. ")
            grid = load_map(f"map{currentMapNum}.txt")
            progMap = print_map(grid)
            player_x, player_y = 0, 0
            resetCurrentLocation()
            UI_run()
        elif progressMade and currentMapNum == 5:
            print("Congrats! You have completed all of the pre-built levels.")


if __name__ == "__main__":
    print("Welcome to Medieval Math Mayhem, a text-based math adventure game!\n")
    startTime = time.time()
    print(f"Your start time is {time.ctime(startTime)}")
    grid, progMap, player_x, player_y = selectMap()
    UI_run()
    endTime = time.time()
    print(f"\nYour end time is {time.ctime(endTime)}")
    timePlayed = round(endTime - startTime, 2)
    mins = int(timePlayed // 60)
    secs = int(timePlayed % 60)
    if mins > 0:
        print(f"It has taken you {mins} minutes {secs} seconds to play the game.")
    else:
        print(f"It has taken you {secs} seconds to play the game.")
    print("\nThanks for playing!\nRestart to play again.")
