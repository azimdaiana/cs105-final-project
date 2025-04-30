from movementFunctions import player_x, player_y
from loadingMaps import load_map
import random
from graphics import graphic

def generate_problem() -> str:
    operations: list = ["+", "-", "*"]
    first_num = randint(1, 12)
    operation = choice(operations)
    second_num = randint(1, 12)
    if operation == "+":
        solution = first_num + second_num
    elif operation == "-":
        solution = first_num - second_num
    else:
        solution = first_num * second_num
    return str(first_num) + " " + operation + " " + str(second_num), int(solution)

def guard_found(grid, player_y, player_x):
    if grid[player_y][player_x] == 3:
        problem, solution = generate_problem()
        print(graphic("guard.jpg", 25))
        print("You have encountered a guard. If you can correctly answer this problem for him, you may pass \n"
              "through. If not, you will be sent to the dungeon... \n\n\nHere is your problem: " + problem)
        answer = input("Answer: ")
        if int(answer) == solution:
            print("Yay! You are free to continue!")
        else:
            print("Off to the dungeon.")
            print(graphic("images.jpeg", 100))


guard_found(load_map("map2.txt"), 1, 3)