from movementFunctions import getCurrentLocation
from userInterface import uni_map
from import riddles_solved
import matplotlib as plt


prevPlay = {
    "lastLoc": getCurrentLocation,
    "map": uni_map,
    "riddlesSolved": riddles_solved
}

lastGame = open("lastGameSaved", "w")
lastGame.open()
lastGame.write(prevPlay)
lastGame.close()

from PIL import Image
img = Image.open("jail.jpg")
plt.imshow(img)
plt.show()