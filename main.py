inventory = ["none", "none", "none"]
money = 20



def shop(x):
    doExit = False
    while doExit is False:
        print("Welcome to the shop, you have", x, "coins.")
        print("Your items: ", inventory)
        print("Shop items: Potions 5 coins, Food 3 coins, and Key 10 coins.")
        print("Press p for potions, f for food, and k for keys (You can also press q to quit)")
        choice = input()
        if choice == 'p':
            if x >= 5:
                print("You got a potion!")
                inventory[0] = "potion"
                x -= 5
            else:
                print("You don't have enough money for that!")
            print()
            print("-----------------------------------------------------------------------------")
        elif choice == 'f':
            if x >= 3:
                print("You got food!")
                inventory[1] = "food"
                x -= 3
            else:
                print("You don't have enough money for that!")
            print()
            print("-----------------------------------------------------------------------------")
        elif choice == 'k':
            if x >= 10:
                print("You got a key!")
                inventory[2] = "key"
                x -= 10
            else:
                print("You don't have enough money for that!")
            print()
            print("-----------------------------------------------------------------------------")
        elif choice == 'q':
            print("Goodbye!")
            print()
            print("-----------------------------------------------------------------------------")
            doExit = True 
        else:
            print("Thats not an option")
            print()
            print("-----------------------------------------------------------------------------")

room = 1
print("You are in room 1")

if room == 1:
    shop(money)
