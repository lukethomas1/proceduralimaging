#!/usr/bin/env python

# Author: Luke Thomas
# Discontinued 3/2/16 after discovery of superior library for python 3.4
# Will port to python 3 and continue development

from PIL import Image
from random import randint
from os.path import isfile

# Identify python keyboard interrupt for user
print("Ctrl + C to exit")

# Get valid height and width input from user
while(1):
    try:
        width = int(input("Enter a width: "))
        height = int(input("Enter a height: "))
        img = Image.new('RGB', (width, height), "black")
        img.save('./pictures/.temp.bmp')
        break;
    except Exception:
        print("Invalid width or height")

# Get the pixels of the image in order to modify later on
pixels = img.load();

# Variables for RGB colors, start at 0 for while loop conditionals
red = 0
green = 0
blue = 0

# Ask if user wants to specify starting RGB values or randomize
userOption = input("Startin RGB values, (r)andom or (c)ustom: ")

# Random RGB values
if userOption == "r":
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

# Custom RGB values, take in user input
elif userOption == "c":
    # Loop until user gives valid input
    while(not red and not green and not blue):
        try:
            red = int(input("Enter a red value: "))
            green = int(input("Enter a green value: "))
            blue = int(input("Enter a blue value: "))
            break
        except Exception:
            print("Invalid input, try again")

# Amount to randomly change RGB values each cycle
changeAmount = 5;

# Create the image
for column in range(img.size[0]):
    for row in range(img.size[1]):
        pixels[row, column] = (red, green, blue) # set the colour accordingly
    red += randint(-changeAmount, changeAmount)
    green += randint(-changeAmount, changeAmount)
    blue += randint(-changeAmount, changeAmount)

# Preview image for the user
# Doesn't work yet
img.show();

# Loop until user gives valid input
while(1):
    saveChoice = input("Would you like to save this image? (y)es or (n)o: ")

    # User wants to save image
    if saveChoice == "y":
        while(1):
            # Get name of file
            fileName = input("What would you like to name the file? ")

            # If user didn't specify a filetype, default to .bmp
            if fileName.find(".") == -1:
               fileName += ".bmp"

            # Check if this file already exists
            if(isfile('./pictures/' + fileName)):
               print("That file name is already taken.")

            # File doesn't exist, save it to the fileName specified
            else:
                img.save('./pictures/' + fileName)
                print("File was successfully save as " + fileName)
                break
        break

    # User doesn't want to save image
    elif saveChoice == "n":
        print("File was not saved.")
        break

    # Input wasn't 'y' or 'n', therefore invalid, get new input
    else:
        print("Invalid input, try again.")

