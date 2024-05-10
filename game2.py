from random import random
import os
import time
import sys
os.system("cls")


dungon = 1
room_num = 0

class Character:
    def __init__(self, name, health, maxhealth, strength, defence, invesntory=[]):
        self.health = health
        self.maxHealth = maxhealth
        self.strength = strength
        self.defence = defence
        self.inventory = invesntory
        self.name = name
    def __str__(self):
        return " (Health: " + str(self.health) +" (maxHealth: "  + str(self.maxHealth) + " Strength: " + str(self.strength) + " Defence: " + str(self.defence) + ")"

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
    time.sleep(1)
    print(" ..", end="\r")
    time.sleep(1)
    print(" ...", end="\r")



room = new_room()



charname = input("What is your name?: ")

wait()

time.sleep(1)
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
    print("You deal "+ str(max((player.strength - room.monster.defence),0)) +"damage")
    
    room.monster.health -= max((player.strength - room.monster.defence),0)
    print("The monster now has " + str(room.monster.health) + " health.")
    print("You now have " + str(player.health) + " health.")
    player.health -= max((room.monster.strength - player.defence),0)

    if player.health <= 0:
        print("You have died.")
        exit()

if action == "2":
    retreatChance = 1
    print("You have a" + retreatChance + "% to excape")
    print("You deal ____")
    
    room.monster.health -= max((player.strength - room.monster.defence),0)
    print("The monster now has " + str(room.monster.health) + " health.")
    print("You now have " + str(player.health) + " health.")
    player.health -= max((room.monster.strength - player.defence),0)

    if player.health <= 0:
        print("You have died.")
        exit()

