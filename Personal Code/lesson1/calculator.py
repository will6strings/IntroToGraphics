""" Program: Calculator
    Author: Will Galbraith
    Date: 09/05/2013
    Purpose: simulates a calculator without the calculations
"""

""" Function:Main
    Purpose:Main function of the program
    Input:
    Output:
"""
def main():
    #defines boolean variable
    keepRunning = True
    
    print("Welcome to the calculator")
    
    #while loop
    while keepRunning:
        print("Please choose what you would like to do:")
        
        print("0: Addition")
        print("1: Subtraction")
        print("2: Multiplication")
        print("3: Division")
        print("4: Quit")
        
        choice = eval(raw_input())
        if choice == "0":
            print("You selected addition\n")
        elif choice == "1":
            print("You selected subtraction\n")
        elif choice == "2":
            print("You selected multiplication\n")
        elif choice == "3":
            print("You selected division\n")
        elif choice == "4":
            print("Bye")
            keepRunning = False
        else:
            print("Please choose a valid option.")
            print("\n")
            
if __name__ == "__main__": main()
    