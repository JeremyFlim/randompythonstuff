from random import *
from tkinter import *

__run__ = True

def game():
    print("Welcome to the gambler's ruin simulation!\nPlease refrain from putting numbers that are too high because it will take a long time!")

    money = int(input("Input the starting money... "))

    goal = int(input("Input the goal... "))

    games = int(input("Input the number of simulations to run... "))

    winChance = int(input("Input a win chance out of 100... "))

    winChance = winChance/100

    gamesDone = 0
    timesLost = 0
    timesWon = 0
    steps = 0

    coinFlip = False

    while gamesDone < games:
        stake = money
        while stake > 0 and stake < goal:
            seed(random())
            if random() < winChance:
                stake = stake + 1
            else:
                stake = stake - 1
        if stake >= goal:
            timesWon += 1
        gamesDone+=1
        print("Game " + str(gamesDone) + " finished...")

    print("You won %s times and lost %s times!" % (timesWon,games - timesWon))

    percentageWin = (timesWon/gamesDone)*100

    print("Your game had a percentage winrate of %s!" % percentageWin)
    retry()

def retry():
    print("Would you like to run more simulations?\nType Y to continue, type anything else to exit...")
    retryChoice = input()
    if retryChoice.lower() == "y":
        game()
    else:
        exit()

if __run__ == True:
    game()

