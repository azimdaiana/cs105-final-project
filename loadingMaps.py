from typing import List

def load_map(fileName: str) -> List[List[int]]:
    file = open(fileName, "r")
    firstLine = file.readline() #reads the dimensions
    print(firstLine)
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

print(load_map("map1.txt"))
print(load_map("map2.txt"))
print(load_map("map3.txt"))
print(load_map("map4.txt"))
print(load_map("map5.txt"))