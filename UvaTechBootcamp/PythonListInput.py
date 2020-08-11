# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:26:20 2020

@author: Diana McSpadden
"""

# a function to ask the user for a word
def getListItemFromUser():
    enteredListItem = input("Enter an item for the list. When we are done type 'END!'")
    return enteredListItem


# initialize my list array
myList= []

endFlag = False
while not endFlag:
    listEntry = getListItemFromUser()
    if (listEntry == "'END'" or listEntry == "END"):
        endFlag = True
    else:
        # add the list entry to the list
        myList.append(listEntry)
        
# one way to print
print("The entered list is: \n",myList)

# another way to print
print("Another way to print the list:\n")
for item in myList:
    print(item, "\n")