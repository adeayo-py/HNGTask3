"""
A simple guess game.
"""

from random import randint


def stageselection():
    #Dictionary to map out each stage properties
    stages = {
        'stage1': {'trials': 6, 'stage': 1, 'guessrange': '1 - 10','correctguess':randint(1,10)},
        'stage2': {'trials': 4, 'stage': 2, 'guessrange': '1 - 20', 'correctguess':randint(1,20)},
        'stage3': {'trials': 3, 'stage': 3, 'guessrange': '1 - 50', 'correctguess':randint(1,50)}
    }
    
    #catch error for any input aside integer
    try:
        selectstage = int(
        input("Welcome to our guess game. \nKindly select difficulty; 1 for easy, 2 for medium and 3 for hard: "))
    except:
        print("Type a number!")
        gameengine()

    #conditionals
    if selectstage == 1:
        return stages['stage1']
    elif selectstage==2:
        return stages['stage2']
    elif selectstage == 3:
        return stages['stage3']
    else:
        print("Select 1 for easy, 2 for medium and 3 for hard")
        gameengine()

def gameengine():
    #calling the stageselection function
    selection = stageselection()

    #iterator
    stageguesscount=0

    print("Welcome to stage", selection['stage'])
    print(f"You have {selection['trials']} trial(s) for this stage")

    #loop for guess based on stage difficulty
    while stageguesscount < selection['trials']:

        # catch error for any input aside integer. Continue iterating till you type an integer
        while True:
            try:
                stageguess = int(input(f"Make a guess between {selection['guessrange']} : "))
                break
            except:
                print("Type a number!")


        stageguesscount+=1
        if stageguess == selection['correctguess']:
            print("You got it right!")
            quit()

        else:
            print("That was wrong")
            if selection['trials'] - stageguesscount > 0:
                print("You have",selection['trials'] - stageguesscount,"trial(s) left")
            else:
                print("Game over!")

gameengine()
