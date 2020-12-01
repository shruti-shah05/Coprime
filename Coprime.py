# DSC 430 : Python Programming 
# Assignment 0102 : Coprime
# Name : Shruti Shah

# GCD reference source : https://docs.python.org/3/library/fractions.html


import sys
from math import gcd

def coprime_test_loop():
    """
    The coprime_test_loop() function asks the user to enter two numbers and then pass those two numbers to coprime(a,b) function
    it will then print out the message indicating whether or not the numbers are coprime.
    it will keep asking the user to enter another pair of numbers until the user indicates that they wish to exit the program. 

    """
    while(True):
        # asking the user to enter two numbers and converting the user input into integers
        first_input= int(validateInput('Please enter the first number or type: exit to end the program:  '))
        second_input = int(validateInput('Please enter the second number or type: exit to end the program: '))
        
        # The if-else statements prints out the message indicating the result of coprime(a,b)
        if(coprime(first_input,second_input)):
            print('     The numbers are coprime\n')                          
        
        else:
            print('     The numbers NOT coprime\n')

 
def coprime(a,b):
    """
    The coprime(a,b) function will return true or false depending on whether or not the number are coprime.
    The if-else statements checks if the numbers are coprime using the GCD method.
    two numbers are said to be coprime if the greatest common divisor of them is 1

    """
    if(gcd(a,b) == 1):                  # checking if the gcd of two numbers is 1 or not, if it is then it will return true.
        return True
    else:
        return False

  
def validateInput(question):
    """
    # The checkConditions() is a helper function.
    # it checks wether the user inputs are valid or not, if the inputs are not valid, it will ask the user to enter the number again.

    """
    num = 0                                  # initializing variable
    while(True): 
        num = input(question)

        if(num.lower() == "exit"):            # if the user enters exit/EXIT, it will exit the program.
            print("Exiting the program...")
            sys.exit()

        # checks if the numbers are positive or not to be consider for it to be coprime.
        try:
            if(int(num) < 0):                     # if the numbers are less than 0, it will prompt the user to enter a positive number.
                print(" *** Only positive numbers are allowed.Please enter the number again.\n ")

            if(int(num) >= 0):
                break

        # checks if it contains any special character or letters
        except:                                 
            # it will print message to inform the user that only numbers are allowed.
            print(" *** Special chracters and letters are not allowed. Please enter only positive numbers.\n ")                 
            
    return num 
        
coprime_test_loop()