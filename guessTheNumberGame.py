import random
import sys

frame_string = "---%--->_<---%---"
print(frame_string)

# face text art
print("|--------|")
print("|--O--O--|")
print("|--------|")
print("|---[]---|")
print("|--------|")

# opening problem, a simple one
def opening():
    # creepy terminator message
    print("Hello Human. Play a game with me.")
    num_to_guess = random.randint(lower_range, upper_range)
    print("I\'ve just thought of a number between %d and %d" % (lower_range, upper_range))
    # prompt the user
    print("guess my number: ")
    user_guess = input()
    # compare values
    if(int(user_guess) == int(num_to_guess)):
        print("That was correct! Thanks for playing with me.")
    # elif
    
    else:
        print("Oops. Wrong guess. Better luck next time, human.")

# has number of chances to guess, with hints
def correction():
    # message
    print("Okay. It's your first time playing. Maybe I'll give you some help")
    lives = 3
    print("We'll play by the same rules, but this time I'll give your %s chances" % str(lives))
    print("If I'm happy, I might even give you some hints")

    num_to_guess = random.randint(lower_range, upper_range)
    strikes = 0
    # three chanced
    while strikes < lives:
        print("Take a guess:")
        user_guess = input()
        if(int(user_guess) == int(num_to_guess)):
            print("Well done, human.")
            break;
        else:
            "Hmmm. Not quite."
            strikes += 1
            # giving corrections
            if(int(user_guess) > num_to_guess):
                print("that one was too large")
            else:
                # no need to check for equal
                print("that one was too small")
    if(strikes >= lives):
        print("You've lost. Try harder.")
    elif(strikes < lives):
        print("Good guess. That was correct! And you had %d chances left" % (lives-strikes))


upper_range = 11
lower_range = 1
opening()
correction()
print("Well, that was fun for me. See you next time, human.")
print(frame_string)
sys.exit(0)



