# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:26:20 2020

@author: Diana McSpadden
"""

# a function to ask the user for a word
def getAWordFromUser():
    enteredWord = input("Give me a word, any word ... ")
    return enteredWord

# a function to validate if the user entered a word
def validateWord(enteredWord):
    isWord = False
    # check if string
    if (type(enteredWord) == type("Diana")):
        # check if alpha and if longer than 1 character unless 'a/A' or 'I' - yes, this doesn't check 
        #   against a dictionary, and also doesn't capture contractions, but it gets the point across
        if (enteredWord.isalpha()):
            if (len(enteredWord) > 1 or enteredWord.upper() == "A" or enteredWord == "I"):
                isWord = True                
    if (isWord != True):
        print("That's not a word. Try again.")
        
    return isWord
    

# initialize that we don't have a word yet
userEnteredAWord = False

# while we don't have a word keep asking for one and validating
while not userEnteredAWord:
    testWord = getAWordFromUser()
    userEnteredAWord = validateWord(testWord)
    
# thank the user for the word
print("Thank you for your word: ", testWord)