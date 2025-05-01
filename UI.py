import blessed
from utilities import load_map, print_map, randomMaze, getCurrentLocation, setLocation, guard_found, generate_problem

term = blessed.Terminal()

#TODO
# def save():
#     s = uni_map
#     return s
# save1 = save()

#function selectMap starts the game by allowing player to input which map they would like. Uses load_map to set 'grid' to desired map
def selectMap():
    s = input("Welcome to ZORK, a text based adventure game.\nPlease select your map: map1, map2, map3, map4, map5, save. Or input map6 to generate your own map\n")
    if s == 'map1':
        grid = load_map('map1.txt')
    if s == 'map2':
        grid = load_map('map2.txt')
    if s == 'map3':
        grid = load_map('map3.txt')
    if s == 'map4':
        grid = load_map('map4.txt')
    if s == 'map5':
        grid = load_map('map5.txt')
    if s == 'map6':
        r = int(input('how many rows will your grid have?'))
        c = int(input('how many columns will your grid have'))
        grid = randomMaze(r,c)
    print(f'You have selected a map that is {len(grid)}x{len(grid[0])} dimensions')
    return grid

grid = selectMap()
progMap = print_map(grid)

print('You are in a castle, trying to find your way out. You can use commands like: north, south, west, east with the number of units you want to move.\n'
      'However, beware of the guards guarding the castle, they might challenge you to a battle!\n'
      'Get ready, the game is about to launch!'
      f"Reminder, this is what your maze looks like {progMap} \n"
      "There is a hidden walkable path that you have to figure out using trial and error, and of course the commands!\n"
      "You will start at the top left corner of the maze.\n"
      )

p_x = getCurrentLocation()[0]
p_y = getCurrentLocation()[1]
def UI_run():
    win = False
    #continuous input dependent on if the player wins or not
    while win == False:
        i = str(input()).lower()
        if 'move' in i:
            direction = input("Which direction would you like to go? (north/south/east/west)\n")
            distance = int(input("How many units would you like to move? (please enter a numerical value)\n"))

            if direction == "west" or direction == "east":
                distMoved = setLocation(distance, 0, grid, progMap)
            if direction == "south" or direction == "north":
                distMoved = setLocation(0, distance, grid, progMap)

            if "Cannot" in distMoved:
                print(f"You have not moved, your location is still {getCurrentLocation()}")
            else:
                print(f"Your current location is {getCurrentLocation()}\n"
                      f"Your current progress map is {progMap}")
        if grid[p_x][p_y] == 2:
            print('you have defeated this level!!')
            win = True
    print(f"Your current location is {getCurrentLocation()}")

    #add continuous prompting so the UI doesn't just end the game
    #p = input()
    #if move in p: (set direction and distance/continue movement conditionals)

    player_x = 0
    player_y = 0
    # print(progMap)

    key_words = ['print', 'move', 'save']
    if 'print' in i:
        print(print_map(grid))


UI_run()


# def UI_start():
#     with term.location(0, 10):
#         print('Welcome to ZORK, a text-based adventure game.\nPlease select your map: map1, map2, map3, map4, map5')
#         s = input()
#         if s == 'map1':
#             uni_map = load_map('map1.txt')
#
#
# print(UI_start())

# #sample code
# progress = input("Would you like to save your progress?(yes/no)")
# if progress == "yes":
#     print(savingGame())
#
# else:
#     pass #start a new game