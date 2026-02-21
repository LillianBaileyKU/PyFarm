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
plotstatus = [0, 0, 0, 0]
invnames = ["Wheat Seed", "Corn Seed", "Soybean Seed", "Tomato Seed", "Potato Seed"]
invcounts = [2, 4, 1, 3, 5]
crops = {"Wheat Seed":"Wheat", "Corn Seed":"Corn", "Soybean Seed":"Soybean", "Tomato Seed":"Tomato", "Potato Seed":"Potato", "Hay Seed":"Hay", "Cow":"Milk", "Chicken":"Egg", "Sheep":"Wool"}
cropprices = {"Wheat":120, "Corn":150, "Soybean":50, "Tomato":80, "Potato":100, "Milk":85, "Egg": 55, "Wool":105}
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
cropgrowtimes = {"Wheat":11, "Corn":9, "Soybean":3, "Tomato":5, "Potato":7, "Hay":5}
animaltimes = {"Cow":13, "Chicken":9, "Sheep":20}
bankrupt = False
totalmoney = 0
cropsharvested = 0
animalnum = []
animals = []
animalstatus = []
animalfed = []
plotupgrade = 1
animalupgrade = 0
fieldupgradeprice = 500
animalupgradeprice = 1000
hasanimals = False


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
        "money": 700,
        "years": 1,
        "seasonday": 1,
        "seasonindex": 0,
        "bankrupt": False,
        "totalmoney": 0,
        "cropsharvested": 0,
        "animals": [],
        "animalstatus": [],
        "plotupgrade": 1,
        "animalupgrade": 0,
        "fieldupgradeprice": 500,
        "animalupgradeprice": 1000,
        "hasanimals": False,
        "animalfed": []
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
    hasanimals = config["hasanimals"]
    animalfed = config["animalfed"]

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
    plotupgrade = config["plotupgrade"]
    animalupgrade = config["animalupgrade"]
    fieldupgradeprice = config["fieldupgradeprice"]
    animalupgradeprice = config["animalupgradeprice"]
    animals = config["animals"]
    animalstatus = config["animalstatus"]
    hasanimals = config["hasanimals"]
    animalfed = config["animalfed"]



while bankrupt != True:
    print("=================")
    print(f"You stand in the middle of {farmname}")
    print(f"It is Year {years}, {seasons[seasonindex]}, Day {seasonday}")
    if hasanimals == False:
        print("1) View Field")
        print("2) Plant Crops")
        print("3) Harvest Crops")
        print("4) View Inventory")
        print("5) View Shop")
        print("6) View Farmer's Manual")
        print("7) Sleep")
    else:
        print("1) View Field")
        print("2) Plant Crops")
        print("3) Harvest Crops")
        print("4) Tend Animals")
        print("5) View Inventory")
        print("6) View Shop")
        print("7) View Farmer's Manual")
        print("8) Sleep")

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

    if hasanimals == True and option == 4:
        animaloption = 0
        while animaloption != 3:
            print("You enter your barn")
            animalindex = 0
            for animal in animals:
                if animals[animalindex] == "":
                    print(f"Stall {animalindex + 1} has nothing living in it!")
                else:
                    print(f"Stall {animalindex + 1} has {animal} living in it! It is at production stage {animalstatus[animalindex]}!")
                    if animalfed[animalindex]:
                        print(f"The {animal} in stall {animalindex + 1} is fed!")
                    else:
                        print(f"The {animal} in stall {animalindex + 1} is unfed!")
                animalindex += 1
            print("1) Feed Animals")
            print("2) Harvest Animal Products")
            print("3) Exit Barn")
            animaloption = int(input("What would you like to do? "))

            if animaloption == 1:
                haycount = 0
                if "Hay" in invnames:
                    haycount += invcounts[invnames.index("Hay")]
                if haycount == 0:
                    print("You don't have any hay to feed with!")
                else:
                    feedoption = int(input("Choose the stall you wish to feed in: ")) - 1
                    if animalfed[feedoption] == True:
                        print("That animal is already fed!")
                    else:
                        animalfed[feedoption] = True
                        print(f"You fed the animal!")
                        haycount -= 1
                        invcounts[invnames.index("Hay")] -= 1
            if animaloption == 2:
                collectoption = int(input("Select the stall you would like to collect from: ")) -1
                if collectoption > (len(animals) - 1) or collectoption < 0:
                    print("You don't have that many stalls!")
                else:
                    animalinstall = animals[collectoption]
                    if animals[collectoption] == "":
                        print("That stall is empty!")
                    elif animalstatus[collectoption] >= animaltimes[animalinstall]:
                        if animalinstall == "Cow":
                            if "Milk" in invnames:
                                ind = invnames.index("Milk")
                                invcounts[ind] += 1
                            else:
                                invnames.append("Milk")
                                invcounts.append(1)
                        elif animalinstall == "Chicken":
                            if "Egg" in invnames:
                                ind = invnames.index("Egg")
                                invcounts[ind] += 1
                            else:
                                invnames.append("Egg")
                                invcounts.append(1)
                        elif animalinstall == "Sheep":
                            if "Wool"in invnames:
                                ind = invnames.index("Wool")
                                invcounts[ind] += 1
                            else:
                                invnames.append("Wool")
                                invcounts.append(1)
                        animalstatus[collectoption] = 0
                        print(f"You collected {crops[animalinstall]} from the {animalinstall}!")
                    else:
                        print("That animal isn't ready to collect from yet!")





    if (hasanimals == False and option == 4) or (hasanimals == True and option == 5):
        invindex = 0
        print("Item | Amount")
        for item in invnames:
            print(f"{item} | {invcounts[invindex]}")
            invindex += 1
        print(f"Your wallet has {money} dollars")

    if (hasanimals == False and option == 5) or (hasanimals == True and option == 6):
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
            print("Hay Seed | 40")
            if hasanimals == True:
                print("Cow | 150")
                print("Chicken | 100")
                print("Sheep | 250")
            if plotupgrade != 5:
                print(f"Field Upgrade | {fieldupgradeprice}")
            if animalupgrade == 0:
                print(f"Build Barn | {animalupgradeprice}")
            elif animalupgrade != 5 and animalupgrade != 0:
                print(f"Barn Upgrade | {animalupgradeprice}")
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
            elif buyoption == "Hay Seed":
                if money - 40 > 0:
                    updateShopInv(buyoption)
                    money -= 40
                else:
                    print("Sorry, you don't have enough money to purchase these!")
            elif buyoption == "Field Upgrade":
                if plotupgrade >= 6:
                    print("Your field is already at max level!")
                elif money - fieldupgradeprice > 0:
                    money -= fieldupgradeprice
                    plotupgrade += 1
                    for i in range(4):
                        plotnum.append(len(plotnum) + 1)
                        plotplant.append("")
                        plotstatus.append(0)

                    fieldupgradeprice = int(fieldupgradeprice * 1.5)
                    
                    print("Your field has been upgraded!")
                else:
                    print("Sorry, you don't have enough money to upgrade your field!")
            elif buyoption == "Build Barn" or buyoption == "Barn Upgrade":
                if buyoption == "Build Barn":
                    if animalupgrade != 0:
                        print("You already have a barn!")
                        continue
                else:
                    if animalupgrade == 0:
                        print("You don't have a barn yet!")
                    elif animalupgrade >= 5:
                        print("Your barn is already at max level!")
                
                if money - animalupgradeprice > 0:
                    money -= animalupgradeprice
                    hasanimals = True

                    for i in range(2):
                        animals.append("")
                        animalstatus.append(0)
                        animalfed.append(False)
                    
                    if animalupgrade == 0:
                        animalupgrade = 1
                        print("Your barn was built!")
                    else:
                        animalupgrade += 1
                        print("Your barn was upgraded!")

                    animalupgradeprice = int(animalupgradeprice * 1.8)
                
                else:
                    if buyoption == "Build Barn":
                        print("Sorry, you don't have enough money to build a barn!")
                    else:
                        print("Sorry, you don't have enough money to upgrade your barn!")
            elif buyoption in ["Cow", "Chicken", "Sheep"]:
                if "" in animals:
                    stall = animals.index("")
                else:
                    stall = None
                if stall == None:
                    print("No empty stalls!")
                else:
                    animals[stall] = buyoption
                    animalstatus[stall] = 0
                    animalfed[stall] = False
                    if buyoption == "Cow":
                        money -= 150
                    elif buyoption == "Chicken":
                        money -= 100
                    elif buyoption == "Sheep":
                        money -= 250
            else:
                print("Sorry, I couldn't find the item you're looking for!")
        elif marketoption == "sell" or marketoption == "Sell":
            cansell = False
            selllist = []
            sellindex = 0
            for thing in invnames:
                if thing == "Wheat" or thing == "Corn" or thing == "Soybean" or thing == "Tomato" or thing == "Potato" or thing == "Milk" or thing == "Egg" or thing == "Wool":
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
    
    if (hasanimals == False and option == 6) or (hasanimals == True and option == 7):
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
        print("\tEvery night you will pay a 35 dollar utilities and taxes bill.")
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
        print("\t-Hailstorms: You will have to pay a 15 dollar repair fee on top of your utilities bill. Crops will grow normally.")
        print("\t-Snowstorms (Winter Only): Crops cannot grow at all that night.")
        print("")
        print("PAGE 6: TIPS & WARNINGS")
        print("\tDO NOT edit farmconfig.json manually. This can break the game.")
        print("\tTry to balance between short-term and long term crops.")
        print("\tRemember, you can only save when exiting the game through the sleep menu! The game will NOT autosave if you close any other way!")


    if (hasanimals == False and option == 7) or (hasanimals == True and option == 8):
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
        weather = random.randint(1,6)
        plotindex = 0
        if seasons[seasonindex] == "Winter" and weather == 4 or seasons[seasonindex] != "Winter" and weather == 6:            
            money -= 50
            print("A hailstorm rolled through! You paid 35 dollars for utilities & taxes, as well as an additional 15 dollars for building repairs!")
        else:
            money -= 35
            print("You paid 35 dollars in utilities & taxes!")
        if money <= 0:
            bankrupt = True
        for num in plotstatus:
            crop = plotplant[plotindex]
            if plotplant[plotindex] != "":
                if num != 0 and num != cropgrowtimes[crop]:
                    if seasons[seasonindex] == "Winter" and weather != 5 and weather != 6:
                        dogrow = random.randint(1, 2)
                        if dogrow == 1:
                            plotstatus[plotindex] += 1
                        else:
                            plotstatus[plotindex] += 0
                    elif seasons[seasonindex] == "Winter" and weather == 5 or weather == 6:
                        print("There was a massive snowstorm. None of your plants were able to grow last night!")
                    else:
                        if weather == 4 or weather == 5:
                            growrate = seasongrowthmods[crop][seasons[seasonindex]] + 1
                        else:
                            growrate = seasongrowthmods[crop][seasons[seasonindex]]
                        plotstatus[plotindex] += growrate
                        if plotstatus[plotindex] > cropgrowtimes[crop]:
                            plotstatus[plotindex] = cropgrowtimes[crop]
            plotindex += 1
        if hasanimals:
            while len(animalstatus) < len(animals):
                animalstatus.append(0)
            while len(animalfed) < len(animals):
                animalfed.append(False)

            for i, animal in enumerate(animals):
                if animal == "":
                    continue
                if animal not in animaltimes:
                    continue
                if animalfed[i]:
                    animalstatus[i] += 1
                if animalstatus[i] >= animaltimes[animal]:
                    animalstatus[i] = animaltimes[animal]
                
                animalfed[i] = False

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
            config["animals"] = animals
            config["animalstatus"] = animalstatus
            config["plotupgrade"] = plotupgrade
            config["animalupgrade"] = animalupgrade
            config["fieldupgradeprice"] = fieldupgradeprice
            config["animalupgradeprice"] = animalupgradeprice
            config["hasanimals"] = hasanimals
            config["animalfed"] = animalfed
            with open(filepath, "w") as f:
                json.dump(config, f, indent=4)
            time.sleep(2)
            break
        if sleepoption == "n":
            sleepoption = ""

if bankrupt == True:
    print("You ran out of money!")
    print("Your farm went into bankruptcy and was taken from you!")
    print(f"You ran your farm for {days} days and {years} years.")
    print(f"You managed to make {totalmoney} dollars and harvested {cropsharvested} crops.")