import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3

print(RPS(2)) #Papper
print(RPS.ROCK) #RPS.ROCK
print(RPS['ROCK']) #RPS.ROCK
print(RPS.ROCK.value) #1

print('')

playerchoice = input("Enter... \n1 for Rock, \n2 for Papper, \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print('')
print('player choice ' + str(RPS(player)).replace('RPS.', ''))
print('Python choice ' + str(RPS(computer)).replace('RPS.', ''))
print('')

if player == 1 and computer == 3:
    print("You win!")
elif player == 3 and computer == 2:
    print('You win!')
elif player == 2 and computer == 1:
    print("You win!")
elif player == computer:
    print("It's a tie")
else:
    print("Python wins!")

print('')
