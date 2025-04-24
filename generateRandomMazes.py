from typing import List
from random import randint

def randomMaze(rows:int, cols:int) -> List[List[int]]:
    grid: List[List[int]] = []
    for i in range(cols-1):
        row: List[int] = []
        for j in range(rows):
            row.append(randint(0, 1))
        grid.append(row)
    exitRow: List[int] = []
    for k in range(rows-2):
        exitRow.append(randint(0, 1))
        exitRow.append(2)
        exitRow.append(randint(0, 1))
    grid.append(exitRow)
    end = randint(0, rows)
    # grid = grid[end] + [2]
    return grid

print(randomMaze(3, 5))
