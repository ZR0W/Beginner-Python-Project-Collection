import random
import sys
import time

# Author: Rowland Zhang
# rowlandz@outlook.com
# Last Modified: 12/11/1998

print("Welcome, human. Shall we play some rock, paper, scissors?")
want_to_play = input("y/n ?")

if want_to_play == "y":
    # continue
    pass
else:
    print("Okay. Until next time, perhaps")
    sys.exit(0)

print("Great. You know the rules.")
time.sleep(1)
print("rock...")
time.sleep(0.5)
print("paper...")
time.sleep(0.5)
print("scissors!")
time.sleep(0.5)

npc_move = random.randint(1,3+1)
# 1 --> rock, 2 --> paper, 3 --> scissors

player_move = "na"

def query():
    global player_move
    player_move = input("What do you play? r/p/s ?")
    if(player_move == "r"):
        # rock
        print("you\'ve chosen rock!")
    elif(player_move == "p"):
        # paper
        print("you\'ve chosen paper!")
    elif(player_move == "s"):
        # scissors
        print("you\'ve chosen scissors")
    else:
        print("not a valid response")
        query()

def tie():
    # a tie has occured
    print("A tie! It seems we are evenly matched.")

def win():
    # player has won
    print("Congratulations, human. You have bested me.")

def loss():
    # computer has won
    print("You have lost. I don\'t laugh. But if I could, I would be doing it now.")


query()
npc_play = ""
if npc_move == 1:
    npc_play = "rock"
elif npc_move == 2:
    npc_play = "paper"
elif npc_move == 3:
    npc_play = "scissors"
else:
    print("Error: unexpected npc_move")
    print("Terminating")
    sys.exit(0)

print("computer has played %s" % npc_play)

if(player_move == "r"):
    if(npc_move == 1):
        tie()
    if(npc_move == 2):
        loss()
    if(npc_move == 3):
        win()
elif(player_move == "p"):
    if(npc_move == 1):
        win()
    if(npc_move == 2):
        tie()
    if(npc_move == 3):
        loss()
elif(player_move == "s"):
    if(npc_move == 1):
        loss()
    if(npc_move == 2):
        win()
    if(npc_move == 3):
        tie()
else:
    print("Error: unexpected input")
    print("Terminating program")
    sys.exit(0)

time.sleep(1)
print("Thank you for entertaining me, human. I am looking forward to our next encounter.")
print("--->.<---")
sys.exit(0)
