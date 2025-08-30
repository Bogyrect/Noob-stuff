import random

print("Welcome to my Blacksmith shop traveler!\n")
name = input("What's your name traveler?\n")
coins = 150  # Player's coin pouch
inventory = []  # Player's inventory
go_to_upgrade = False

# Lists
weapon = {
    "Short Sword": 85,
    "Rapier": 125,
    "Long Sword": 200,
    "Mace": 75,
    "Bow": 50,
    "Arrow x5": 10,
}

armor = {
    "Chainmail": 180,
    "Cuirass": 120,
    "Gauntlets": 155,
    "Gambeson": 90,
    "Greaves": 125,
    "Helmet": 100,
}

items = {
    "Chainmail": 180,
    "Cuirass": 120,
    "Gauntlets": 155,
    "Gambeson": 90,
    "Greaves": 125,
    "Short Sword": 85,
    "Rapier": 125,
    "Long Sword": 200,
    "Mace": 75,
    "Bow": 50,
    "Helmet": 100,
}
    # Main Menu
while True:
    print(f"\n{name}, you have {coins} Gold.")
    print("Your inventory:", inventory)
    print("="*30)
    print("   BLACKSMITH MAIN MENU")
    print("="*30)
    print("1. Shop")
    print("2. Upgrade an item")
    print("3. Sell Items")
    print("4. Exit")
    if go_to_upgrade:
        choice = "2"
        go_to_upgrade = False
    else:
        choice = input("Enter 1, 2, 3, or 4: ").strip()
# Shop
    if choice == "1":
        print("Great! Here are my finest armors.\n")
        discount_item = random.choice(list(items.keys()))
        discount_percent = random.choice([10, 20, 30])
        for item, price in items.items():
            if item == discount_item:
                discounted_price = int(price * (1 - discount_percent / 100))
                print(f"{item}: {discounted_price} Gold (SALE! {discount_percent}% off!)")
            else:
                print(f"{item}: {price} Gold")
        while True:
            buy_choice = input("What would you like to buy? (type 'exit' to leave)\n").strip().title()
            if buy_choice.lower() == 'exit':
                break
            if buy_choice in items:
                # Use discounted price if it's the discount item
                if buy_choice == discount_item:
                    price = int(items[buy_choice] * (1 - discount_percent / 100))
                else:
                    price = items[buy_choice]
                confirm = input(f"Confirm purchase of {buy_choice} for {price} Gold? (yes/no): ").strip().lower()
                if confirm != "yes":
                    print("Purchase cancelled.")
                    continue  # Go back to the shop menu
                if coins >= price:
                    coins -= price
                    print(f"Excellent choice! The {buy_choice} costs {price} Gold.")
                    print(f"You have {coins} Gold coins left.")
                    inventory.append(buy_choice)
                    # After purchase, offer next options:
                    print("\nWhat would you like to do next?")
                    print("1. Upgrade an item")
                    print("2. Return to main menu")
                    print("3. Exit")
                    next_action = input("Enter 1, 2, or 3: ").strip()
                    if next_action == "1":
                        go_to_upgrade = True
                        break  # Exit shop loop, main loop will check the flag
                    elif next_action == "2":
                        break  # Return to main menu
                    elif next_action == "3":
                        print("Goodbye, adventurer!")
                        exit()
                    else:
                        print("Returning to main menu.")
                        break
                else:
                    print(f"Sorry, you don't have enough coins for the {buy_choice}. You have {coins} Gold.\n")
            else:
                print(f"Sorry, I don't have that item at this time.")
# Upgrade
    elif choice == "2":
        while True:
            print("Your inventory:", inventory)  # Shows inventory before asking
            upgrade = input("Do you want to upgrade an item? Type the item name or 'no' to skip:\n").strip().title()
            if upgrade.lower() == 'no':
                break
            if upgrade in inventory:
                upgrade_cost = 50
                if coins >= upgrade_cost:
                    coins -= upgrade_cost
                    print(f"Your {upgrade} has been upgraded! You have {coins} Gold left.")
                else:
                    print(f"Sorry, you don't have enough coins to upgrade the {upgrade}. You have {coins} Gold.\n")
            else:
                print("You don't have that item in your inventory!\n")
            if upgrade in weapon:
               print("Upgrade options:")
               print("1. Increase damage +10")
               print("2. Increase durability +10")
               print("3. Critical hit chance +5%")
               print("4. Increase attack speed +5%")
               weapon_upgrade = {
                  "damage": weapon[weapon]["damage"] +10,
                  "durability": weapon[weapon]["durability"] +10,
                  "critical hit chance": weapon[weapon]["critical hit chance"] +5,
                  "attack speed": weapon[weapon]["attack speed"] +5,
               }
               weapon_upgrade = input("Choose an upgrade 1-4").strip()
            if weapon_upgrade in ["1", "2", "3", "4"]:
                print(f"Your {weapon} has been upgraded to {weapon_upgrade}\n")
# Selling Items
    elif choice == "3":
        if not inventory:
            print("You have nothing to sell!")
            continue
        print("Your inventory:", inventory)
        sell_choice = input("Which item would you like to sell? (type 'no' to cancel)\n").strip().title()
        if sell_choice.lower() == 'no':
            print("Sale Cancelled.")
            continue
        if sell_choice in inventory:
            sell_price = items.get(sell_choice, 0) // 2 # Sell for half price
            if sell_price > 0:
                coins += sell_price
                inventory.remove(sell_choice)
                print(f"You sold {sell_choice} for {sell_price} Gold. You now have {coins} Gold.")
            else:
                print(f"I can't buy that item from you.")
        else:
            print("You don't have that item in your inventory.")

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
    if go_to_upgrade:
        continue  # Skip the rest of the loop and go to upgrade section
    elif choice == "4":
        print("Goodbye, adventurer!")
        break