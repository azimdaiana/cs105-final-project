from PIL import Image

#code below is a modified version of https://medium.com/@kernel.rb/bring-your-images-to-life-in-text-a-guide-to-python-based-ascii-art-79ac8f0b3c64

#resizing the img to fit the terminal
def resizeImg(image, newWidth):
    width, height = image.size
    ratio = height / width
    newHeight = int(newWidth * ratio * 0.55) #height adjusted for terminal
    return image.resize((newWidth, newHeight))

#convert img to grayscale
def pixelToGrayscale(image):
    return image.convert("L")  # "L" mode for grayscale

#map each pixel in the img to an ASCII char
ASCIICHAR = "@%#*+=-:. "
def pixelToAscii(image):
    pixels = image.getdata()
    asciiStr = ""
    for pixel_value in pixels:
        index = pixel_value * (len(ASCIICHAR) - 1) // 255
        asciiStr += ASCIICHAR[index]
    return asciiStr

def graphic(image, newWidth):
    try:
        image = Image.open(image)
    except:
        print("unable to open image")
        return

    # Convert to grayscale and ASCII art
    grayscaleImg= pixelToGrayscale(resizeImg(image, newWidth))
    newImgPixels = pixelToAscii(grayscaleImg)

    asciiImg = "\n".join(newImgPixels[i:i + newWidth] for i in range(0, len(newImgPixels), newWidth))

    return asciiImg  # Print the ASCII art to the console

    # try:
    #   with open("asciiArt.txt", "w") as c:
    #     try:
    #       c.write(asciiImg)
    #     except Exception as e:
    #       print(f"Error while writing to the file: {e}")
    # except Exception as e:
    #   print(f"Error while opening the file: {e}")

# print(graphic("guard.jpg", 25))