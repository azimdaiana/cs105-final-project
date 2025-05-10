import blessed
import time
from utilities import (
    load_map, print_map, randomMaze, getCurrentLocation, setLocation,
    guard_found, generate_problem, loadSavedGame, savingGame, goalReached, resetCurrentLocation
)

term = blessed.Terminal()

currentMapNum = 1
progressMade = False

def selectMap():
    return load_map(currentMapNum)

def draw_map(grid, player_x, player_y, message=""):
    print(term.home + term.clear)
    print(term.bold("== Medieval Math Mayhem =="))

    for y, row in enumerate(grid):
        line = ""
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                line += term.reverse("P")  # Highlight player
            else:
                line += cell
        print(term.move(y + 2, 2) + line)

    print(term.move(len(grid) + 4, 2) + term.yellow("Enter direction (north, south, east, west) or 'q' to quit:"))
    if message:
        print(term.move(len(grid) + 5, 2) + term.cyan(f"{message}"))

def UI_run():
    grid, progMap, player_x, player_y = selectMap()
    message = "Welcome to the dungeon!"

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            draw_map(grid, player_x, player_y, message)
            print(term.move(len(grid) + 6, 2) + "> ", end="", flush=True)
            direction = input().strip().lower()

            if direction == 'q':
                break

            new_x, new_y = player_x, player_y
            if direction == "north":
                new_y -= 1
            elif direction == "south":
                new_y += 1
            elif direction == "east":
                new_x += 1
            elif direction == "west":
                new_x -= 1
            else:
                message = "Invalid direction. Try again."
                continue

            # Check map boundaries
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] != "#":
                player_x, player_y = new_x, new_y
                setLocation(player_x, player_y)

                # Check for guard
                if guard_found(player_x, player_y, progMap):
                    correct = generate_problem()
                    if correct:
                        message = "Correct! You defeated the guard."
                        progMap[player_y][player_x] = "X"  # Mark cleared
                    else:
                        message = "Wrong! You are sent back to start."
                        player_x, player_y = 1, 1  # Reset position
                        setLocation(player_x, player_y)

                if goalReached(player_x, player_y, grid):
                    message = "🎉 You reached the goal! Congrats!"
                    break
                else:
                    message = "You moved."

            else:
                message = "You can't go that way."

    print(term.normal + "\nThanks for playing!")

# Main
if __name__ == "__main__":
    print(term.clear + term.move(0, 0))
    print("Welcome to Medieval Math Mayhem, a text-based math adventure game!\n")
    startTime = time.time()
    print(f"Your start time is {time.ctime(startTime)}")

    UI_run()

    endTime = time.time()
    print(f"\nYour end time is {time.ctime(endTime)}")
    timePlayed = round(endTime - startTime, 2)
    mins = int(timePlayed // 60)
    secs = int(timePlayed % 60)
    if mins > 0:
        print(f"It took you {mins} minutes {secs} seconds to play the game.")
    else:
        print(f"It took you {secs} seconds to play the game.")
    print("Thanks for playing!\nRestart to play again.")
