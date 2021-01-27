# The Dice Roll Simulation can be done by choosing a random integer between 1 and 6 for which we can use the random module

#importing module for random number generation
import random

# range of the values of a dies
minVal = 1
maxVal = 6

#to loop the rolling through user input
rollAgain = "yes"

# loop
while rollAgain == "yes" or rollAgain == "y":
    print("Rolling The Dices...")
    print("The Values are : ")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(minVal, maxVal))

    # generating and printing 2nd random integer from 1 to 6
    print(random.randint(minVal, maxVal))

    # asking user to roll the dice again. Any input other than yes or y will terminate the loop
    rollAgain = input("Roll the Dices Again?")