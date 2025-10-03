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
cropprices = {"Wheat":100, "Corn":120, "Soybean":40, "Tomato":65, "Potato":90}
days = 0
seasonday = 1
years = 1
money = 1000
seasons = ["Spring", "Summer", "Fall", "Winter"]
seasonindex = 0
seasonlen = 15
seasongrowthmods = {
    "Wheat": {"Spring":2, "Summer":1, "Fall":1, "Winter":1},
    "Corn": {"Spring":1, "Summer":2, "Fall":1, "Winter":1},
    "Soybean":{"Spring":1, "Summer":1, "Fall":2, "Winter":1},
    "Tomato":{"Spring":1, "Summer":2, "Fall":1, "Winter":1},
    "Potato":{"Spring":2, "Summer":1, "Fall":1, "Winter":1}
}
cropgrowtimes = {"Wheat":11, "Corn":9, "Soybean":3, "Tomato":5, "Potato":7}
bankrupt = False
totalmoney = 0
cropsharvested = 0

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
        "invnames": ["Tomato Seed", "Potato Seed"],
        "invcounts": [3, 2],
        "days": 0,
        "money": 700,
        "years": 1,
        "seasonday": 1,
        "seasonindex": 0,
        "bankrupt": False,
        "totalmoney": 0,
        "cropsharvested": 0
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
    years = config["years"]
    seasonday = config["seasonday"]
    seasonindex = config["seasonindex"]
    bankrupt = config["bankrupt"]
    totalmoney = config["totalmoney"]
    cropsharvested = config["cropsharvested"]

if menuoption == 3:
    print(f"Welcome to {farmname}!")
    print("Your parents left you with a bit of cash and some seeds to get started!")
    print("You will have 7 options to choose from.")
    time.sleep(1)
    print("View Field | This option will allow you to check on your crops and their stages of growth!")
    print("Plant Crops | This option will allow you to plant crops on empty plots!")
    print("Harvest Crops | This option will allow you to harvest any crop that has fully grown!")
    print("View Inventory | This option will allow you to see all the items in your inventory!")
    print("View Shop | This option will allow you to visit the shop to buy seeds and sell crops!")
    print("View Farmer's Manual | This option will allow you to read through some information on growing crops, weather, and other useful tidbits.")
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
    years = config["years"]
    seasonday = config["seasonday"]
    seasonindex = config["seasonindex"]
    bankrupt = config["bankrupt"]
    totalmoney = config["totalmoney"]
    cropsharvested = config["cropsharvested"]


while bankrupt != True:
    print("=================")
    print(f"You stand in the middle of {farmname}")
    print(f"It is Year {years}, {seasons[seasonindex]}, Day {seasonday}")
    print("1) View Field")
    print("2) Plant Crops")
    print("3) Harvest Crops")
    print("4) View Inventory")
    print("5) View Shop")
    print("6) View Farmer's Manual")
    print("7) Sleep")

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
        if plotplant[harvestchoice] != "" and plotstatus[harvestchoice] >= cropgrowtimes[plotplant[harvestchoice]]:
            if plotplant[harvestchoice] in invnames:
                harvestindex = invnames.index(plotplant[harvestchoice])
                invcounts[harvestindex] += 1
            else:
                invnames.append(plotplant[harvestchoice])
                invcounts.append(1)
            cropsharvested += 1
            plotplant[harvestchoice] = ""
            plotstatus[harvestchoice] = 0
        elif plotplant[harvestchoice] != "" and plotstatus[harvestchoice] < cropgrowtimes[plotplant[harvestchoice]]:
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
            print("Wheat Seed | 30")
            print("Corn Seed | 50")
            print("Soybean Seed | 25")
            print("Tomato Seed | 35")
            print("Potato Seed | 40")
            print("Options are CASE SENSITIVE!")
            buyoption = input("Choose your purchase: ")
            if buyoption == "Wheat Seed":
                if money - 30 > 0:
                    updateShopInv(buyoption)
                    money -= 30
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Corn Seed":
                if money - 50 > 0:
                    updateShopInv(buyoption)
                    money -= 50
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Soybean Seed":
                if money - 25 > 0:
                    updateShopInv(buyoption)
                    money -= 25
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Tomato Seed":
                if money - 35 > 0:
                    updateShopInv(buyoption)
                    money -= 35
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Potato Seed":
                if money - 40 > 0:
                    updateShopInv(buyoption)
                    money -= 40
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
                    totalmoney += cropprices[sellchoice] * invcounts[invnames.index(sellchoice)]
                    idx = invnames.index(sellchoice)
                    invcounts.pop(idx)
                    invnames.pop(idx)
                else:
                    print("Sorry, you don't seem to have that item!")
    
    if option == 6:
        print("You picked up your farmer's manual!")
        print("PAGE 1: CROP INFORMATION")
        print("\tWheat | Takes 11 days to grow, sells for 100 dollars. Grows faster in the spring.")
        print("\tCorn | Takes 9 days to grow, sells for 120 dollars. Grows faster in the summer.")
        print("\tSoybeans | Takes 3 days to grow, sells for 40 dollars. Grows faster in the fall.")
        print("\tTomatoes | Takes 5 days to grow, sells for 65 dollars. Grows faster in the summer.")
        print("\tPotatoes | Takes 7 days to grow, sells for 90 dollars. Grows faster in the spring.")
        print("")
        print("PAGE 2: SEED PRICES")
        print("\tWheat Seeds | 30 dollars")
        print("\tCorn Seeds | 50 dollars")
        print("\tSoybean Seeds | 25 dollars")
        print("\tTomato Seeds | 35 dollars")
        print("\tPotato Seeds | 40 dollars")
        print("")
        print("PAGE 3: FINANCES")
        print("\tEvery night you will pay a 75 dollar utilities and taxes bill.")
        print("\tIf a hailstorm hits your farm, you will have to pay a 30 dollar repair fee on top of your regular bill.")
        print("\tKeep your money above 0 or you will go bankrupt and lose your farm!")
        print("PAGE 4: INVENTORY AND SHOP")
        print("\tYour inventory is housed completely in one menu.")
        print("\tSeeds are plantable crops only. Harvested crops are stored as their respective name.")
        print("\tWhen entering the shop to buy something, inputs are case-sensitive.")
        print("\tWhen entering the shop to sell something, you may only sell harvested crops. Never seeds.")
        print("PAGE 5: WEATHER")
        print("\tSome nights, the weather will change and it will affect how your farm acts.")
        print("\t-Normal (Sunny) nights: Crops will grow at their usual rate.")
        print("\t-Rainy nights: Crops grow slightly faster")
        print("\t-Hailstorms: You will have to pay a 30 dollar repair fee on top of your utilities bill. Crops will grow normally.")
        print("\t-Snowstorms (Winter Only): Crops cannot grow at all that night.")
        print("")
        print("PAGE 6: TIPS & WARNINGS")
        print("\tDO NOT edit farmconfig.json manually. This can break the game.")
        print("\tTry to balance between short-term and long term crops.")
        print("\tRemember, you can only save when exiting the game through the sleep menu! The game will NOT autosave if you close any other way!")


    if option == 7:
        print("You went to bed!")
        days += 1
        seasonday += 1
        if seasonday > seasonlen:
            seasonday = 1
            seasonindex = (seasonindex + 1) % len(seasons)
            print(f"The season has changed! It is now {seasons[seasonindex]}")
            if seasonindex == 0:
                years += 1
                print(f"A new year has begun! It is now Year {years}.")
        weather = random.randint(1,3)
        plotindex = 0
        if seasons[seasonindex] == "Winter" and weather == 2 or seasons[seasonindex] != "Winter" and weather == 3:            
            money -= 105
            print("A hailstorm rolled through! You paid 75 dollars for utilities & taxes, as well as an additional 30 dollars for building repairs!")
        else:
            money -= 75
            print("You paid 75 dollars in utilities & taxes!")
        if money <= 0:
            bankrupt = True
        for num in plotstatus:
            crop = plotplant[plotindex]
            if plotplant[plotindex] != "":
                if num != 0 and num != cropgrowtimes[crop]:
                    if seasons[seasonindex] == "Winter" and weather != 3:
                        dogrow = random.randint(1, 2)
                        if dogrow == 1:
                            plotstatus[plotindex] += 1
                        else:
                            plotstatus[plotindex] += 0
                    elif seasons[seasonindex] == "Winter" and weather == 3:
                        print("There was a massive snowstorm. None of your plants were able to grow last night!")
                    else:
                        if weather == 2:
                            growrate = seasongrowthmods[crop][seasons[seasonindex]] + 1
                        else:
                            growrate = seasongrowthmods[crop][seasons[seasonindex]]
                        plotstatus[plotindex] += growrate
                        if plotstatus[plotindex] > cropgrowtimes[crop]:
                            plotstatus[plotindex] = cropgrowtimes[crop]
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
            config["years"] = years
            config["seasonday"] = seasonday
            config["seasonindex"] = seasonindex
            config["bankrupt"] = bankrupt
            config["totalmoney"] = totalmoney
            config["cropsharvested"] = cropsharvested
            with open(filepath, "w") as f:
                json.dump(config, f, indent=4)
            time.sleep(2)
            sys.exit()
        if sleepoption == "n":
            sleepoption = ""

if bankrupt == True:
    print("You ran out of money!")
    print("Your farm went into bankruptcy and was taken from you!")
    print(f"You ran your farm for {days} days and {years} years.")
    print(f"You managed to make {totalmoney} dollars and harvested {cropsharvested} crops.")
