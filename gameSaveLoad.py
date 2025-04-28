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

from PIL import Image
img = Image.open('enemy.png')
# Display the image
img.show()