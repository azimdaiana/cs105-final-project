from typing import List
from random import randint, choice
from progressiveMap import print_map

#print(print_map("map1.txt"))

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

    grid[currentRow][currentCol] = 2 #indicate the end goal

    return grid
#add a rando number for an enemey
#print(randomMaze(3, 5))
