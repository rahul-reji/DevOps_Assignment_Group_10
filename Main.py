#include files to be added here
import Calculator
import LeapYear
import PrimeNumber
import Palindrome

while(True):
    print("Hello User! What would you like to do today? -\n" \
            "1. Calculator\n" \
            "2. Check if Leap Year or Not\n" \
            "3. Check if Prime or Not\n" \
            "4. Check if Palindrome or Not\n" \
            "5. Exit\n")
    
    
    # Take input from the user 
    select = int(input("Select operations form 1, 2, 3, 4 : "))
    
    if select == 1:
        Calculator.calculator()
    
    elif select == 2:
        LeapYear.check()
    
    elif select == 3:
        PrimeNumber.CheckPrime()
        
    elif select == 4:
        Palindrome.isPalindrome()

    elif select == 5:
        quit()
