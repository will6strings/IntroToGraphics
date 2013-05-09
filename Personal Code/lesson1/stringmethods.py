""" Project: String Methods
    Author: Will Galbraith
    Description: Playing around with the string methods
    Date: 9 May 2013"""

""" Function: Main
    Purpose: This is the main function
    Input:
    Output:
    """
    
def main():
    #asks for the user's name
    userName = raw_input("Please tell me your name: ")
    #Shows the name as all uppercase
    print ("I will shout your name: ", userName.upper())
    #Shows the name as all lowercase
    print ("Now all in lowercase: ", userName.lower())
    #Swaps the cases on userName
    print ("How about inverting the case? ", userName.swapcase())
    #Sets a value that is the length of char in name
    numChars = len(userName)
    #shows the name length
    print ("Your name has ", numChars, " characters.")
    #prints the name like a cartoon would say it
    print ("I will now pronounce your name like a cartoon character:")
    #changes the name to all upper case
    userName = userName.upper()
    #replaces any sign of 'R' with 'W'
    userName = userName.replace("R", "W")
    #first letter cap rest lower
    userName = userName.title()
    #shows the new name 
    print (userName)

#calls the main method
if __name__ == "__main__":main()
    