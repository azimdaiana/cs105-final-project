from movementFunctions import getCurrentLocation
from movementFunctions import grid
import json
# from enemies import riddles_solved

def savingGame():
    prevPlay = {
            "lastLoc": getCurrentLocation(),
            "grid": grid,
            # "progMap": uni_map,
        }

    with open('lastGameSaved.json', 'w') as lastGame:
        json.dump(prevPlay, lastGame)

