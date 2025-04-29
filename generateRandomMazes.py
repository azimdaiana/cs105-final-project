from typing import List
from random import randint, choice

def randomMaze(rows:int, cols:int) -> List[List[int]]:
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

    return grid

