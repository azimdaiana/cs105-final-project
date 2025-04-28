from movement_functions import getCurrentLocation

prevPlay = {
    "lastLoc": getCurrentLocation,
    "map": load_map,
    "enemiesDef": enemiesDef
}

lastGame = open("lastGameSaved", "w")
lastGame.open()
lastGame.write(prevPlay)
lastGame.close()