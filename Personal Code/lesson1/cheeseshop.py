def main():
    #tell the user something
    print ("Welcome to the cheese shop!")
    
    #get information from the user
    cheesetype = raw_input("What kind of cheese would you like?")
    
    #we dont have that kind ...
    print("Sorry, We're all out of")
    print(cheesetype)
    
if __name__ == "__main__": main()