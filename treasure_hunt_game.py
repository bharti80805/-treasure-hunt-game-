# Treasure Hunt Adventure Game

print("===================================")
print("     TREASURE HUNT ADVENTURE")
print("===================================")

print("Welcome Explorer!")

name = input("Enter your name: ").title()

print("Hello", name + "!")
print()

print("Your mission is to find the hidden treasure.")
print("Be careful! Every choice matters.")
print()

health = 100
coins = 0
inventory = []

print("============ MENU ============")
print("1. Start Game")
print("2. Game Rules")
print("3. Exit")
print()

print("===================================")
print("Choose wisely...")
print("One wrong decision can end your adventure.")
print("===================================")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Loading Game...")
    print()

    print("You reached the entrance of the Ancient Temple.")
    print("There are two doors in front of you.")
    print()

    print("Dark Door")
    print("Bright Door")
    print()

    door_choice = input("Which door will you choose?: ").lower()

    if door_choice == "dark door":
        print("You opened the Dark Door.")
        print("The room is dark...")
        print("You found an old map!")

        inventory.append("Old Map")
        print("👜 Inventory:", inventory)

        coins += 20
        print("🪙 Coins:", coins)

        print("The map shows a secret passage ahead...")
        print("Mission Continues...")
        print()

        print("The secret passage leads to a dark cave...")
        print("👹 A Wild Monster Appears!")
        print()

        print("What will you do?")
        print("1. Fight")
        print("2. Run")
        print("3. Hide")

        monster_choice = input("Enter your choice: ").lower() 
        if monster_choice == "fight":
            print("You decided to fight!")
            print("The monster attacked you!")

            health -= 30
            print("❤️ Health:", health)

            print("After a long battle...")
            print("You defeated the monster!")
            print()

            print("You found:")
            print("1. Golden Key")
            print("2. Magic Crystal")
            print()

            print("Both items added to your Inventory.")
            inventory.append("Golden Key")
            inventory.append("Magic Crystal")

            print("👜 Inventory:", inventory)
            print()

            print("You finally reached the Treasure Room.")
            print("A huge golden door is standing in front of you.")
            print("The door is locked...")

            if "Golden Key" in inventory:
                print("You used the Golden Key.")
                print("The door opened...")
                print("🏆 YOU WIN!")
                print()

                print("======== SECRET SHOP ========")
                print("Welcome Explorer!")
                print("🪙 Coins:", coins)
                print()

                print("1. ❤️ Health Potion - 30 Coins")
                print("2. ⚔️ Sword - 50 Coins")
                print("3. 🛡️ Shield - 40 Coins")
                print("4. 🚪 Exit Shop")

                shop_choice = int(input("Enter your choice: "))

                if shop_choice == 1:
                    print("❤️ You selected Health Potion.")

                    if coins >= 30:
                        coins -= 30
                        health += 50

                        if health > 100:
                            health = 100
                            print("🎉 Purchase Successful!")
                            print("❤️ Health:", health)
                            print("🪙 Coins:", coins)                           
                        else:
                            print("❌ Not enough Coins!")
                            
                elif shop_choice == 2:                       
                       print("⚔️ You selected Sword.")                       
                       if coins >= 50:
                            coins -= 50
                            inventory.append("Sword")                         
                            print("🎉 Purchase Successful!")
                            print("🪙 Coins:", coins)
                            print("👜 Inventory:", inventory)
                       else:
                            print("❌ Not enough Coins!")
                            
                elif shop_choice == 3:                                     
                         print("🛡️ You selected Shield.")
                         if coins >= 40:
                             coins -= 40
                             inventory.append("Shield")
                             print("🎉 Purchase Successful!")                        
                             print("🪙 Coins:", coins)
                             print("👜 Inventory:", inventory)
                         else:
                             print("❌ Not enough Coins!")
                             
                elif shop_choice == 4:                     
                         print("👋 Thanks for visiting the Secret Shop!")
                else:
                        print("❌ Invalid Choice!")

                print()
                print("====================================")
                print("      CONGRATULATIONS!")
                print("====================================")
                print("🏆 You found the Hidden Treasure!")
                print()
                print("👤 Player :", name)
                print("❤️ Final Health :", health)
                print("🪙 Final Coins :", coins)
                print("👜 Inventory :", inventory)
                print()
                print("🎉 Thanks for Playing!")
                print("See you in the next Adventure...")
                print("====================================")

            else:
                print("The door is locked.")
                print("You don't have the Golden Key.")
                print("GAME OVER")

        elif monster_choice == "run":
            print("You run away safely.")
            print("But you lost the chance to find the treasure.")
            print("GAME OVER")

        elif monster_choice == "hide":
            print("You hid behind a big rock.")
            print("The monster couldn't see you.")
            print("You escaped safely.")
            print("Mission Continues...")

        else:
            print("❌ Invalid Choice!")
            print("The monster attacked while you were confused!")
            print("GAME OVER")


    elif door_choice == "bright door":
        print("You opened the Bright Door.")
        print("A hidden trap was waiting!")
        print("You fell into the trap.")

        health -= 60

        print("❤️ Health:", health)
        print("GAME OVER")
        print("Better luck next time, Explorer!")

    else:
        print("Invalid Door!")

elif choice == 2:
    print("================ GAME RULES ================")
    print("1. Explore the temple carefully.")
    print("2. Every decision changes your journey.")
    print("3. Some doors are safe, some are deadly.")
    print("4. Collect useful items like Maps, Keys and Weapons.")
    print("5. Without the Key, the treasure room cannot be opened.")
    print("6. If your Health becomes 0, the game is over.")
    print("7. Find the treasure and escape safely to win.")
    print("============================================")

elif choice == 3:
    print("Thanks for playing!")

else:
    print("Invalid Choice!")