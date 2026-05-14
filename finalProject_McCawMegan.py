# Megan McCaw
# May 11, 2026
# Final Project
# This program will be a text-based adventure game where the player is stranded on a deserted island and given choices that lead to survival, rescue, or demise.

import random
import time

# Create the player character with a dictionary to hold stats and boolean values for rescued status

def create_player():
    name = input("You wake up on a deserted island. As you come to, you try to remember how you got here. What is your name? ")
    player = {
        "name": name,
        "health": 85,
        "hunger": 50,
        "thirst": 50,
        "energy": 90,
        "morale": 50,
        "shelter_progress": 0,
        "rescued": False,
    }
    return player

def display_stats(player):
    print(f"\n{player['name']}'s Stats:")
    print(f"🏥 Health: {player['health']}")
    print(f"🍜 Hunger: {player['hunger']}")
    print(f"💧 Thirst: {player['thirst']}")
    print(f"⚡️ Energy: {player['energy']}")
    print(f"🔥 Morale: {player['morale']}")
    print(f"🛖 Shelter Progress: {player['shelter_progress']}%")

def search_food(player):
    print("\nYou explore the island in search of food...")
    time.sleep(2)
    
    roll = random.randint(1, 10)

    if roll <= 3:
        print("🫐 You found some berries! They are safe to eat.")
        player["hunger"] -= 15
        player["energy"] += 10
        player["morale"] += 5
    elif roll <= 6:
        print("🐟 You caught a fish! You feel much stronger.")
        player["hunger"] -= 25
        player["energy"] += 15
        player["morale"] += 10
    elif roll <= 9:
        print("😥 You couldn't find any food.")
        player["hunger"] += 5
        player["energy"] -= 5
        player["morale"] -= 5
    else:
        print("🤕 You got injured while searching for food!")
        player["health"] -= 20
        player["hunger"] += 10
        player["energy"] -= 20
        player["morale"] -= 15

def drink_water(player):
    print("\nYou're getting thirsty. You search for water...")
    time.sleep(2)

    roll = random.randint(1, 10)

    if roll <= 5:
        print("🥥 You found coconuts with water inside!")
        player["thirst"] -= 25
        player["energy"] += 10
        player["morale"] += 5
    else:
        print("😥 You couldn't find any water.")
        player["thirst"] += 10
        player["energy"] -= 5
        player["morale"] -= 5

def rest(player):
    print("\n😴 You take some time to rest and recover...")
    time.sleep(2)
    player["health"] += 10
    player["energy"] += 10
    player["morale"] += 5

def build_shelter(player):
    print("\nYou attempt to build a shelter using found materials...")
    time.sleep(2)

    roll = random.randint(1, 10)
    if roll <= 5:
        print("You made some progress on the shelter. 🛖")
        player["shelter_progress"] += 10
        player["morale"] += 10
        player["energy"] -= 15
    elif roll <= 8:
        print("😥 Your shelter fell apart while you were building it!")
        player["morale"] -= 10
        player["energy"] -= 10
    else:
        print("A log fell on your head!🤕")
        player["health"] -= 15
        player["energy"] -= 10
        player["morale"] -= 10

def signal_for_help(player):
    print("\n📢 You try to signal for help by creating a large SOS sign on the beach...")
    time.sleep(2)

    roll = random.randint(1, 10)
    if roll <= 2:
        print("🛩️ A plane flies overhead and sees your signal! You're rescued!")
        player["rescued"] = True
    else:
        print("😥 No one sees your signal.")
        player["morale"] -= 10


def main():
    player = create_player()

    print(f"\n🏝️ Welcome to the island, {player['name']}! You need to survive or find a way to civilization.")

    while player["health"] > 0:

        if player["shelter_progress"] >= 100:
            print("\nCongratulations! You've built a shelter and adapted to life on the island!")
            break

        if player["rescued"]:
            print("\nCongratulations! You've been rescued!")
            break

# Check for critical conditions - if hunger or thirst is too high, or energy/morale is too low, the player takes health damage
        if player["hunger"] >= 95:
            player["health"] -= 10
            print("You are starving!")
        if player["thirst"] >= 95:
            player["health"] -= 15
            print("You are severely dehydrated!")
        if player["energy"] <= 0:
            player["health"] -= 5
            print("You are completely exhausted!")
        if player["morale"] <= 0:
            player["health"] -= 10
            print("You have lost hope and are struggling to survive...")
        if player["health"] <= 0:
            player["health"] = 0
            print("\nYou didn't survive the island...")
            break

        time.sleep(1)

        display_stats(player)
        print("\nWhat would you like to do?")
        print("1. Search for food")
        print("2. Search for water")
        print("3. Rest")
        print("4. Attempt to build a shelter")
        print("5. Attempt to signal for help")
        print("6. Check stats")
        print("7. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            search_food(player)
        elif choice == "2":
            drink_water(player)
        elif choice == "3":
            rest(player)
        elif choice == "4":
            build_shelter(player)
        elif choice == "5":
            signal_for_help(player)
        elif choice == "6":
            display_stats(player)
        elif choice == "7":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

# Slightly increase hunger and thirst, decrease energy after each action
        player["hunger"] += 5
        player["thirst"] += 5
        player["energy"] -= 3

# Cap the stats to be between 0 and 100
        player["hunger"] = max(0, min(100, player["hunger"]))
        player["thirst"] = max(0, min(100, player["thirst"]))
        player["energy"] = max(0, min(100, player["energy"]))
        player["morale"] = max(0, min(100, player["morale"]))

main()