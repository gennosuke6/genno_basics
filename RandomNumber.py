import random

def GameDraw():
    FirstNumber = int(input("Please, insert the first game number: "))
    LastNumber = int(input("Please, insert the last game number: "))
    Game = 1
    GametobePlayed = [random.randint(FirstNumber,LastNumber) for int in range(Game)]
    print(GametobePlayed)
    Exit = input("Do you want to try again? ").upper()
    while Exit=="YES":
        GameDraw()
        break
        
GameDraw()

