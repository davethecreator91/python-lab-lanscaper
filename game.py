# print("Welcome to the lawn mowing game!")



def gameStart():
    # print("Welcome to the lawn mowing game!")
    # print("What would you like to do?")
    # print("1. Use teeth to cut grass")
    # print("2. Buy scissors")
    # print("3. Use scissors to cut grass")
    # print("user can use teeth to cut grass")

    # print("user can buy scissors")

    # print("user can use scissors to cut grass")

    # print("user can buy push lawnmower")

    # print("user can use push lawnmower to cut grass")


    # print("You built a sucessful empire, You Win!")

    print("Welcome to the lawn mowing game!")
    gameSession = True
    while gameSession == True:
        wallet = 0
        

        print("user can use teeth to cut grass")


        # print(choice1)
        choice1 = input("Would you like to cut grass with your teeth? (y/n):")
        if choice1 == "y":
            print(f"You cut the grass with your teeth. You have ${wallet}.")
            wallet += 1

        else:
            print("You did not cut the grass with your teeth.")
            print(choice1)
        
        if wallet >= 1:
            print("user can buy scissors")

        # print(choice2)
        choice2 = input("Would you like to buy scissors? (y/n)")
        if choice2 == "y":
            wallet -= 1
            print(f"You bought scissors. You have ${wallet} left.")
        else:
            print("You did not buy scissors.")
            print(choice1)

       
        # print(choice3)
        choice3 = input("Would you like to use scissors to cut grass? (y/n)")
        if choice3 == "y":
            wallet += 5
            print(f"You cut the grass with scissors. You have ${wallet}.")
        else:
            print("You did not use scissors to cut grass.")
            print(choice3)

        if wallet >= 5:
            print('user can buy lawnmower')

        # print(choice4)
        choice4 = input('Would you like to buy a lawnmower? (y/n)?:')
        if choice4 == 'y':
            wallet -= 5
            print(f"You bought a lawn mower. You have ${wallet} left.")
            print("Congratulations your lawnmowing empire is off to a successful start, YOU WIN!")
            gameSession = False
                    

gameStart()