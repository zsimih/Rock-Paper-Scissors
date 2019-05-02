import random
print("This is a Rock-Paper-Scissors game to be played against the computer!")
print("Good luck!")
print("\n")
gameObjects = ("Rock", "Paper", "Scissors")
otherGame = "yes"
computersScore = 0
playersScore = 0

while otherGame != "no":
    choiceCorrect = False
    while choiceCorrect is False:
        playersChoice = input(str("Rock, Paper or Scissors you choose?   "))
        if playersChoice == "Rock":
            choiceCorrect = True
        if playersChoice == "Paper":
            choiceCorrect = True
        if playersChoice == "Scissors":
            choiceCorrect = True
        if choiceCorrect is False:
            print("Choice couldn't be recognised, please try again.")
            print("\n")
    computersChoice = random.choice(gameObjects)
    if (computersChoice == playersChoice):
        print("Both of you chose ", playersChoice, ", try again!")
    if (computersChoice == "Rock") & (playersChoice == "Paper"):
        print("You won! Paper wraps around the Rock!")
        playersScore += 1
    if (computersChoice == "Rock") & (playersChoice == "Scissors"):
        print("Computer won! Scissors don't cut the Rock!")
        computersScore += 1
    if (computersChoice == "Paper") & (playersChoice == "Rock"):
        print("Computer won! Paper wraps around the Rock!")
        computersScore += 1
    if (computersChoice == "Paper") & (playersChoice == "Scissors"):
        print("You won! Scissors cut through Paper!")
        playersScore += 1
    if (computersChoice == "Scissors") & (playersChoice == "Rock"):
        print("You won! Rock brakes the Scissors blade!")
        playersScore += 1
    if (computersChoice == "Scissors") & (playersChoice == "Paper"):
        print("Computer won! Scissors cut through Paper!")
        computersScore += 1
    print("Your score: ", playersScore)
    print("Computer's score: ", computersScore)
    otherGame = input(str("Do you want to play more? Type anything if yes, otherwise type no   "))
    if otherGame == "no":
        if playersScore > computersScore:
            print("Congratulation, you have beaten the computer!")
        if playersScore < computersScore:
            print("You have been defeated!")
        if playersScore == computersScore:
            print("Your score equals the computer's score, you shouldn't settle with a draw.")
            otherGame = input(str("Do you want to play more? Type anything if yes, otherwise type no   "))
    print("\n")





