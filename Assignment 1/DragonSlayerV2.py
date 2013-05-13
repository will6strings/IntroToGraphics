""" Program: DragonSlayer.py
    Author: Will Galbraith
    Last Modified by: Will Galbraith
    Version: 2.0
    Date Last Modified: May 13th 2013
    Description: Dragon Slayer is a text adventure game where the player 
    chooses between two options progressing the story line in hopes to kill the
    dragon of Moldoon before he himself meets a simular fate.
    This version introduces the concept of a battle with the dragon.
    When the player reaches the dragon there is a random chance that they will defeat him.
    """
    
''' 1.1 edit: Changed the multiple story functions (theCave, theRiver, thePath, theCabin)
    by just adding them directly into the two main stories darkForest & fieryMountain
    cleaning up the main function so it looks simpler.
    Also fixed a majr spelling error firey instead of the correct fiery'''
    
''' 2.0 edit: Imported the random library. Took out all the else statements for
    invalid input and added an if in the chooseDir function to tell the user to 
    use a vaild selection. When the player attacks the dragon and starts the battle
    a random number between 1 & 2 is assigned. If 1 the player slays the dragon if 
    2 the dragon slays the player.(see fieryMountain())'''

#import libraries needed
import time
import random

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
        #in case user chooses an invalid input
        if choice != '1' and choice != '2':
            print("Please enter 1 or 2")
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
    print("You approach a split in the road one leads to the fiery mountains")
    print("the other the dark forest.")
    time.sleep(2)
    print("Where will you go...")
    print("1. The Fiery Mountains")
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
    #go towards the water or the light
    choice = chooseDir()
    #if they choose the water
    if choice == "1":
        print("You begin to follow the sound")
        print("Following the sound of the water you come to a river.")
        print("There doesn't appear to be a bridge ")
        print("but looks as though there is a clearing down the river.")
        print("Will you risk crossing the river or follow it.")
        time.sleep(2)
        print("Where will you go...")
        print("1. Try crossing the river")
        print("2. Follow the river towards the clearing")
        print
        #try to cross or follow clearing
        choice = chooseDir()
        #if they try to cross
        if choice == "1":
            print("You attempt to make your way across the river.")
            print("Once you get halfway through you realize")
            print("the river is deeper then you hoped and your armor drags")
            print("you down.")
        #if they follow the river
        elif choice == "2":
            print("Following the path of the river you come to a clearing.")
            print("In the middle of the clearing you see a golden sword")
            print("placed into a stone.")
            print("Walking up to the sword you pull it from the stone.")
    #they choose the light
    elif choice == "2":
        print("You work your way towards the light.")
        print("Following the light you come to a cabin in the woods.")
        print("The light is comming from inside and you hear other people")
        print("Should you go in?")
        time.sleep(2)
        print("Where will you go...")
        print("1. Enter the cabin")
        print("2. Try to go around the cabin")
        print
        #go in the cabin or go around
        choice = chooseDir()
        #if they go in the cabin
        if choice == "1":
            print("You enter the cabin.")
            print("Inside you find a group of bandits.")
            print("The bandits steal all your armor and equipment.")
            print("They then leave you bare in the woods.")
        #if they try to go around
        elif choice == "2":
            print("You try to go around the cabin.")
            print("As you pass by you hear a wire trip.")
            print("Looking to your left your met with an arrow between the eyes")

                
"""Function:fieryMountain
   Purpose:Gives the player the firey mountain story and choices
   """
def fieryMountain():
    print("As you approach the base of the mountain")
    print("you see the mouth of a cave and a path leading")
    print("further up the mountain.")
    print("Where could the dragon be?")
    time.sleep(2)
    print("Where will you go...")
    print("1. Enter the cave")
    print("2. Follow the path up the mountain")
    print
    #deciding between the cave or the path
    choice = chooseDir()
    #go to cave
    if choice == "1":
        print("You begin towards the cave.")
        print("You enter the cave and spot the dragon.")
        print("You notice he is asleep.")
        print("You see two opportunities")
        print("One to attack head on the other to sneak around from behind")
        time.sleep(2)
        print("What will you do...")
        print("1. Attack head on")
        print("2. Try the sneak attack")
        print
        #attack head on or sneak attack
        choice = chooseDir()
        #if head on
        if choice == "1":
            print("The dragon awakes and you begin a fierce battle.")
            #Determine the outcome of the battle
            choice = random.randint(1,2)
            #converts choice to string, if the outcome if a win (1)
            if str(choice) == '1':
                print("After an attempt to eat you the dragons neck")
                print("Is exposed and you decapitate him.")
                print("Congradulations on saving the land.")
            #if you lose the fight
            else:
                print("You hold up your shield to block the dragons swipe")
                print("but he knocks it away. Your left lying on the ground.")
                print("As the dragon takes one giant breath he blows out a")
                print("curtain of fire engulfing you in the flames...")
        #if sneak attack
        elif choice == "2":
            print("The dragon wasn't actually sleeping.")
            print("As you try to sneak around him he takes")
            print("One big gulp and eats you.")
    #go to the path
    elif choice == "2":
         print("You walk towards the path.")
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
         #continue to climb or try to climb down
         choice = chooseDir()
         #if they climb back down
         if choice == "1":
            print("You start to climb back down the mountain.")
            print("As you begin your decent your leg slips.")
            print("You try to grab hold but you miss and fall...")
         #if they decide to climb up
         elif choice == "2":
            print("You choose to struggle on climbing higher.")
            print("Suddenly the mountain begins to rumble.")
            print("Fire and brimstone rain from above as the") 
            print("firey mountain erupts.")
            print("Lava begins to pour from above engulfing you.")

         
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
            print("You begin your journey to the Fiery Mountain.")
            fieryMountain()    
        #go to forest
        elif choice == "2":
            print("You walk towards the forest")
            darkForest()
        #ask user to play again
        print("Do you wish to play again?")
        print("1: Yes")
        print("2: No")
        choice = chooseDir()
        if choice == "2":
            play = False

if __name__ == "__main__": main()

                    