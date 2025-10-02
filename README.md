# PyFarm
A lightweight text-based farming game written in Python.
Tend your farm by planting, harvesting, and selling crops. Keep yourself out of bankruptcy!

## Features
* View your field and track crop growth
* Plant and harvest crops
* Manage your inventory
* Buy seeds and sell crops at the shop
* Keep track of days and farm finances
* Save and load farm progress using JSON files

## Requirements
* Python (Written in Python 3.13.7)

## How to Install
1. Download this repository
2. Run the game with: python pyfarm.py
3. The download should contain a farmconfig.json file, but if it does not, you can create one by copying the format of the JSON in this repo

## How to Play
1. Select your farmconfig.json file when prompted
2. Choose to create a new farm or use an existing farm
3. Use the menu options to control the game:
  * View Field | Check the crops in your field
  * Plant Crops | Plant seeds from your inventory
  * Harvest Crops | Harvest fully grown crops
  * View Inventory | Check your seeds and harvested crops
  * View Shop | Buy seeds or sell crops
  * Sleep | End the day, pay utilities/taxes, and progress crops to next growth stage
  * When sleeping, you will be prompted to save and exit. Progress is ONLY saved if you say yes and exit the game.

## Roadmap
* Implement seasons
* Add weather effects that change crop growth time
* Add animals and their products
* Implement upgrades to the farm
* Add random events
* Add more crop types(?)
