import random
mirio = random.randint(0,2)
#mirio is the computer/AI
#rock is 1, paper is 2, scissors is 3
futaba = input("Rock, Paper or Scissors?")

#Rock
  rockTie():
    mirio == 0 and futaba == ("Rock")
    print("You tied, please try again!")
  
  rockWin():
    mirio == 0 and futaba ==("Scissors")
    print("You won, Congratulations!")
  
  rockLoss():
    mirio == 0 and futaba ==("Paper")
    print("You lost, get good!")

#Paper
paperTie():
  mirio == 1 and futaba ==("Paper")
  print("You tied, please try again!")

 paperWin():
    mirio == 1 and futaba ==("Rock")
    print("You won, Congratulations!")
  
  paperLoss():
    mirio == 1 and futaba ==("Scissors")
    print("You lost, get good!")

#Scissors
  scissorsTie():
    mirio == 2 and futaba ==("Scissors")
    print("You tied, please try again!")
  
  scissorsWin():
    mirio == 2 and futaba ==("paper")
   print("You won, Congratulations!")

  scissorsLoss():
    mirio == 2 and futaba ==("Rock")
    print("You lost, get good!")


