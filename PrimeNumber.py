# A default function for Prime checking conditions  
def CheckPrime(n):  
    # Taking an input number from the user  
    n = int(input("Enter your input number:"))  
    # Checking that given number is more than 1  
    if n > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(n/2) + 1):  
            # If the given number is divisible or not  
            if (n % j) == 0:  
                print(n, "is not a prime number")  
                break  
        # Else it is a prime number  
        else:  
            print(n, "is a prime number")  
    # If the given number is 1  
    else:  
        print(n, "is not a prime number")  

  
