""" Program: Salami Word Slice
    Author: Will Galbraith
    Date: 09/05/2013
    Description: Demonstrates the split property 
    of strings using the word Salami
    """

""" Function:Main
    Purpose:Main function of the program
    Input:
    Output:
    """
def main():
    print("GUIDE:")
    print("0 1 2 3 4 5 6")
    print("|s|a|l|a|m|i|")
    #space
    print
    
    meat = "salami"
    #prints starting from 2 'l' and stops before 5 'i'
    print("meat[2:5]", meat[2:5])
    #prints everything before 3 'a'
    print("meat[:3]", meat[:3])
    #prints everything after and including 2 'l'
    print("meat[2:]", meat[2:])
    #prints everything after 3 'a'
    print("meat[-3:]", meat[-3:])
    #prints char at section 1 'a' 
    print("meat[1]", meat[1])
    
if __name__ == "__main__":main()