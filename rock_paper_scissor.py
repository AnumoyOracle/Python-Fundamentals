from random import choice
moves = ["Rock", "Paper", "Scissor"]

def canWin(a, b):
    if (a == "Rock" and b == "Scissor") or (a == "Paper" and b == "Rock") or (a == "Scissor" and b == "Paper"):
        return True
    else:
        return False

while True:
    userScore = 0
    computerScore = 0
    userInput = int(input(''' 
      You want to continue the game ?
          Press 1 (Continue)
          Press 2 (Exit)
    '''))
    if userInput == 1:
        for turn in range(1,6):
            userChoice = int(input(''' 
                Select your move :
                Press 1 (Rock)
                Press 2 (Paper)
                Press 3 (Scissor)
            '''))
            userMove = moves[userChoice - 1]
            computerMove = choice(moves)
            if userMove == computerMove:
                print("This turn ends in a draw")
                print("Both the player choose ", userMove)
                userScore += 1
                computerScore += 1
            elif canWin(userMove, computerMove) == True:
                print("In this turn User wins")   
                print("User chose", userMove)
                print("Computer chose", computerMove)
                userScore += 2
            else:
                print("In this turn computer wins")
                print("User chose", userMove)
                print("Computer chose", computerMove)
                computerScore += 2

        if userScore == computerScore:
            print("Draw Game : ")
            print("Score of the user : ", userScore)
            print("Score of the computer : ", computerScore)
        elif userScore > computerScore:
            print("User won the game")
            print("Score of the user : ", userScore)
            print("Score of the computer : ", computerScore)
        else:
            print("Computer won the game")
            print("Score of the user : ", userScore)
            print("Score of the computer : ", computerScore)                
    else:
        break    