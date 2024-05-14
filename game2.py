from random import random
# from colorama import Fore, Style
import os
import time

os.system("cls")

dungon = 1
room_num = 0

class Character:
    def __init__(self, name, health, maxhealth, strength, defence, inventory=[]):
        self.health = health
        self.maxHealth = maxhealth
        self.strength = strength
        self.defence = defence
        self.inventory = inventory
        self.name = name
    def __str__(self):
        return self.name + " (Health: " + str(self.health) +" maxHealth: "  + str(self.maxHealth) + " Strength: " + str(self.strength) + " Defence: " + str(self.defence) + ")"

class Room:
    def __init__(self, description, monster=None, item=None):
        self.description = description
        self.monster = monster
        self.item = item
    def __str__(self):
        return f"{self.description}\n  Monsters: {self.monster}\n  Loot: {self.item}"


class Item:
    def __init__(self, name,helath_impact=0, strength_impact=0, defence_impact=0):
        self.name = name
        self.health_impact = helath_impact
        self.strength_impact = strength_impact
        self.defence_impact = defence_impact
    def __str__(self):
        return f'''{self.name} (Health impact: {self.health_impact} Strength impact: {self.strength_impact} Defence impact: {self.defence_impact})'''

def new_room():
    health = health=int(10*random())
    monster1 = Character("Goblin", health=health, strength=int(10*random()), defence=int(10*random()), maxhealth=health)    
    item1 = Item("Sword", strength_impact=5)
    return Room(monster=monster1, item=item1,description="a cave")

def wait():
    print("")
    print(" .", end="\r")
    time.sleep(0.5)
    print(" ..", end="\r")
    time.sleep(0.5)
    print(" ...", end="\r")

def movement():
    print("1. Advance rooms")
    print("2. Inventory")
    print("3. Leave dungon")

    action = input()


# def leave_dungon():
#     leave_dungon_y_n = input("Are you sure you want to leave dungon, all progress will be lost, Y or N")
#     if leave_dungon_y_n == "y" or "Y":
#         print("")
#         #Go back to home base
#     if leave_dungon_y_n == "n" or "N":
#   --->  else leave_dungon()    <---


# #*************************************************************************
# #Is there a way to get this funtion to restart without using a loop
# #*************************************************************************



















# movement()

charname = input("What is your name?: ")

# Let's make 10 rooms
rooms = []
for i in range(10):
    rooms.append(new_room())

# we start in room 0
current_room = 0

while(True):
    print("You are in room " + str(current_room))
    print(rooms[current_room])
    print("What do you do?")
    print("1. Advance to next room")
    print("2. Go back to previous room")
    print("3. Inventory")
    action = input()
    if action == "1":
        if current_room < len(rooms):
            current_room += 1
    elif action == "2":
        if current_room > 0:
            current_room -= 1
    elif action == "3":
        print("You have no items")
    else:
        print("Invalid input")







# if charname == "1":
#     print("wait bypassed")
# else:   
#     wait()

# time.sleep(1)
os.system("cls")

player = Character(name=charname, health=100, strength=10, defence=5,maxhealth=100)


print("Your stats are: ")
print("")
print("HP "+ str(player.health)+"/"+str(player.maxHealth) )
print("Strength "+str(player.strength))
print("Defence "+str(player.defence))
print("")
print("Current room : ")
print(room)
print("")



print("What do you do?")
print("1. Attack")
print("2. Retreat")
print("3. Run to next room")
action = input()
if action == "1":

    print("You attack the monster!")

    print("You deal "+ str(max((player.strength - room.monster.defence),0)) +" damage")

    room.monster.health -= max((room.monster.health - (player.strength - room.monster.defence)),0)
    print("The monster now has " + str(room.monster.health) + " health.")
    
    print("You now have " + str(player.health) + " health.")
    player.health -= max((room.monster.strength - player.defence),0)

    if player.health <= 0:
        print("You have died.")
        exit()
