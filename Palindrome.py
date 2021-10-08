
def check(s):
    return s == s[::-1]

def isPalindrome():
    s = input("Enter your string: ")
    ans = check(s)

    if ans:
        print("Palindrome")
    else:
        print("Not a Palindrome")
