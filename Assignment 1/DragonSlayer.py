""" Program: DragonSlayer.py
    Author: Will Galbraith
    Last Modified by: Will Galbraith
    Version: 1.0
    Date Last Modified: May 9th 2013
    Description: Dragon Slayer is a text adventure game where the player 
    chooses between two options progressing the story line in hopes to kill the
    dragon of Moldoon before he himself meets a simular fate.
    This version is just a straight walk through of the choices.
    """

#import libraries needed
import time

"""Function:chooseDir
   Purpose:Determines which path the player takes
   Output:Returns an int representing user's choice 
   """
def chooseDir():
    #clears the choice of user in  case previous choice was made
    choice = ''
    while choice != '1' and choice != '2':
        print ("Choose knight:")
        #gets the choice from the user
        choice = raw_input()
    #returns the users choice
    return choice
    

""" Function:introduction
    Purpose:Gives the player his introduction to the story
    """
def introduction():
    print("You are a knight of valor.")
    print("Your king has set you on a quest to slay the dragon")
    print("of Moldoon who keeps ravaging the kingdom.")
    print("You begin your adventure sword and shield in hand.")
    print("Behold your first decision in your quest.")
    print("You approach a split in the road one leads to the firey mountains")
    print("the other the dark forest.")
    time.sleep(2)
    print("Where will you go...")
    print("1. The Firey Mountains")
    print("2. The Dark Forest")
    print

"""Function:darkForest
   Purpose:Gives the player the dark forest story and choices
   """
def darkForest():
    print("Entering the forest you can barely see a thing.")
    print("To your left you hear running water and ")
    print("to your right you see a dim light.")
    print("Standing still you contemplate where to go.")
    time.sleep(2)
    print("Where will you go...")
    print("1. The sound of water")
    print("2. The dim light")
    print

"""Function:theRiver
   Purpose: Continues the story towards the river 
   """
def theRiver():
    print("Following the sound of the water you come to a river.")
    print("There doesn't appear to be a bridge ")
    print("but looks as though there is a clearing down the river.")
    print("Will you risk crossing the river or follow it.")
    time.sleep(2)
    print("Where will you go...")
    print("1. Try crossing the river")
    print("2. Follow the river towards the clearing")
    print
    
"""Function:theCabin
   Purpose: Continues the story towards the cabin
   """
def theCabin():
    print("Following the light you come to a cabin in the woods.")
    print("The light is comming from inside and you hear other people")
    print("Should you go in?")
    time.sleep(2)
    print("Where will you go...")
    print("1. Enter the cabin")
    print("2. Try to go around the cabin")
    print
    
"""Function:fireyMountain
   Purpose:Gives the player the firey mountain story and choices
   """
def fireyMountain():
    print("As you approach the base of the mountain")
    print("you see the mouth of a cave and a path leading")
    print("further up the mountain.")
    print("Where could the dragon be?")
    time.sleep(2)
    print("Where will you go...")
    print("1. Enter the cave")
    print("2. Follow the path up the mountain")
    print
    
"""Function:theCave
   Purpose:Follows the story into the cave
   """
def theCave():
    print("You enter the cave and spot the dragon.")
    print("You notice he is asleep.")
    print("You see two opportunities")
    print("One to attack head on the other to sneak around from behind")
    time.sleep(2)
    print("What will you do...")
    print("1. Attack head on")
    print("2. Try the sneak attack")
    print
    
"""Function:thePath
   Purpose:Follows the story up the mountain path
   """
def thePath():
    print("You start your climb up the path.")
    print("After a long endevor you still see no sign of the dragon.")
    print("You realize you have climbed to a dangerous height.")
    print("Wondering if the dragon is still up the mountain")
    print("you think about carrying on.")
    time.sleep(2)
    print("Where will you go...")
    print("1. Climb back down")
    print("2. Continue on forward")
    print
    
"""Function:Main
   Purpose:The main function tying the story together
   """
def main():
    #variable to continue playing
    play = True
    
    #While play is equal to true play the game
    while play:
        introduction()
        #user decides to go to the mountain or the forest
        choice = chooseDir()
        #go to mountain
        if choice == "1":
            print("You begin your journey to the Firey Mountain.")
            fireyMoutain()
            #deciding between the cave or the path
            choice = chooseDir()
            #go to cave
            if choice == "1":
                print("You begin towards the cave.")
                theCave()
                #attack head on or sneak attack
                choice = chooseDir()
                #if head on
                if choice == "1":
                    print("The dragon awakes and you begin a fierce battle.")
                    print("After an attempt to eat you the dragons neck")
                    print("Is exposed and you decapitate him.")
                    print("Congradulations on saving the land.")
                elif choice == "2":
                    print("The dragon wasn't actually sleeping.")
                    print("As you try to sneak around him he takes")
                    print("One big gulp and eats you.")
                else
                    print ("Please make a valid choice")
############ NEED TO FINISH FIRST VERSION LATER ##################################
                    