from tkinter import Tk, filedialog
import random
import sys
import time
import json
import os

option = 0
run = True
fieldsize = 4
plotnum = [1, 2, 3, 4]
plotplant = ["", "", "", ""]
plotstatus = [0, 1, 0, 0]
invnames = ["Wheat Seed", "Corn Seed", "Soybean Seed", "Tomato Seed", "Potato Seed"]
invcounts = [2, 4, 1, 3, 5]
crops = {"Wheat Seed":"Wheat", "Corn Seed":"Corn", "Soybean Seed":"Soybean", "Tomato Seed":"Tomato", "Potato Seed":"Potato"}
cropprices = {"Wheat":50, "Corn":75, "Soybean":85, "Tomato":90, "Potato":105}
days = 0
money = 1000

Tk().withdraw()
filepath = filedialog.askopenfilename(title="Select your farmconfig.json file")
print("Copyright (C) 2025 Lillian Bailey")
print("This program comes with ABSOLUTELY NO WARRANTY; for details, refer to the LICENSE file")
print("This is free software, and you are welcome to redistribute it under certain conditions.")
if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
    print(f"No usable farm file found at {filepath}")
    print("A new farm will be created and saved there.")
    menuoption = 1
else:
    menuoption = int(input("Would you like to create a new farm (1 for new farm, 2 for existing farm)? "))


def updateShopInv(buyoption):
    if buyoption in invnames:
        buyindex = invnames.index(buyoption)
        invcounts[buyindex] += 1
    else:
        invnames.append(buyoption)
        invcounts.append(1)

if menuoption == 1:
    farmname = input("Enter your farm's name: ")
    config = {
        "farmname": farmname,
        "fieldsize": 4,
        "plotplant": ["", "", "", ""],
        "plotstatus": [0, 0, 0, 0],
        "invnames": ["Wheat Seed", "Corn Seed"],
        "invcounts": [3, 2],
        "days": 0,
        "money": 500
    }
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)
    menuoption = int(input("Would you like to see the tutorial (2 for no, 3 for yes)? "))

    fieldsize = config["fieldsize"]
    plotplant = config["plotplant"]
    plotstatus = config["plotstatus"]
    invnames = config["invnames"]
    invcounts = config["invcounts"]
    days = config["days"]
    money = config["money"]

if menuoption == 3:
    print(f"Welcome to {farmname}!")
    print("Your parents left you with a bit of cash and some seeds to get started!")
    print("You will have 6 options to choose from.")
    time.sleep(1)
    print("View Field | This option will allow you to check on your crops and their stages of growth!")
    print("Plant Crops | This option will allow you to plant crops on empty plots!")
    print("Harvest Crops | This option will allow you to harvest any crop that has fully grown!")
    print("View Inventory | This option will allow you to see all the items in your inventory!")
    print("View Shop | This option will allow you to visit the shop to buy seeds and sell crops!")
    print("Sleep | This option will allow you to end your day on the farm. You will have the chance to save and exit the game at this menu or to return to your farm for another day!")
    time.sleep(8)
    print("When in the shop, enter 'buy' to buy things or 'sell' to sell things!")
    print("When ending the day, you will pay a utilities and taxes bill!")
    print("Try to keep yourself out of bankruptcy!")
    time.sleep(4)
    print("DO NOT EDIT FARMCONFIG.JSON OR IT WILL BREAK THE SCRIPT.")
    print("Good luck! Enjoy your farm!")
    time.sleep(2)
    menuoption = 2

if menuoption == 2:
    with open(filepath, "r") as f:
        config = json.load(f)
    farmname = config["farmname"]
    fieldsize = config["fieldsize"]
    plotplant = config["plotplant"]
    plotstatus = config["plotstatus"]
    invnames = config["invnames"]
    invcounts = config["invcounts"]
    days = config["days"]
    money = config["money"]

while True:
    print("=================")
    print(f"You stand in the middle of {farmname}")
    print(f"It is day {days}")
    print("1) View Field")
    print("2) Plant Crops")
    print("3) Harvest Crops")
    print("4) View Inventory")
    print("5) View Shop")
    print("6) Sleep")

    option = int(input("What would you like to do? "))

    if option == 1:
        # View Field Option
        index = 0
        print("You look into your field of crops..")
        for crop in plotplant:
            if plotplant[index] == "":
                print(f"Plot {index + 1} has nothing growing in it!")
            else:
                print(f"Plot {index + 1} has {crop} growing in it! It is in growth stage {plotstatus[index]}")
            index += 1
    
    if option == 2:
        plantyes = False
        plotchoice = int(input("Pick the plot to plant in: ")) - 1
        if plotplant[plotchoice] != "":
            print("There is already a crop in that plot!")
        else:
            cropchoice = input("Pick a crop from your inventory: ")
            plantyes = True
        if plantyes == True:
            if cropchoice in invnames:
                if invcounts[invnames.index(cropchoice)] > 0:
                    plotplant[plotchoice] = crops[cropchoice]
                    invcounts[invnames.index(cropchoice)] -= 1
                    plotstatus[plotchoice] = 1
            else:
                print("You do not have those seeds!")

    if option == 3:
        harvestindex = 0
        harvestchoice = int(input("Pick the plot to harvest: ")) - 1
        if plotplant[harvestchoice] != "" and plotstatus[harvestchoice] == 3:
            if plotplant[harvestchoice] in invnames:
                harvestindex = invnames.index(plotplant[harvestchoice])
                invcounts[harvestindex] += 1
            else:
                invnames.append(plotplant[harvestchoice])
                invcounts.append(1)
            plotplant[harvestchoice] = ""
            plotstatus[harvestchoice] = 0
        elif plotplant[harvestchoice] != "" and plotstatus[harvestchoice] != 3:
            print("That plot is not ready to be harvested yet!")
        elif plotplant[harvestchoice] == "":
            print("There is nothing growing in this plot!")

    if option == 4:
        invindex = 0
        print("Item | Amount")
        for item in invnames:
            print(f"{item} | {invcounts[invindex]}")
            invindex += 1
        print(f"Your wallet has {money} dollars")

    if option == 5:
        buyindex = 0
        print("Welcome to the market!")
        marketoption = input("Would you like to buy or sell? ")
        if marketoption == "buy" or marketoption == "Buy":
            print("Item | Price")
            print("Wheat Seed | 25")
            print("Corn Seed | 35")
            print("Soybean Seed | 40")
            print("Tomato Seed | 45")
            print("Potato Seed | 50")
            print("Options are CASE SENSITIVE!")
            buyoption = input("Choose your purchase: ")
            if buyoption == "Wheat Seed":
                if money - 25 > 0:
                    updateShopInv(buyoption)
                    money -= 25
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Corn Seed":
                if money - 35 > 0:
                    updateShopInv(buyoption)
                    money -= 35
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Soybean Seed":
                if money - 40 > 0:
                    updateShopInv(buyoption)
                    money -= 40
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Tomato Seed":
                if money - 45 > 0:
                    updateShopInv(buyoption)
                    money -= 45
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Potato Seed":
                if money - 50 > 0:
                    updateShopInv(buyoption)
                    money -= 50
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            else:
                print("Sorry, I couldn't find the item you're looking for!")
        elif marketoption == "sell" or marketoption == "Sell":
            cansell = False
            selllist = []
            sellindex = 0
            for thing in invnames:
                if thing == "Wheat" or thing == "Corn" or thing == "Soybean" or thing == "Tomato" or thing == "Potato":
                    selllist.append(thing)
                    cansell = True
            if cansell == False:
                print("Sorry, you have nothing for me to buy!")
            elif cansell == True:
                print("Item | Sell Price")
                for stuff in range(0, len(selllist)):
                    print(f"{selllist[stuff]} | {cropprices[selllist[stuff]]}")
                sellchoice = input("What would you like to sell? ")
                if sellchoice in selllist:
                    money += cropprices[sellchoice] * invcounts[invnames.index(sellchoice)]
                    invcounts.pop(invcounts[invnames.index(sellchoice)])
                    invnames.pop(invnames.index(sellchoice))
                else:
                    print("Sorry, you don't seem to have that item!")

    if option == 6:
        print("You went to bed!")
        print("Taxes were 75 dollars!")
        days += 1
        plotindex = 0
        money -= 75
        for num in plotstatus:
            if num != 0 and num != 3:
                plotstatus[plotindex] += 1
            plotindex += 1
        sleepoption = input("Would you like to save and exit (y/n)? ")
        if sleepoption == "y":
            print("You fall into a deep dream! See you when you wake up!")
            config["farmname"] = farmname
            config["fieldsize"] = fieldsize
            config["plotplant"] = plotplant
            config["plotstatus"] = plotstatus
            config["invnames"] = invnames
            config["invcounts"] = invcounts
            config["days"] = days
            config["money"] = money
            with open(filepath, "w") as f:
                json.dump(config, f, indent=4)
            time.sleep(2)
            sys.exit()
        if sleepoption == "n":
            sleepoption = ""

