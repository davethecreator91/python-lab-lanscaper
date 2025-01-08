

# print("user can use teeth to cut grass")

# print("user can buy scissors")

# print("user can use scissors to cut grass")

# print("user can buy push lawnmower")

# print("user can use push lawnmower to cut grass")


# print("You built a sucessful empire, You Win!")

gameSession = True

def gameStart():
    # print("Welcome to the lawn mowing game!")
    # print("What would you like to do?")
    # print("1. Use teeth to cut grass")
    # print("2. Buy scissors")
    # print("3. Use scissors to cut grass")
    print
    
    while gameSession == True:
        wallet = 0
        print("Welcome to the lawn mowing game!")
        print("user can use teeth to cut grass")


        choice1 = input("Would you like to cut grass with your teeth? (y/n):")
        if choice1 == "y":
            wallet += 1
            print(f"You cut the grass with your teeth. You have ${wallet}.")
        else:
            print("You did not cut the grass with your teeth.")

        
        if wallet >= 1:
            print("user can buy scissors")
            choice2 = input("Would you like to buy scissors? (y/n)")
        if choice2 == "y":
            wallet -= 1
            print(f"You bought scissors. You have ${wallet} left.")
            choice3 = input("Would you like to use scissors to cut grass? (y/n)")
            if choice3 == "y":
                wallet += 5
                print(f"You cut the grass with scissors. You have ${wallet}.")
                if wallet > 5:
                    print('user can buy lawnmower')
                    choice4 = input('Would you like to buy lawnmower? (y/n)?:')
                    if choice4 == 'y':
                        print(f"You bought a lawn mower. You have ${wallet} left.")
                        print("Congratulations your lawnmowing empire is off to a successful start, YOU WIN!")
                        gameSession = False
            else:
                print("You did not use scissors to cut grass.")
        else:
            print("You did not buy scissors.")

        


gameStart()