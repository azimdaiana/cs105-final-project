from typing import List
from Logic import precondition
from random import randint, choice
from graphics import graphic


def load_map(fileName: str) -> List[List[int]]:
    """
    converts info stored in a txt file into a list that will be used as a maze for a user
    :param fileName: takes in a txt file that has a maze written in
    :return: returns the maze in a list of lists
    """

    file = open(fileName, "r")
    if type == "2D":
        file.readlines()
    firstLine = file.readline() #reads the dimensions
    # print(firstLine)
    rows, cols = map(int, firstLine.split("x")) #splits the first line using the x to parse the dimensions and converts to ints
    grid = []

    for i in range(rows):
        line = file.readline().strip()
        row = []
        for char in line:
            row.append(int(char)) #converts the row into ints and creates a list(row) of int
        grid.append(row) #appends the rows into the matrix
    file.close()
    return grid

def randomMaze(rows:int, cols:int) -> List[List[int]]:
    """
    generates a random maze based on the inputs of dimensions, the maze is characterized by 0 = walls, 1 = walking path, 3 = battles/enemies, 2 = end state
    :param rows: # of rows in a maze
    :param cols: # of columns in a maze
    :return: returns a matrix/maze stored in a list of lists
    """
    grid: List[List[int]] = [] #empty map
    for i in range(rows): #create an empty map of only 0s (walls)
        row = []
        for j in range(cols):
            row.append(0)
        grid.append(row)

    #starting points
    currentCol = randint(0, cols-1)
    currentRow = 0
    grid[currentRow][currentCol] = 1 #the start
    path = [(currentRow, currentCol)] #initiating a path

    #creating a path through the map
    while currentRow < rows - 1:
        direction = choice(["down", "left", "right"]) #randomly choose a direction
        if direction == "down" and currentRow + 1 < rows:
            currentRow += 1
        elif direction == "left" and currentCol > 0:
            currentCol -= 1
        elif direction == "right" and currentCol < cols - 1:
            currentCol += 1
        grid[currentRow][currentCol] = 1 #updates the 0 at the location to a 1
        path.append([currentRow, currentCol]) #saves the path to the goal

    grid[currentRow][currentCol] = 2 #indicate the end goal

    #adding battles on the path
    if cols > 5: #randomizes the number of battles depending on the size of the map
        numBattles = randint(4, cols+1)
    else:
        numBattles = randint(2, cols+1)

    battlePosPoss = path[:-1]  # possible enemy locations

    for i in range(numBattles):
        if battlePosPoss:
            battlePos = choice(battlePosPoss) #randomized battle position
            battleRow = battlePos[0]
            battleCol = battlePos[1]
            grid[battleRow][battleCol] = 3 #position of the battle
            battlePosPoss.remove(battlePos) #removes the possibility of a repeat

    grid[0][0] = 1
    return grid

def print_map(map):
    """
    :param map:
    :return:
    """
    player_map = []

    for i in map:
       f = []
       for l in i:
           if l == 0 or l ==7:
               f.append(l)
           else:
               f.append(0)
       player_map.append(f)
    return player_map

player_x = 0
player_y = 0

def canGoEast(x: int, grid) -> bool:
    if grid[player_y][x] == 0:
        return False
    else:
        return True


def canGoWest(x: int, grid) -> bool:
    if grid[player_y][x] == 0:
        return False
    else:
        return True


def canGoNorth(y: int, grid) -> bool:
    if grid[y][player_x] == 0:
        return False
    else:
        return True


def canGoSouth(y: int, grid) -> bool:
    if grid[y][player_x] == 0:
        return False
    else:
        return True


def goEast(x: int, progMap):
    global player_y, player_x
    for i in range(abs(player_x - x)):
        progMap[player_y][player_x + i] = 7
    player_x = x
    return player_x


def goWest(x: int, progMap):
    global player_y, player_x
    for i in range(abs(player_x - x)):
        progMap[player_y][player_x - i] = 7
    player_x = x
    return player_x


def goNorth(y: int, progMap):
    global player_y, player_x
    for i in range(abs(player_y - y)):
        progMap[player_y - i][player_x] = 7
    player_y = y
    return player_y


def goSouth(y: int, progMap):
    global player_y, player_x
    for i in range(abs(player_y - y)):
        progMap[player_y + i][player_x] = 7
    player_y = y
    return player_y


def getCurrentLocation() -> tuple:
    location: tuple = (player_x, player_y)
    return location


def setLocation(x: int, y: int, grid, progMap)-> bool:
    precondition(x == player_x or y == player_y)
    if x < 0 or y < 0:
        print("Please input a positive index.")
    elif x > player_x:
        if canGoEast(x, grid):
            print("Moved " + str(abs(player_x - x)) + " units east.")
            goEast(abs(player_x - x), progMap)
            return True
        else:
            return False

    elif x < player_x:
        if canGoWest(x, grid):
            print("Moved " + str(abs(player_x - x)) + " units west.")
            goWest(abs(player_x - x), progMap)
            return True
        else:
            return False


    elif y < player_y:
        if canGoNorth(y, grid):
            print("Moved " + str(abs(player_y - y)) + " units north.")
            goNorth(abs(player_y - y), progMap)
            return True
        else:
            return False

    elif y > player_y:
        if canGoSouth(y, grid):
            print("Moved " + str(abs(player_y - y)) + " units south.")
            goSouth(abs(player_y - y), progMap)
            return True
        else:
            return False
    progMap[player_y][player_x] = 7

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


# guard_found(load_map("map2.txt"), 1, 3)