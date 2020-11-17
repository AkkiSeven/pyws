# Cooking game
# Made on 11/17/2020
#Made by Akshay Madhira

# Importing the required modules
import random
import time
import os

# Creating the intro!
print("Today, you will cook in this fun game!🍳🍪🥘")
time.sleep(5)
os.system('cls')
print("Get tips, get cash, make food(not real food of course!!!)🤣")
time.sleep(6)
os.system('cls')
# Asking the player if he/she wants to play
play = input("Do you want to play(y or n) - ")

# If he/she wants to play, they type the letter 'y', and then this piece of code runs, else, it won't run and go to else statement.
if play.lower() == 'y':
    print("Hi! We are happy you are on this exciting journey!")
    time.sleep(3)
    os.system('cls')
    print("Welcome to CookAlways™!")
    print("░█████╗░░█████╗░░█████╗░██╗░░██╗  ░█████╗░██╗░░░░░░██╗░░░░░░░██╗░█████╗░██╗░░░██╗░██████╗™")
    print("██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██║░░░░░░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝██╔════╝")
    print("██║░░╚═╝██║░░██║██║░░██║█████═╝░  ███████║██║░░░░░░╚██╗████╗██╔╝███████║░╚████╔╝░╚█████╗░")
    print("██║░░██╗██║░░██║██║░░██║██╔═██╗░  ██╔══██║██║░░░░░░░████╔═████║░██╔══██║░░╚██╔╝░░░╚═══██╗")
    print("╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░██║███████╗░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░██████╔╝")
    print("░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░")
    print("Screen will clear in 5 seconds")
    time.sleep(5)
    os.system('cls')
    # Main Game
    your_name = input("Let's start simple. What is your name? (this information will not be stored by any software or server) - ")
    name = your_name
    print("Hello " + name + "!" + " Let's start! No cooking experience required!")
    tip = 0
    cash = 0

# If he/she doesn't want to play, they type the letter 'no', then this piece of code runs
else:
    print("Well, you miss the fun of cooking...😢, but, Bye! Play next time!😁")

# Leaving extra piece of line for nice format!
