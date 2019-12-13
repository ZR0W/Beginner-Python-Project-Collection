# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:07:49 2019

@author: Rowland Zhang
"""

import random

# gloabal variable
targetWord = ""
stylelisticSeperator = "=============================="
unknown = "_"
chances = 5

# method definition

def main():
    print(stylelisticSeperator)
    print("Hello human. Welcom to a game of hangman.")
    global targetWord 
    targetWord = randomWord()
    print(stylelisticSeperator)
    queryUser()
    print(stylelisticSeperator)
    endGame()
    print(stylelisticSeperator)

def randomWord():
    file = open("words_Xethron.txt", "r")
    if file.mode == "r":
        print("using words from %s" % file.name)
        # contents = file.read()
        # print(contents)
        
        fileLines = file.readlines()
        
        lineCount = 0
        for line in fileLines:
            lineCount += 1
            line = line.strip()
            # print("%d - %s" % (lineCount, line))
        
        wordNum = random.randint(0, lineCount+1)
        randomWord = fileLines[wordNum].strip()
        print("DEBUG: num: %d, word: %s" % (wordNum, randomWord))
        return randomWord
    
    pass

def queryUser():
    prompt = "I expect you know the rules of the game.\nI will give you %d chances in total" % chances
    print(prompt)
    ask([], 0)
    pass

def ask(knowledge, strikes):
    if(strikes >= chances):
        print("Sorry human. It seems you have run out of chances to guess my word.\nBetter luck next time.")
        return
    print("You have %d chances left." % (chances-strikes))
    progress_so_far = currentKnowledge(knowledge)
    print(progress_so_far)
    if not(unknown in progress_so_far) :
        print("Congratulations. You've pieced together that the word is %s" % targetWord)
        return
    currentGuess = input("Make your guess: ")
    if(currentGuess == targetWord):
        print("That was correct! the answer is %s" % currentGuess)
        return
    if currentGuess in targetWord:
        print("the word does contain [%s]" % currentGuess)
        knowledge.extend(currentGuess)
        pass
    else:
        print("the word does not have [%s] in it" % currentGuess)
        strikes += 1
        pass
    ask(knowledge, strikes)
    
def currentKnowledge(knowledge):
    output = ""
    for a in targetWord:
        if (a in knowledge):
           output += a
           output += " "
        else:
           output += unknown
           output += " "
    return output.strip()
    pass

def endGame():
    prompt = "Thank you for playing hangman with me.\nI look forward to our next encouter."
    print(prompt)
    pass

# code execution
    
main()