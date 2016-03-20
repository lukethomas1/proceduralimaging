#!/usr/bin/env python
#! python3

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

import create

# Variables for RGB colors, start at 0 for while loop conditionals
rgb = [0, 0, 0]

# Variables for dimensions of image
width = 0;
height = 0;

# Volatility, the amount the colors change each cycle
changeAmount = 0;

# Used for user specifications
rgbOption = ""
settingsOption = ""
separateVariance = True
overlap = False

# For valid input checks
valid = False

######## Make sure the images folder and text file exist ########


if(not exists('./images/')):
    makedirs('./images/')

######## User Inputted Image Specifications ########


while input("Type any key to create a picture or q to quit: ") != "q":
    # Identify python keyboard interrupt for user
    print("Ctrl + C to exit")

    # Get valid height and width input from user
    while(True):
        try:
            width = int(input("Enter a width: "))
            height = int(input("Enter a height: "))
            changeAmount = int(input("Enter volatility: "))
            # Ask if user wants to specify starting RGB values or randomize
            rgbOption = input("Starting RGB values, (r)andom or (c)ustom: ")
            settingsOption = input("Settings: (d)efault or (c)ustom? ")
            imageAmount = int(input("How many images would you like to" +
                                    " create? "))

            if((rgbOption != "r" and rgbOption != "c") or
               (settingsOption != "d" and settingsOption != "c")):
                raise ValueError()
            valid = True
            break;
        except Exception:
            print("Invalid width or height")

    rgb = create.InitialColors(rgbOption)
    settings = create.ImageSettings(settingsOption)
    overlap = settings[0]
    separateVariance = settings[1]

    ######## Creating the image ########

    # Find the next batch number
    index = 1
    while(exists('./images/batch' + str(index))):
        index += 1
    batch = './images/batch' + str(index)
    makedirs(batch)

    for number in range(1, imageAmount + 1):
        img = create.NewImage(width, height, rgb, changeAmount,
                              separateVariance, overlap)
        img.save(batch + '/' + str(number) + '.bmp')