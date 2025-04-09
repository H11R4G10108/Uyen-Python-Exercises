"""
Description: Given an integer x, return true if x is a palindrome, and false otherwise.
A palindrome is a number that remains the same when its digits are reversed.
Input: an integer 
Output: a boolean value indicating whether the integer is a palindrome
"""

"""ver1"""
def isPalindrome(x):
        if x<0: return False # negative numbers are not palindromes
        if x==0: return True # 0 is a palindrome
        str_x=str(x)
        reverse=str_x[::-1] # reverse the string
        if reverse==str_x:
            return True
        else:
            return False
        
print(isPalindrome(121))  # True
print(isPalindrome(-121)) # False
print(isPalindrome(10))   # False

"""ver2"""
def isPalindrome2(x):
    if x<0: return False # negative numbers are not palindromes
    if x==0: return True # 0 is a palindrome
    phannguyen=x
    reverse=0
    while phannguyen!=0:
        phandu=phannguyen%10
        phannguyen=phannguyen//10
        reverse=reverse*10+phandu
    return reverse==x # check if the reversed number is equal to the original number

print(isPalindrome2(121))  # True
print(isPalindrome2(-121)) # False
print(isPalindrome2(10))   # False
