#!/usr/bin/env python

# Author: Luke Thomas
# Date: March 3, 2016

# Description: This program takes in user input to create randomly generated
# pixel-painted images. Also has functionality to create a single image and
# save it with a specific name, or create a bulk group of images with numbered
# names.

from PIL import Image
from random import randint
from os.path import isfile, exists
from os import makedirs

# Variables for RGB colors, start at 0 for while loop conditionals
red = 0
green = 0
blue = 0

# Variables for dimensions of image
width = 0;
height = 0;

# Volatility, the amount the colors change each cycle
changeAmount = 0;

# For valid input checks
valid = False

######## Make sure the images folder and text file exist ########


if(not exists('./images/')):
    makedirs('./images/')
if(not isfile('./images/images.txt')):
    file = open('./images/images.txt', 'a')
    file.write('1')
    file.close()
    
######## User Inputted Image Specifications ########


while input("Type any key to create a picture or q to quit: ") != "q":
    # Identify python keyboard interrupt for user
    print("Ctrl + C to exit")

    # Get valid height and width input from user
    while(1):
        try:
            width = int(input("Enter a width: "))
            height = int(input("Enter a height: "))
            changeAmount = int(input("Enter volatility: "))
            valid = True
            break;
        except Exception:
            print("Invalid width or height")

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


    ######## Creating the image ########

    
    def create_image(red, green, blue):
        # Create a new image
        img = Image.new('RGB', (width, height), "black")

        # Get the pixels of the image
        pixels = img.load()

        # Draw the image
        for column in range(img.size[1]):
            for row in range(img.size[0]):
                pixels[row, column] = (red, green, blue) # set the colour accordingly
            red += randint(-changeAmount, changeAmount)
            green += randint(-changeAmount, changeAmount)
            blue += randint(-changeAmount, changeAmount)
        return img

    numImages = int(input("How many of these images would you" +
                            " like to create? "))
    # Bulk images, save without asking to default names
    if numImages > 1:
        # To be used to name each picture
        nextSaveNumber = 0
        
        # Get the starting number to save the images as
        saveTrackerFile = open('./images/images.txt', 'r+')

        # Try getting the next save number automatically
        try:
            nextSaveNumber = int(saveTrackerFile.read()) + 1

        # Threw an error, get the save number manually
        except Exception:
            # Loop until valid user input
            while(1):
                try:
                    nextSaveNumber = int(input("Auto save failed, enter manual" +
                                               " starting save number: "))
                    break
                except Exception:
                    print("Invalid input, try again.")
        
        # Create the amount of images specified
        for number in range(0, numImages):
            # Create the next image
            nextImage = create_image(red, green, blue)
            
            while isfile('./images/' + str(nextSaveNumber) + '.bmp'):
                nextSaveNumber += 1
                
            nextImage.save('./images/' + str(nextSaveNumber) + '.bmp')
            nextSaveNumber += 1
            
        # Modify the save file to show the correct next save name and close it
        saveTrackerFile.seek(0)
        saveTrackerFile.write(str(nextSaveNumber))
        #saveTrackerFile.truncate()
        saveTrackerFile.close()

    elif numImages == 1:
        # Create and preview image for user
        img = create_image(red, green, blue)
        img.show()
        
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
                    if(isfile('./images/' + fileName)):
                       print("That file name is already taken.")

                    # File doesn't exist, save it to the fileName specified
                    else:
                        img.save('./images/' + fileName)
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
