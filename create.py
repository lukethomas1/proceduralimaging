#!/usr/bin/env python3

# Author: Luke Thomas
# Date: March 3, 2016

from PIL import Image
from random import randint

RED = 0
GREEN = 1
BLUE = 2
MAX_COLOR = 255

def InitialColors(rgbOption):
    rgb = [0, 0, 0]

    # Random RGB values
    if(rgbOption == "r"):
        for color in range(0, len(rgb)):
            rgb[color] = randint(0, MAX_COLOR)

    # Custom RGB values, take in user input
    elif(rgbOption == "c"):
        # Loop until user gives valid input
        while(True):
            try:
                rgb[RED] = int(input("Enter a red value: "))
                rgb[GREEN] = int(input("Enter a green value: "))
                rgb[BLUE] = int(input("Enter a blue value: "))
                break
            except Exception:
                print("Invalid input, try again")
    return rgb


def ImageSettings(settingsOption):
    # Default Settings
    settings = [False, True]

    if(settingsOption == "c"):
        while(True):
            try:
                settings[0] = int(input("Enter (1) for overlap, (0) for no " +
                                    "overlap: "))
                settings[1] = int(input("Enter (1) for separate variance" +
                                             ", (0) for no separate variance: "))
                break
            except Exception:
                print("Invalid input, try again.")
    return settings


def NewImage(width, height, rgbCopy, changeAmount, separateVariance, overlap):
    # Deep copy rgb values to avoid modifying the original array
    rgb = [0, 0, 0]
    for color in range(0, len(rgb)):
        rgb[color] = rgbCopy[color]

    # Create a new image
    img = Image.new('RGB', (width, height), "black")

    # Get the pixels of the image
    pixels = img.load()

    # Draw the image
    for column in range(img.size[1]):
        for row in range(img.size[0]):
            # Set the color of the pixel
            pixels[row, column] = (rgb[RED], rgb[GREEN], rgb[BLUE])

        # Each color varies a separately
        if(separateVariance):
            for color in range(0, len(rgb)):
                # Change color slightly based on volatility
                rgb[color] += randint(-changeAmount, changeAmount)

                # Dont let color go over 255 value
                if(rgb[color] > MAX_COLOR):
                    rgb[color] = MAX_COLOR
                elif(rgb[color] < 0):
                    rgb[color] = 0

        # Each color varies by the same amount
        else:
            amount = randint(-changeAmount, changeAmount)
            for color in range(0, len(rgb)):
                rgb[color] += amount

        # If a color reaches max value (255), will be set to 0
        if(overlap):
            for color in range(0, len(rgb)):
                rgb[color] = rgb[color] % MAX_COLOR
    return img