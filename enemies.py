from movement_functions import player_x, player_y
import random

first_num = 0
operation = "+"
second_num = 0
solution = 0

def generate_problem() -> str:
    operations: list = ["+", "-", "*"]
    first_num = random.randint(1, 12)
    operation = random.choice(operations)
    second_num = random.randint(1, 12)
    if operation == "+":
        solution = first_num + second_num
    elif operation == "-":
        solution = first_num + second_num
    else:
        solution = first_num + second_num
    return str(first_num + " " + operation + " " + second_num)

def guard_found() :
    if map[player_y][player_x] == 3:
        print("You have encountered a guard. If you can correctly answer this problem for him, you may pass \n"
              "through. If not, you will be sent to the dungeon... \n\n\n Here is your problem: " + generate_problem)
        ### Call to open guard image function here
        answer = input("Answer :")
        if answer == solution:
            print("Yay!")