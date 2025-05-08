from movementFunctions import getCurrentLocation
from movementFunctions import grid
import json
# from enemies import riddles_solved

def savingGame(player_x, player_y, grid, progMap):
    prevPlay = {
            "lastLoc": [player_y, player_x],
            "grid": grid,
            "progMap": [progMap],
        }

    with open('lastGameSaved.json', 'w') as lastGame:
        json.dump(prevPlay, lastGame)
    print("Game has been saved successfully. Come back soon to continue where you left off!")
