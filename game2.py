from random import random

class Character:
    def __init__(self, name, health, power, toughness,invesntory=[]):
        self.health = health
        self.power = power
        self.toughness = toughness
        self.inventory = invesntory
        self.name = name
    def __str__(self):
        return " (Health: " + str(self.health) + " Power: " + str(self.power) + " Toughness: " + str(self.toughness) + ")"

class Room:
    def __init__(self, description, monster=None, item=None):
        self.description = description
        self.monster = monster
        self.item = item
    def __str__(self):
        return f"{self.description}\n  Monsters: {self.monster}\n  Loot: {self.item}"


class Item:
    def __init__(self, name,helath_impact=0, power_impact=0, toughness_impact=0):
        self.name = name
        self.health_impact = helath_impact
        self.power_impact = power_impact
        self.toughness_impact = toughness_impact
    def __str__(self):
        return f'''{self.name} (Health impact: {self.health_impact} Power impact: {self.power_impact} Toughness impact: {self.toughness_impact})'''

def new_room():
    monster = Character("Goblin", health=int(10*random()), power=int(10*random()), toughness=int(10*random()))
    item = Item("Sword", power_impact=5)
    return Room("A Cave",monster=monster, item=item)

room = new_room()

player = Character("Player", health=100, power=10, toughness=5)


print("Your vital stats are: ")
print(player)
print("Your current location is: ")
print(room)

print("What do you do?")
print("1. Attack")
print("2. Retreat")
print("3. Run to next room")
action = input()
if action == "1":
    print("You attack the monster!")
    player.health -= max((room.monster.power - player.toughness),0)
    if player.health <= 0:
        print("You have died.")
        exit()
    room.monster.health -= max((player.power - room.monster.toughness),0)
    print("The monster now has " + str(room.monster.health) + " health.")
    print("You now have " + str(player.health) + " health.")


