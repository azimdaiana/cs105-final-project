from typing import List
from Logic import precondition
from random import randint, choice
from PIL import Image
import json

def load_map(fileName: str) -> List[List[int]]:
    """
    converts info stored in a txt file into a list that will be used as a maze for a user
    :param fileName: takes in a txt file that has a maze written in
    :return: returns the maze in a list of lists
    """

    file = open(fileName, "r")
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
        grid.append([0] * cols)

    #starting points
    currentCol = 0
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
        if grid[currentRow][currentCol] == 0:
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

def canGoEast(y: int, grid) -> bool:
    global player_x, player_y
    if y < 0 or y >= len(grid[0]):
        print(f"\nMoving in this direction would be out of bound. Please try a different direction.")
        return False
    if grid[player_x][y] == 0:
        return False
    else:
        return True

def canGoWest(y: int, grid) -> bool:
    global player_x, player_y
    if y < 0 or y >= len(grid[0]):
        print(f"\nMoving in this direction would be out of bound. Please try a different direction.")
        return False
    if grid[player_x][y] == 0:
        return False
    else:
        return True

def canGoNorth(x: int, grid) -> bool:
    global player_x, player_y
    if x < 0 or x >= len(grid):
        print(f"\nMoving in this direction would be out of bound. Please try a different direction.")
        return False
    if grid[x][player_y] == 0:
        return False
    else:
        return True

def canGoSouth(x: int, grid) -> bool:
    global player_x, player_y
    if x < 0 or x >= len(grid):
        print(f"\nMoving in this direction would be out of bound. Please try a different direction.")
        return False
    if grid[x][player_y] == 0:
        return False
    else:
        return True

def goEast(y: int, progMap):
    global player_y, player_x
    for i in range(abs(player_y - y)):
        progMap[player_x][player_y + i] = 7
    player_y = y

def goWest(y: int, progMap):
    global player_y, player_x
    for i in range(abs(player_y - y)):
        progMap[player_x][player_y - i] = 7
    player_y = y

def goNorth(x: int, progMap):
    global player_y, player_x
    for i in range(abs(player_x - x)):
        progMap[player_x - i][player_y] = 7
    player_x = x

def goSouth(x: int, progMap):
    global player_y, player_x
    for i in range(abs(player_x - x)):
        progMap[player_x + i][player_y] = 7
    player_x = x

player_x = 0
player_y = 0

def getCurrentLocation() -> tuple:
    global player_x, player_y
    return (player_x, player_y)

def updateCurrentLocation(newPlayer_x, newPlayer_y):
    global player_x, player_y
    player_x, player_y = newPlayer_x, newPlayer_y
    return (player_x, player_y)

def resetCurrentLocation():
    global player_x, player_y
    player_x, player_y = 0,0
    return (player_x, player_y)

def setLocation(x: int, player_x:int, y: int, player_y:int, grid, progMap)-> bool:
    if precondition(x == player_x or y == player_y) == False:
        print(f"You can only move in a straight line horizontally or vertically!")
        return False
    if x > player_x:
        if canGoSouth(x, grid):
            goSouth(x, progMap)
            return True
        else:
            return False
    elif x < player_x:
        if canGoNorth(x, grid):
            goNorth(x, progMap)
            return True
        else:
            return False
    elif y < player_y:
        if canGoWest(y, grid):
            goWest(y, progMap)
            return True
        else:
            return False
    elif y > player_y:
        if canGoEast(y, grid):
            goEast(y, progMap)
            return True
        else:
            return False

def goalReached(grid):
    if grid[player_x][player_y] == 2:
        print(f"You found the exit and have escaped this castle level.\n")
        open('lastGameSaved.json', 'w').close()  # clears the last saved game

# code for the 4 functions below is a modified version of https://github.com/Kernel-rb/Image2ASCII
def resizeImg(image, newWidth):
    """
    :param image: path file
    :param newWidth: int value
    :return: resized img to fit the terminal
    """
    width, height = image.size
    ratio = height / width
    newHeight = int(newWidth * ratio * 0.55) #height adjusted for terminal
    return image.resize((newWidth, newHeight))
def pixelToGrayscale(image):
    """
    :param image: img path
    :return: converts the img into grayscale
    """
    return image.convert("L")  # "L" mode for grayscale
def pixelToAscii(image):
    """
    :param image: img path
    :return: map each pixel in the img to an ASCII char
    """
    ASCIICHAR = "@%#*+=-:. "
    pixels = image.getdata()
    asciiStr = ""
    for pixel_value in pixels:
        index = pixel_value * (len(ASCIICHAR) - 1) // 255
        asciiStr += ASCIICHAR[index]
    return asciiStr
def graphic(image, newWidth):
    try:
        image = Image.open(image)
    except:
        print("unable to open image")
        return

    # Convert to grayscale and ASCII art
    grayscaleImg= pixelToGrayscale(resizeImg(image, newWidth))
    newImgPixels = pixelToAscii(grayscaleImg)

    asciiImg = "\n".join(newImgPixels[i:i + newWidth] for i in range(0, len(newImgPixels), newWidth))

    return asciiImg  # Print the ASCII art to the console

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

def guard_found():
    # if grid[player_y][player_x] == 3:
        problem, solution = generate_problem()
        print(graphic("guard.jpg", 25))
        print("You have encountered a guard. If you can correctly answer this problem for him, you may pass \n"
              "through. If not, you will be sent to the dungeon... \nHere is your problem: " + problem)
        answer = input("Answer: ")

        try:
            if int(answer) == solution:
                print("Yay! You are free to continue!")
                return True
            else:
                print("Incorrect answer.\nOff to the dungeon. You have failed the game.")
                print(graphic("images.jpeg", 60))
                return False
        except ValueError:
            print("That is not a valid number! Off to the dungeon you go for trying to trick the guard.")
            print(graphic("images.jpeg", 60))
            return False

def savingGame(player_x, player_y, grid, progMap):
    prevPlay = {
            "lastLoc": (player_x, player_y),
            "grid": grid,
            "progMap": progMap,
        }

    with open('lastGameSaved.json', 'w') as lastGame:
        json.dump(prevPlay, lastGame)
    print("Game has been saved successfully. Come back soon to continue where you left off!")

def loadSavedGame():
    with open("lastGameSaved.json", "r") as lastGame:
        prevPlay = json.load(lastGame)
    return prevPlay["lastLoc"], prevPlay["grid"], prevPlay["progMap"]
